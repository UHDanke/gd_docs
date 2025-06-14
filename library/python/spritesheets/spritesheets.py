import os
import ast
import glob
import json
import plistlib
import numpy as np
from PIL import Image
import cv2



def _repl_edge(pil_img: Image.Image, pad=1) -> Image.Image:
    img_np = np.array(pil_img)
    img_np = cv2.copyMakeBorder(img_np, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    return Image.fromarray(img_np, mode='RGBA')



class Sprite:
    """
        Simple container for cocos2d-x plist frames.
    """ 
    
    __slots__ = ('x','y','w','h','offsetX','offsetY','trimW','trimH','origW','origH','is_rotated')
    
    def __init__(self, origin, size, offset, size_trim, size_orig, is_rotated):
        self.x, self.y = origin
        self.w, self.h = size
        self.offsetX, self.offsetY = offset
        self.offsetY *= -1 # Y offset is inverted in Cocos2d
        self.trimW, self.trimH = size_trim
        self.origW, self.origH = size_orig
        self.is_rotated = is_rotated
    
    
    def unpack(self, image, padding=0):
        x0 = (self.origW - self.trimW) // 2 + int(self.offsetX) + padding
        y0 = (self.origH - self.trimH) // 2 + int(self.offsetY) + padding
        x1 = self.x - padding
        y1 = self.y - padding
        
        if self.is_rotated:
            x2 = self.x + self.h + padding
            y2 = self.y + self.w + padding
        else:
            x2 = self.x + self.w + padding
            y2 = self.y + self.h + padding
        
        sprite = image.crop((x1, y1, x2, y2))
        
        if self.is_rotated:
            sprite = sprite.transpose(Image.ROTATE_90)
        
        new_sprite = Image.new(image.mode, (self.origW, self.origH), None)
        new_sprite.paste(sprite, (x0, y0))
        
        return new_sprite
    
    
    def repack(self, atlas, image, is_padded=False, generate_padding=True, padding=1):
        img = self.format_img(image, is_padded, generate_padding, padding)
        atlas.paste(img, (self.x-padding, self.y-padding))
    
                    
    def format_img(self, image, is_padded=False, generate_padding=True, padding=1):
        size_orig = (self.origW, self.origH)
        size_trim = (self.trimW, self.trimH)

        if is_padded:
            size_orig += 2*padding
            size_trim += 2*padding

        if image.size in [size_orig, size_trim]:
                sprite = image                
        else:
            trim = image.crop(image.getbbox())
            
            if image.size == size_trim:
                    sprite = trim
            else:
                raise ValueError()

        if not is_padded and padding > 0:
            if generate_padding:
                new_sprite = _repl_edge(sprite, pad=padding)
            else:
                blank = Image.new(image.mode, [x+2*padding for x in size_trim], None)
                new_sprite = blank.copy()
                new_sprite.paste(sprite,(padding, padding))
                
            sprite = new_sprite

                
        if self.is_rotated:
            sprite = sprite.transpose(image.ROTATE_90)
            
        return sprite
            
    
    
class SpriteSheet:
    """
        Sprite sheet class for handling cocos2d-x plist files. Currently only supports format 3.
    """
    
    def __init__(self, plist_path):
        self.plist_path = plist_path
        self.image_path = None # determined from metadata
        self.image = None
        self.sprites = {}
        self.metadata = None # grabbed on self._load()
        self._load()
    
    
    @property
    def plist_dir(self):
        return os.path.dirname(self.plist_path)


    @staticmethod
    def _parse_tuple(string):
        s = string.replace('{','(').replace('}',')')
        return ast.literal_eval(s)
    
    
    def _load(self):
        
        with open(self.plist_path, 'rb') as f:
            plist = plistlib.load(f)

        self.metadata = plist.get('metadata', {})
        size = self.metadata.get("size")
        self.metadata["size"] = self._parse_tuple(size)
        
        plist_format = self.metadata.get('format', None)
        
        match plist_format:
            case 3:
                self._process_format3(plist)
            case _:
                raise ValueError(f"Unsupported cocos2d-x format: {plist_format}")
                
        self.image_path = os.path.join(self.plist_dir, self.metadata.get("textureFileName"))
        self.image = Image.open(self.image_path)
    
    
    def _process_format3(self, plist):
        frames = plist.get('frames', {})

        for name, info in frames.items():
            origin, size = self._parse_tuple(info['textureRect'])
            offset = self._parse_tuple(info['spriteOffset'])
            size_trim = self._parse_tuple(info['spriteSize'])
            size_orig = self._parse_tuple(info['spriteSourceSize'])
            is_rotated = info.get('textureRotated', False)
            
            self.sprites[name] = Sprite(origin, size, offset, size_trim, size_orig, is_rotated)


    def unpack(self, output_dir, include_metadata=False, include_padding=False):
        
        print(f'Unpacking spritesheet: {self.image_path}')
        # create sub-folder
        os.makedirs(output_dir, exist_ok=True)
        
        # dump metadata
        if include_metadata: 
            with open("metadata.json", "w", encoding="utf-8") as f:
                json.dump(self.metadata, f, ensure_ascii=False, indent='\t')
        
        for sprite_name, sprite in self.sprites.items():
            print(f'\t- {sprite_name}')
            img = sprite.unpack(self.image)
            img.save(os.path.join(output_dir, sprite_name))
        
        print('\n')
     
            
    def repack(self, input_dir, output_dir, partial=True, is_padded=False, generate_padding=True, padding=1):
        
        image_paths = glob.glob(os.path.join(input_dir, "*.png"))
        image_names = [os.path.basename(img) for img in image_paths]
        
        if partial:
            base = self.image.copy()
        else:
            if not set(self.sprites.keys()).issubset(image_names):
                raise ValueError("Sprites missing from unpacked atlas, use partial packing if you are compiling a partial texture pack.")
            else:
                base = Image.new(self.image.mode, self.metadata.get("size"), None)
        
        image_set = set(self.sprites.keys()).intersection(image_names)
        
        for path in image_set:
            sprite = self.sprites.get(path, None)
            if sprite is None: continue
            
            img = Image.open(os.path.join(input_dir, path))
            sprite.repack(base, img, is_padded, generate_padding, padding)
        
        os.makedirs(output_dir, exist_ok=True)
        base.save(os.path.join(output_dir, os.path.basename(self.image_path)))
        
        
        
class SpriteResources:
    """
        Resource directory handler.
    """
    def __init__(self, path=None):
        self.sheets = dict()
        self._init(path)
    
    
    def _init(self, path):
        try:
            self.add_file(path)
        except:
            pass
        try:
            self.add_dir(path)
        except:
            pass
        
    class Sheet(SpriteSheet):

        def __init__(self, plist_path, base_dir):
            super().__init__(plist_path)
            self.base_dir = base_dir
            
            
    def add_file(self, plist_path):
        if not (os.path.exists(plist_path) and plist_path.endswith(".plist")):
            raise ValueError()
        
        dir_path = os.path.relpath(plist_path, os.path.dirname(plist_path))
        try:    
            spritesheet = self.Sheet(plist_path, dir_path)
            self.sheets[plist_path] = spritesheet
        except Exception as e:
            print(f'File skipped due to error while loading: {e}')
                
    
    
    def add_dir(self, dir_path, recursive=True, quality=None):
        if not os.path.isdir(dir_path):
            raise ValueError()
        
        if quality is None:
            suffix = ".plist"
        else:
            suffix = "-"+quality+".plist"
        
        if recursive:
            plist_files = glob.glob(os.path.join(dir_path,"**/*"+suffix), recursive=True)
        else:
            plist_files = glob.glob(os.path.join(dir_path,"*"+suffix))
        
        for plist_path in plist_files:

            try:    
                spritesheet = self.Sheet(plist_path, dir_path)
                self.sheets[plist_path] = spritesheet
            except Exception as e:
                print(f'File skipped due to error while loading: {e}')

       
    def unpack(self, output_dir, use_subdirs=True, include_metadata=False, include_padding=False):
        
        for sheet in self.sheets.values():
            subdir, _ = os.path.splitext(os.path.relpath(sheet.plist_path, sheet.base_dir))

            if use_subdirs:
                output_path = os.path.join(output_dir, subdir)
            else:
                output_path = output_dir

            sheet.unpack(output_path, include_metadata, include_padding)

    
    def repack(self, input_dir, output_dir, partial=True, is_padded=False, generate_padding=True, padding=1):
    
        for sheet in self.sheets.values():
            rel = os.path.relpath(sheet.plist_path, sheet.base_dir)
            subdir, _ = os.path.splitext(rel)
            img_path = os.path.join(input_dir, subdir)
            out_dir = os.path.join(output_dir, os.path.dirname(rel))
            sheet.repack(img_path, out_dir, partial, is_padded, generate_padding, padding)
            
    
    def create_subdirs(self, output_dir):
        
        for sheet in self.sheets.values():
            subdir, _ = os.path.splitext(os.path.relpath(sheet.plist_path, sheet.base_dir))
            output_path = os.path.join(output_dir, subdir)
            
            os.makedirs(output_path, exist_ok=True)
