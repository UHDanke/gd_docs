# Auto-Build

Auto-Build is a feature exclusive to smart blocks, accessible from Edit Special. It allows you to build structures using templates.

There are 2^8 \= 256 unique template variations using only blocks, out of which 46 (+1) are required and act as default for the others.  
With 1x1 slopes, there are 5\*6^8 \= 8 398 080 unique variations.  
With 2x1 slopes, there are 13\*(6^8+6^6\*4\*8+6^4\*4^2\*8\*5+6^2\*4^3\*8\*12+4^4\*4\*3\*2) \= 54 981 888 unique variations.

The Auto-Build system aims at cutting down the amount of templates needed to be manually created by the player by increasing the chances of a match with additional matching steps and options. 

Ideally, the player should define the templates they need and let the tool handle most of the work. Predicting the output of Auto-Build is difficult, so it is better to be reactive than proactive to template issues.

## Options

**Reference Only**

* Toggles smart block between normal and reference.

**Allow Rotation**

* Create also matches rotated templates.

**Allow Flip X**

* Create also matches horizontally flipped templates.

**Allow Flip Y**

* Create also matches vertically flipped templates.

**Ignore Corners**

* Create also matches templates with different corners.

**Use nearby as reference**

* Only fills in the selected objects, nearby unselected smart blocks are used as reference, even if placed on a different editor layer.

**Don't Delete**

* Smart blocks are not deleted after pasting a template.

**Back**

* Exit the menu.

**Create**

* Paste the given template.

**Template**

* Creates new templates from selected objects.

**Special**

* Use predefined templates.

**Browser**

* Local template browser.

**Create All**

* Pastes all required variations in a row using the given template.

**Paste Template**

* Pastes a premade set of shapes using the given template.

## Templating

Templating supports only grid-locked smart blocks. Exceptions are treated as if they were grid-locked, but results will vary.  
When templating, the maximum distance an object can be from the edges of the center tile and still be part of the template is 0.5 for other smart blocks and 1 for reference blocks.  
If you define a non-required template and its default template is undefined, the default will be highlighted in green and the non-required template will substitute it.  
Identical templates are merged into one single variation.  
All object properties, such as groups, layers, z order, extra options are saved within templates.  
Due to this it can sometimes be difficult to identify near identical templates in the variations browser.  
When using Create on a layer, the created objects will use the current layer instead. This does not apply for Editor L2 or on the "All" Layer.  
All blocks, besides other smart blocks, can be part of a template \- including triggers.  
It is not possible to template smart blocks, as they are ignored when using **Template**.  
Since they are ignored, the object properties of smart blocks do not matter when templating.

### 2x1 Slopes

For 2x1 slope templates, the center of the base of the slope (the bigger half) is used as the center of the template.  
A reference block can be placed in the same tile as the tip of the slope.  
The max distance an object can be from a 2x1 slope is longer by 1 block along the length of the slope.  
2x1 slopes used as reference blocks cannot overlap with other reference blocks.  
For the solid / air check, both halves are checked separately.

### Object Links

Object links are saved within templates, but how they are handled depends on whether a smart block is included in the object link.  
If the object link has no smart objects, then only the objects within the template's default range are included, still linked together.  
If the object link includes a smart object, then the entire linked object is going to be included in the template.  
If the object link includes only reference  objects, then the entire object link is ignored.  
If multiple smart objects are linked together, the one used as the center tile is the bottom-most, then left-most smart object.  
The remaining smart objects are ignored and will not be used as reference objects.  
Additionally, the only reference objects used are the ones within the 3x3 area around the center tile.

### Weights

When there are multiple variations per template, weights can be added using the **Add** button to randomize the choice.  
The final chances are calculated by dividing the variation's weight with the sum of the weights of all templates.  
**Add** adds 10 to the weights of the selected templates when clicked.  
**Zero** resets the weights of the selected templates to 0\.  
By default, with no weights defined, the top-most left-most variation is used.  
If at least one variation has a weight, all variations without a weight are excluded and marked with a "0" symbol.

### Matching Steps

When searching for a matching template, the game goes through the following steps, in this order:

* Exact matches  
* Match template with reference slopes as solid block if the slope is connected to a tile, otherwise as air.  
* Match template with all reference slopes as solid blocks.  
* Use the default template (if it exists).

Each step also does the following matches, in this order, if the corresponding option is enabled:

* Exact  
* Flipped (X, Y, XY)  
* Rotated (-90, \-180, \-270)  
* Ignore Corners

### Default Templates

Below you can view a visual guide of all default templates and their variations.  
Highlighted in white are the default templates for other templates that include any of the smart objects highlighted in red.  

<img src="https://github.com/user-attachments/assets/3c867688-2381-41a9-9c15-ca77dd73e5d5" width="85%">
