# Link Visible

Makes all objects part of a group active if at least one of them is active.

## Behavior

This trigger is activated on level load no matter where its placed. It cannot be activated later or deactivated in any way.

Objects count as being active if they are on-screen.

### Toggle

Toggled off objects count as inactive for Link Visible.

### UI

UI objects that are visible on-screen also count as active for Link Visible.

### Object Linking

Object Links and Group ID Parents are ignored by Link Visible.

### Invisible Objects

Making the object invisible with Hide, Alpha, Opacity or Blending does not make them inactive.