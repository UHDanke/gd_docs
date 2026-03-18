# Area Performance and Optimization

Area triggers reapply their effect every tick, so they put a constant strain on the processor.
Lag components can be split in two categories:
- Strength calculations for each target
- Effect application

Out of the two, applying area effects is the much more demanding one.

Enter triggers are far more optimized and should not be replaced by Area triggers.

## Effect Strength

If the resulting effect strength is 0, no Area effect will be applied.

Certain proximity options will make the Area affect less (or more) targets depending on the strength calculation.

## Object Links

Transformations (Scale, Rotate) and color operations (Fade, Tint) are applied per object even when using object links.

Scaling and rotation on object links also applies movement on all objects linked to the target, which is done per object. This makes Area Scale and Rotate the laggiest Area triggers when using object links.

Movements are optimized for multiple objects, using object links with Area Move can make use of this optimization and significantly reduce lag.

Overall, Area Move is the only Area trigger that sees a significant improvement from using object links. Area Fade and Tint have negligible increases from reducing the amount of targets that need to be calculated while Area Scale and Rotate are negatively impacted by it.

## Fade and Tint

Area Fade and Tint effects are applied only on visible targets that are not toggled off. This includes completely transparent targets done using either the Hide object option, color blending, color opacity or Alpha triggers.

If there are multiple Area Fade triggers per target, all will do the strength calculation but only the strongest (or first) effect will be applied. This is not the case for other Area effects where all are applied.

## Scale, Rotate and Move

Whether Area Scale, Rotate and Move is applied on toggled off targets is inconsistent and depends on length and deadzone settings. Toggling off targets has no effect in most common cases, so toggling shouldn't be considered a reliable way to optimize these effects.
