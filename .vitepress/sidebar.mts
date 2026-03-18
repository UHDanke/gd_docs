export default [
  {
    text: 'About',
    link: '/index'
  },
  {
    text: 'Credits',
    link: '/credits'
  },
  {
    text: 'To Do List',
    link: '/to_do_list'
  },
  {
    text: 'Editor',
    collapsed: true,
    items: [
      {
        text: 'Colors & Layers',
        collapsed: true,
        items: [
          {
            text: 'Color Assignment',
            link: '/editor/colors_layers/color_assignment'
          },
          {
            text: 'Color Channels',
            link: '/editor/colors_layers/color_channels'
          },
          {
            text: 'Color Sliders',
            link: '/editor/colors_layers/color_sliders'
          },
          {
            text: 'Other Color & Layering Options',
            link: '/editor/colors_layers/other_color_and_layering_options'
          },
          {
            text: 'Rendering Order',
            link: '/editor/colors_layers/rendering_order'
          },
          {
            text: 'Select Color Menu',
            link: '/editor/colors_layers/select_color_menu'
          }
        ]
      },
      {
        text: 'Autobuild',
        link: '/editor/autobuild'
      },
      {
        text: 'Extra Object Options',
        link: '/editor/extra_object_options'
      }
    ]
  },
  {
    text: 'Triggers',
    collapsed: true,
    items: [
      {
        text: 'General',
        collapsed: true,
        items: [
          {
            text: 'Trigger Activation',
            link: '/triggers/general/trigger_activation'
          },
          {
            text: 'Trigger Channels',
            link: '/triggers/general/trigger_channels'
          },
          {
            text: 'Target Behavior',
            link: '/triggers/general/target_behavior'
          },
          {
            text: 'Game Loop',
            link: '/triggers/general/game_loop'
          },
          {
            text: 'ID Limits',
            link: '/triggers/general/id_limits'
          },
          {
            text: 'Durations',
            link: '/triggers/general/durations'
          },
          {
            text: 'Easings',
            link: '/triggers/general/easings'
          }
        ]
      },
      {
        text: 'Animate',
        collapsed: true,
        items: [
          {
            text: 'Animated Objects',
            link: '/triggers/animate/animated_objects'
          },
          {
            text: 'Animate Trigger',
            link: '/triggers/animate/animate_trigger'
          },
          {
            text: 'Edit Animation',
            link: '/triggers/animate/edit_animation'
          },
          {
            text: 'Particle Object',
            link: '/triggers/animate/particle_object'
          },
          {
            text: 'Spawn Particle',
            link: '/triggers/animate/spawn_particle'
          }
        ]
      },
      {
        text: 'Area',
        collapsed: true,
        items: [
          {
            text: 'Area Triggers',
            link: '/triggers/area/area_triggers'
          },
          {
            text: 'Edit Area Triggers',
            link: '/triggers/area/edit_area_triggers'
          },
          {
            text: 'Area Stop',
            link: '/triggers/area/area_stop'
          }
        ]
      },
      {
        text: 'Audio',
        collapsed: true,
        items: [
          {
            text: 'Game Audio Settings',
            link: '/triggers/audio/game_audio_settings'
          },
          {
            text: 'FMOD',
            link: '/triggers/audio/fmod'
          },
          {
            text: 'Primary Song',
            link: '/triggers/audio/primary_song'
          },
          {
            text: 'Pitch & Speed',
            link: '/triggers/audio/pitch_speed'
          },
          {
            text: 'Song',
            link: '/triggers/audio/song_trigger'
          },
          {
            text: 'Edit Song',
            link: '/triggers/audio/edit_song'
          },
          {
            text: 'Song Guidelines',
            link: '/triggers/audio/song_guidelines'
          },
          {
            text: 'SFX',
            link: '/triggers/audio/sfx'
          },
          {
            text: 'Edit SFX',
            link: '/triggers/audio/edit_sfx'
          },
          {
            text: 'Loop',
            link: '/triggers/audio/loop'
          },
          {
            text: 'Volume Proximity',
            link: '/triggers/audio/volume_proximity'
          },
          {
            text: 'BPM Guide',
            link: '/triggers/audio/bpm_guide'
          }
        ]
      },
      {
        text: 'Camera',
        collapsed: true,
        items: [
          {
            text: 'Default Camera Properties',
            link: '/triggers/camera/default_camera_properties'
          },
          {
            text: 'Camera Mode',
            link: '/triggers/camera/camera_mode'
          },
          {
            text: 'Camera Guide',
            link: '/triggers/camera/camera_guide'
          },
          {
            text: 'Gameplay Offset',
            link: '/triggers/camera/gameplay_offset'
          },
          {
            text: 'Offset Camera',
            link: '/triggers/camera/offset_camera'
          },
          {
            text: 'Rotate Camera',
            link: '/triggers/camera/rotate_camera'
          },
          {
            text: 'Zoom Camera',
            link: '/triggers/camera/zoom_camera'
          },
          {
            text: 'Camera Edge',
            link: '/triggers/camera/camera_edge'
          }
        ]
      },
      {
        text: 'Collisions',
        collapsed: true,
        items: [
          {
            text: 'Collision Objects',
            link: '/triggers/collisions/collision_objects'
          },
          {
            text: 'Collision Trigger',
            link: '/triggers/collisions/collision_trigger'
          },
          {
            text: 'Instant Collision Trigger',
            link: '/triggers/collisions/instant_collision_trigger'
          },
          {
            text: 'State Blocks',
            link: '/triggers/collisions/state_blocks'
          },
          {
            text: 'Performance Optimization',
            link: '/triggers/collisions/performance_optimization'
          }
        ]
      },
      {
        text: 'Follows',
        collapsed: true,
        items: [
          {
            text: 'Follow',
            link: '/triggers/follows/follow'
          },
          {
            text: 'Follow Player Y',
            link: '/triggers/follows/follow_player_y'
          },
          {
            text: 'Advanced Follow',
            link: '/triggers/follows/advanced_follow'
          },
          {
            text: 'Edit Advanced Follow',
            link: '/triggers/follows/edit_advanced_follow'
          },
          {
            text: 'Retarget Advanced Follow',
            link: '/triggers/follows/retarget_advanced_follow'
          }
        ]
      },
      {
        text: 'Items',
        collapsed: true,
        items: [
          {
            text: 'Pickup',
            link: '/triggers/items/pickup'
          },
          {
            text: 'Count',
            link: '/triggers/items/count'
          },
          {
            text: 'Instant Count',
            link: '/triggers/items/instant_count'
          },
          {
            text: 'Item Edit',
            link: '/triggers/items/item_edit'
          },
          {
            text: 'Item Compare',
            link: '/triggers/items/item_compare'
          },
          {
            text: 'Item Persist',
            link: '/triggers/items/item_persist'
          },
          {
            text: 'Time',
            link: '/triggers/items/time'
          },
          {
            text: 'Time Control',
            link: '/triggers/items/time_control'
          },
          {
            text: 'Time Event',
            link: '/triggers/items/time_event'
          },
          {
            text: 'Counter Labels',
            link: '/triggers/items/counter_labels'
          }
        ]
      },
      {
        text: 'Level',
        collapsed: true,
        items: [
          {
            text: 'BG Effect On/Off',
            link: '/triggers/level/bg_effect_on_off'
          },
          {
            text: 'BG Speed',
            link: '/triggers/level/bg_speed'
          },
          {
            text: 'Change Background',
            link: '/triggers/level/change_background'
          },
          {
            text: 'Change Ground',
            link: '/triggers/level/change_ground'
          },
          {
            text: 'Change Middleground',
            link: '/triggers/level/change_middleground'
          },
          {
            text: 'MG Speed',
            link: '/triggers/level/mg_speed'
          },
          {
            text: 'Offset MG Y',
            link: '/triggers/level/offset_mg_y'
          }
        ]
      },
      {
        text: 'Misc',
        collapsed: true,
        items: [
          {
            text: 'Collectibles',
            link: '/triggers/misc/collectibles'
          },
          {
            text: 'End',
            link: '/triggers/misc/end'
          },
          {
            text: 'Event',
            link: '/triggers/misc/event'
          },
          {
            text: 'On Death',
            link: '/triggers/misc/on_death'
          },
          {
            text: 'Options',
            link: '/triggers/misc/options'
          },
          {
            text: 'Reset',
            link: '/triggers/misc/reset'
          },
          {
            text: 'Stop',
            link: '/triggers/misc/stop'
          },
          {
            text: 'Timewarp',
            link: '/triggers/misc/timewarp'
          },
          {
            text: 'Toggle',
            link: '/triggers/misc/toggle'
          },
          {
            text: 'Toggle Object',
            link: '/triggers/misc/toggle_object'
          },
          {
            text: 'Touch',
            link: '/triggers/misc/touch'
          }
        ]
      },
      {
        text: 'Player',
        collapsed: true,
        items: [
          {
            text: 'Disable/Enable Player Trail',
            link: '/triggers/player/disable_enable_player_trail'
          },
          {
            text: 'Show/Hide Player',
            link: '/triggers/player/show_hide_player'
          },
          {
            text: 'Player Control',
            link: '/triggers/player/player_control'
          },
          {
            text: 'Gravity',
            link: '/triggers/player/gravity'
          },
          {
            text: 'Reverse',
            link: '/triggers/player/reverse'
          },
          {
            text: 'Gameplay Arrow',
            link: '/triggers/player/gameplay_arrow'
          }
        ]
      },
      {
        text: 'Spawn',
        collapsed: true,
        items: [
          {
            text: 'Activation Limits',
            link: '/triggers/spawn/activation_limits'
          },
          {
            text: 'Adv Random',
            link: '/triggers/spawn/adv_random'
          },
          {
            text: 'Random',
            link: '/triggers/spawn/random'
          },
          {
            text: 'Sequence',
            link: '/triggers/spawn/sequence'
          },
          {
            text: 'Spawn Remapping',
            link: '/triggers/spawn/spawn_remapping'
          },
          {
            text: 'Spawn Trigger',
            link: '/triggers/spawn/spawn_trigger'
          }
        ]
      },
      {
        text: 'Transforms',
        collapsed: true,
        items: [
          {
            text: 'Animate Keyframe',
            link: '/triggers/transforms/animate_keyframe'
          }
        ]
      },
      {
        text: 'Visual',
        collapsed: true,
        items: [
          {
            text: 'Color',
            link: '/triggers/visual/color'
          },
          {
            text: 'Pulse',
            link: '/triggers/visual/pulse'
          },
          {
            text: 'Alpha',
            link: '/triggers/visual/alpha'
          },
          {
            text: 'Shake',
            link: '/triggers/visual/shake'
          },
          {
            text: 'Link Visible',
            link: '/triggers/visual/link_visible'
          },
          {
            text: 'UI',
            link: '/triggers/visual/ui'
          }
        ]
      }
    ]
  },
  {
    text: 'Bugs',
    collapsed: true,
    items: [
      {
        text: 'Overview',
        link: '/bugs/README'
      },
      {
        text: 'Misc',
        link: '/bugs/misc'
      },
      {
        text: 'Advanced Follow',
        link: '/bugs/advanced_follow'
      },
      {
        text: 'Area Triggers',
        link: '/bugs/area_triggers'
      },
      {
        text: 'Arrow Trigger',
        link: '/bugs/arrow_trigger'
      },
      {
        text: 'Collisions',
        link: '/bugs/collisions'
      },
      {
        text: 'Editor',
        link: '/bugs/editor'
      },
      {
        text: 'Enter Effects',
        link: '/bugs/enter_effects'
      },
      {
        text: 'Events',
        link: '/bugs/events'
      },
      {
        text: 'Gradient',
        link: '/bugs/gradient'
      },
      {
        text: 'Items & Timers',
        link: '/bugs/items_and_timers'
      },
      {
        text: 'Keyframes',
        link: '/bugs/keyframes'
      },
      {
        text: 'Move Trigger',
        link: '/bugs/move_trigger'
      },
      {
        text: 'Particles',
        link: '/bugs/particles'
      },
      {
        text: 'Spawn Triggers',
        link: '/bugs/spawn_triggers'
      },
      {
        text: 'Uncategorized',
        link: '/bugs/uncategorized'
      }
    ]
  }
];

