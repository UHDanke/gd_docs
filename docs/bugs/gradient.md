# Gradient

## Gradient doesn't account for screen rotation when loading the level

**Version:** 2.207
**Date:** Thu Dec 18 2025 00:00:00 GMT+0200 (Eastern European Standard Time)

### Description
Gradient triggers without any references (ID 0) use the screen's edges as reference instead. These edges are initialized when the level loads, however, if the camera trigger is placed before the origin camera rotation isn't taken into account. Example: ![image](https://github.com/user-attachments/assets/e2baf11d-2f0b-45e5-bbc9-e15dc3fd271e)

## UI Gradient doesn't work

**Version:** 2.207

### Description
Gradients on UI layer and above do not follow the screen. An unused layer ID exists where gradients do follow the screen, BUT it renders above BG layer.
