# Easing Formulas

## Ease

$$EaseIn(x,\ easeRate) =
  \begin{cases}
    0 & \text{for} & x \le 0\\
    x*0.01^{(1-easeRate)} & \text{for}& 0 < x \le 0.01 \\
    x^{easeRate} & \text{for}& 0.01 < x < 1 \\
    1 & \text{for}& x \ge 1
  \end{cases}$$

  $$EaseOut(x,\ easeRate) =
  \begin{cases}
    0 & \text{for} & x \le 0\\
    x^{easeRate^{-1}} & \text{for}& 0 < x < 1 \\
    1 & \text{for}& x \ge 1
  \end{cases}$$

$$EaseInOut(x,\ easeRate) =
  \begin{cases}
    EaseIn(2\cdot x,\ easeRate)/2 & \text{for}& x < 0.5 \\
    1-EaseIn(2-2\cdot x,\ easeRate)/2 & \text{for}&  x \ge 0.5
  \end{cases}$$

### Notes

Ease In values below 1% and Ease In Out values below 0.5% and above 99.5% are linearly approximated.

Ease rate is limited between 0.10 and 20.00.

## Elastic

$$ElasticIn(x,\ easeRate) =
  \begin{cases}
    0 & \text{for} & x \le 0\\
    ExponentialIn(x)\cdot\sin(\pi\cdot(0.5+\frac{2-2\cdot x}{easeRate})) & \text{for}& 0 < x < 1 \\
    1 & \text{for}& x \ge 1
  \end{cases}$$

$$ElasticOut(x,\ easeRate) = 1-ElasticIn(1-x,\ easeRate)$$

$$ElasticInOut(x,\ easeRate) =
  \begin{cases}
    2^{9}\cdot ElasticIn(2\cdot x,\ easeRate)& \text{for}& 0 < x < 0.5 \\
    1-2^{9}\cdot ElasticIn(2-2\cdot x,\ easeRate) & \text{for}& 0.5 \leq x < 1
  \end{cases}$$

### Notes

Trigonometric functions are approximated and linearly interpolated using a table of 101 points (1% divisions). This is much more noticeable on elastic easings with very low ease rate.

Ease rate is limited between 0.10 and 20.00.

## Bounce

$$BounceIn(x) = 1-BounceOut(1-x)$$

$$BounceOut(x) =
  \begin{cases}
    0 & \text{for} & x \le 0\\
    7.5625\cdot x^{2} & \text{for}& 0 < x < 2.75^{-1} \\
    7.5625\cdot(x-\frac{1.5}{2.75})\cdot x + 0.75 & \text{for}& 2.75^{-1} < x < 1.1375^{-1} \\
    7.5625\cdot(x-\frac{2.25}{2.75})\cdot x + 0.9375 & \text{for}& 1.1375^{-1} < x < 1.1^{-1} \\
    7.5625\cdot(x-\frac{2.625}{2.75})\cdot x + 0.984375 & \text{for}& 1.1^{-1} < x < 1 \\
    1 & \text{for}& x \ge 1
  \end{cases}$$

  $$BounceInOut(x) =
  \begin{cases}
    (1-BounceOut(1-2\cdot x))/2 & \text{for}& 0 < x < 0.5 \\
    (1+BounceOut(2\cdot x-1))/2 & \text{for}& 0.5 \leq x < 1
  \end{cases}$$

## Exponential

$$ExponentialIn(x) =
  \begin{cases}
    0 & \text{for} & x \le 0\\
    2^{10\cdot (x -1)} & \text{for}& 0 < x < 1 \\
    1 & \text{for}& x \ge 1
  \end{cases}$$

$$ExponentialOut(x) = 1-ExponentialIn(1-x)$$

$$ExponentialInOut(x) =
  \begin{cases}
    2^{9}\cdot ExponentialIn(2\cdot x)& \text{for}& 0 < x < 0.5 \\
    1-2^{9}\cdot ExponentialIn(2-2\cdot x) & \text{for}& 0.5 \leq x < 1
  \end{cases}$$

## Sine

$$SineIn(x) =
  \begin{cases}
    0 & \text{for} & x \le 0\\
    1-\cos(0.5\cdot\pi\cdot x) & \text{for}& 0 < x < 1 \\
    1 & \text{for}& x \ge 1
  \end{cases}$$

$$SineOut(x) = 1-SineIn(1-x)$$

$$SineInOut(x) =
  \begin{cases}
    SineIn(x)/2 & \text{for}& x < 0.5 \\
    0.5+SineOut(x-0.5)/2 & \text{for}&  x \ge 0.5
  \end{cases}$$

### Notes

Trigonometric functions are approximated and linearly interpolated using a table of 101 points (1% divisions). This is not noticeable in the case of sine easings.

## Back

$$BackIn(x) =
  \begin{cases}
    0 & \text{for} & x \le 0\\
    3.5949095\cdot x^{3}-2.5949095\cdot x^{2} & \text{for}& 0 < x < 1 \\
    1 & \text{for}& x \ge 1
  \end{cases}$$

$$BackOut(x) = 1-BackIn(1-x)$$

$$BackInOut(x,\ easeRate) =
  \begin{cases}
    BackIn(2\cdot x)/2 & \text{for}& x < 0.5 \\
    1-BackIn(2-2\cdot x)/2 & \text{for}&  x \ge 0.5
  \end{cases}$$