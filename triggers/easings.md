# Easing Formulas

## Ease

$$EaseIn(x,\ easeRate) = 
  \begin{cases}
    0 & \text{for} & x \le 0\\
    x^{easeRate} & \text{for}& 0 < x < 1 \\
    1 & \text{for}& 1 \le x
  \end{cases}$$
  
$$EaseOut(x,\ easeRate) = EaseIn(x,easeRate^{-1})$$

$$EaseInOut(x,\ easeRate) = 
  \begin{cases}
    EaseIn(2\cdot x,\ easeRate)/2 & \text{for}& x < 0.5 \\
    1-EaseIn(2-2\cdot x,\ easeRate)/2 & \text{for}&  x \ge 0.5
  \end{cases}$$


## Elastic

$$ElasticIn(x,\ easeRate) = 
  \begin{cases}
    0 & \text{for} & 0 \le x\\
    ExponentialIn(x)\cdot\sin(\pi\cdot(0.5+\frac{2-2\cdot x}{easeRate})) & \text{for}& 0 < x < 1 \\
    1 & \text{for}& x \ge 1
  \end{cases}$$
  
$$ElasticOut(x,\ easeRate) = ElasticIn(1-x,\ easeRate)$$

$$ElasticInOut(x,\ easeRate) = 
  \begin{cases}
    2^{9}\cdot ElasticIn(2\cdot x,\ easeRate)& \text{for}& 0 < x < 0.5 \\
    1-2^{9}\cdot ElasticIn(2-2\cdot x,\ easeRate) & \text{for}& 0.5 \leq x < 1
  \end{cases}$$

## Exponential

$$ExponentialIn(x) = 
  \begin{cases}
    0 & \text{for} & 0 \le x\\
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
    0 & \text{for} & 0 \le x\\
    1-\cos(0.5\cdot\pi\cdot x) & \text{for}& 0 < x < 1 \\
    1 & \text{for}& x \ge 1
  \end{cases}$$
  
$$SineOut(x) = 
  \begin{cases}
    0 & \text{for} & 0 \le x\\
   \sin(0.5\cdot\pi\cdot x) & \text{for}& 0 < x < 1 \\
    1 & \text{for}& x \ge 1
  \end{cases}$$
  
$$SineInOut(x) = 
  \begin{cases}
    SineIn(x)/2 & \text{for}& x < 0.5 \\
    0.5+SineOut(x-0.5)/2 & \text{for}&  x \ge 0.5
  \end{cases}$$
