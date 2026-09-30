# DerivateGauss (Operator)

## Name

`DerivateGauss` — Convolve an image with derivatives of the Gaussian.

## Signature

`static void HOperatorSet.DerivateGauss(HObject image, out HObject derivGauss, HTuple sigma, HTuple component)`

`HImage HImage.DerivateGauss(HTuple sigma, string component)`

`HImage HImage.DerivateGauss(double sigma, string component)`

## Description

`DerivateGauss` convolves an image with the derivatives of a
Gaussian and calculates various features derived therefrom.
*`sigma`* is the parameter of the Gaussian (i.e., the amount of
smoothing). If one value is passed in *`sigma`* the amount of
smoothing in the column and row direction is identical. If two
values are passed in *`sigma`* the first value specifies the
amount of smoothing in the column direction, while the second value
specifies the amount of smoothing in the row direction. The
possible values for *`component`* are:

- ***"none"*:** —

  Smoothing only.
- ***"x"*:** —

  First derivative along x.
  $$g'(x, y) = \frac{\partial g(x, y)}{\partial x}$$ ![figure](../assets/3c3562b0b5f46923.svg)
- ***"y"*:** —

  First derivative along y.
  $$g'(x,y) = \frac{\partial g(x,y)}{\partial y}$$ ![figure](../assets/e00786f24b80ab41.svg)
- ***"gradient"*:** —

  Absolute value of the gradient.
  $$g'(x,y) = \sqrt{ \frac{ \partial g(x,y) }{ \partial x }^2 \; \frac{ \partial g(x,y) }{ \partial y }^2 }$$ ![figure](../assets/c4f01a82cd50f539.svg)
- ***"gradient_dir"*:** —

  Gradient direction in radians.
  $$\phi = \mathrm{atan2}\left(\frac{\partial g(x,y)}{\partial y}, \frac{\partial g(x,y)}{\partial x}\right)$$ ![figure](../assets/9211fc4296f49807.svg)
- ***"xx"*:** —

  Second derivative along x.
  $$g'(x,y) = \frac{\partial^2 g(x,y)}{\partial x^2}$$ ![figure](../assets/36000c321c4ed774.svg)
- ***"yy"*:** —

  Second derivative along y.
  $$g'(x,y) = \frac{\partial^{2} g(x,y)}{\partial y^{2}}$$ ![figure](../assets/b7d0aa3af092e943.svg)
- ***"xy"*:** —

  Second derivative along x and y.
  $$g'(x,y)=\frac{\partial^{2} g(x,y)}{\partial x \partial y}$$ ![figure](../assets/a5f94431c67c82c9.svg)
- ***"xxx"*:** —

  Third derivative along x.
  $$g'(x,y) = \frac{\partial^{3} g(x,y)}{\partial x^{3}}$$ ![figure](../assets/146c7b56095eb787.svg)
- ***"yyy"*:** —

  Third derivative along y.
  $$g'(x, y) = \frac{\partial^{3} g(x, y)}{\partial y^{3}}$$ ![figure](../assets/4a494d6451493119.svg)
- ***"xxy"*:** —

  Third derivative along x, x and y.
  $$g'(x,y) = \frac{\partial^3 g(x,y)}{\partial x^2 \partial y}$$ ![figure](../assets/cf620a1b7ccccfff.svg)
- ***"xyy"*:** —

  Third derivative along x, y and y.
  $$g'(x,y) = \frac{\partial^{3} g(x,y)}{\partial x \partial y^{2}}$$ ![figure](../assets/d97243ecd95b0a7e.svg)
- ***"det"*:** —

  Determinant of the Hessian matrix:
  $$DET = \frac{\partial^{2}g(x,y)}{\partial x^{2}} \frac{\partial^{2}g(x,y)}{\partial y^{2}} - \left( \frac{\partial^{2}g(x,y)}{\partial y \partial x} \right)^{2}$$ ![figure](../assets/7eb47eb761703744.svg)
- ***"laplace"*:** —

  Laplace operator (trace of the Hessian matrix):
  $$TR = \frac{\partial^{2} g(x,y)}{\partial x^{2}} + \frac{\partial^{2} g(x,y)}{\partial y^{2}}$$ ![figure](../assets/a5872f7009acf39a.svg)
- ***"mean_curvature"*:** —

  Mean curvature H
  $$a = \left(1 + \frac{\partial g(x,y)^2}{\partial x} \right) \frac{\partial^2 g(x,y)}{\partial y^2}\\ b = 2 \frac{\partial g(x,y) \partial g(x,y) \partial^2 g(x,y)}{\partial x \partial y \partial y x} \\c = \left(1 + \frac{\partial g(x,y)^2}{\partial y} \right) \frac{\partial^2 g(x,y)}{\partial x^2}\\d = \left(1 + \frac{\partial g(x,y)^2}{\partial x} + \frac{\partial g(x,y)}{\partial y} \right)^{3/2} \\H = \frac{a - b + c}{d} \\H = \frac{1}{2}(\kappa_{min} + \kappa_{max})$$ ![figure](../assets/f5869b515acb0383.svg)
- ***"gauss_curvature"*:** —

  Gaussian curvature K
  $$K = \frac{DET}{\left(1 + \frac{\partial g(x,y)}{\partial x}^2 + \frac{\partial g(x,y)}{\partial y}^2\right)^2}$$ ![figure](../assets/4ad2c9a14e3a190b.svg)
- ***"area"*:** —

  Differential Area A
  $$A = EG - F^2 E = 1 + \frac{\partial g(x,y)}{\partial x}^2 F = \frac{\partial g(x,y) \partial g(x,y)}{\partial x \partial y} G = 1 + \frac{\partial g(x,y)^2}{\partial y}$$ ![figure](../assets/5c443b9661dec222.svg)
- ***"eigenvalue1"*:** —

  First eigenvalue
  $$a = \frac{\frac{\partial^2 g(x,y)}{\partial x^2} + \frac{\partial^2 g(x,y)}{\partial y^2}}{2} \\\n\\\ \\lambda_{1} = a + \sqrt{a^2 - \left(\frac{\partial^2 g(x,y)}{\partial x^2} \frac{\partial^2 g(x,y)}{\partial y^2} - \frac{\partial^2 g(x,y)}{\partial y \partial x} \right)}$$ ![figure](../assets/f1e0dad6ad6c4352.svg)
- ***"eigenvalue2"*:** —

  Second eigenvalue
  $$a = \frac{\frac{\partial^2 g(x,y)}{\partial x^2} + \frac{\partial^2 g(x,y)}{\partial y^2}}{2} \\\\lambda_2 = a - \sqrt{a^2 - \left(\frac{\partial^2 g(x,y)}{\partial x^2} \frac{\partial^2 g(x,y)}{\partial y^2} - \frac{\partial^2 g(x,y)}{\partial y \partial x}\right)}$$ ![figure](../assets/b92a4f811ddb147e.svg)
- ***"eigenvec_dir"*:** —

  Direction of the eigenvector corresponding to the first eigenvalue
  in radians
- **'main1_curvature'** —

  First main curvature
  $$k_{max} = H + \sqrt{H^{2} - K}$$ ![figure](../assets/84297f0db7c8fc3a.svg)
- **'main2_curvature'** —

  Second main curvature
  $$k_{min} = H - \sqrt{H^2 - K}$$ ![figure](../assets/b5ef94258ab88825.svg)
- ***"kitchen_rosenfeld"*:** —

  Second derivative perpendicular to the gradient
  $$k = \frac{\frac{\partial^{2} g(x,y)}{\partial x^{2}} \frac{\partial g(x,y)}{\partial y} + \frac{\partial^{2} g(x,y)}{\partial y^{2}} \frac{\partial g(x,y)}{\partial x} - 2 \frac{\partial^{2} g(x,y)}{\partial y\partial x} \frac{\partial g(x,y)}{\partial y} \frac{\partial g(x,y)}{\partial x}}{\frac{\partial g(x,y)^{2}}{\partial x} + \frac{\partial g(x,y)^{2}}{\partial y}}$$ ![figure](../assets/0e61b9fa86eac835.svg)
- ***"zuniga_haralick"*:** —

  Normalized second derivative perpendicular to the gradient
  $$k = \frac{ \frac{\partial^2 g(x,y)}{\partial x^2} \frac{\partial g(x,y)}{\partial y}^2 + \frac{\partial^2 g(x,y)}{\partial y^2} \frac{\partial g(x,y)}{\partial x}^2 - 2 \frac{\partial^2 g(x,y)}{\partial y\partial x} \frac{\partial g(x,y)}{\partial x} \frac{\partial g(x,y)}{\partial y} }{ ( \frac{\partial g(x,y)}{\partial x}^2 + \frac{\partial g(x,y)}{\partial y}^2 )^{3/2} }$$ ![figure](../assets/3fcf013308333536.svg)
- ***"2nd_ddg"*:** —

  Second derivative along the gradient
  $$k = \frac{\frac{\partial^2 g(x,y)}{\partial x^2} \frac{\partial g(x,y)}{\partial x} + 2 \frac{\partial g(x,y)}{\partial x} \frac{\partial g(x,y)}{\partial y} \frac{\partial^2 g(x,y)}{\partial y \partial x} + \frac{\partial^2 g(x,y)}{\partial y^2} \frac{\partial g(x,y)}{\partial y}}{\frac{\partial g(x,y)^2}{\partial x} + \frac{\partial g(x,y)^2}{\partial y}}$$ ![figure](../assets/068890d27f88735d.svg)
- ***"de_saint_venant"*:** —

  Second derivative along and perpendicular to the gradient
  $$k = \frac{\frac{\partial g(x,y)}{\partial x} \frac{\partial g(x,y)}{\partial y} (\frac{\partial^2 g(x,y)}{\partial x^2} - \frac{\partial^2 g(x,y)}{\partial y^2}) - (\frac{\partial g(x,y)}{\partial x} - \frac{\partial g(x,y)}{\partial y}) \frac{\partial^2 g(x,y)}{\partial x \partial y}}{\frac{\partial g(x,y)^2}{\partial x} + \frac{\partial g(x,y)^2}{\partial y}}$$ ![figure](../assets/6a816848c0d1b936.svg)

## Attention

Besides the pure C version there are specific implementations of
`DerivateGauss` for speed up.
Such an optimization is applied in case it is supported by the system and
the respective system parameter `*_enable` is set to
*"true"*, see [`SetSystem`](set_system.md).
The following optimizations are supported (listed according to their
priority):

- using *AVX512f* instructions (*"avx512f_enable"*)
- using *AVX* instructions (*"avx_enable"*)
- using *SSE2* instructions (*"sse2_enable"*)

These implementations are slightly inaccurate compared to the pure C
version due to numerical issues.
For example, using SSE2 instructions the inaccuracy is in order of magnitude
of 1.0e-5 for 'byte' images and *`component`* set to *"none"*,
*"x"*, or *"y"*.

In case accuracy is preferred over performance, set all corresponding system
parameter to *"false"* (using [`SetSystem`](set_system.md)) before calling
`DerivateGauss`.
This way `DerivateGauss` does not use the accelerations.
Do not forget to set the parameter back to *"true"* afterwards.

`DerivateGauss` is only executed on an OpenCL
device if *`sigma`* induces a filter width respectively height of
up to 129 pixels. This corresponds to a *`sigma`* of less than 20.7
for *`component`* = *"none"*.
The OpenCL implementation is slightly inaccurate compared to the pure C
version due to numerical issues.

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / direction* / cyclic* / int1* / int2* / uint2* / int4* / real*) **allowed for compute devices*

Input images.

**`derivGauss`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (real)

Filtered result images.

**`sigma`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Sigma of the Gaussian.

Default:
1.0

Suggested values:
0.7, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0

Value range:
`0.01
≤
sigma
≤
50.0`

Minimum increment:
0.01

Recommended increment:
0.1

**`component`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Derivative or feature to be calculated.

Default:
"x"

List of values:
"2nd_ddg", "area", "de_saint_venant", "det", "eigenvalue1", "eigenvalue2", "eigenvec_dir", "gauss_curvature", "gradient", "gradient_dir", "kitchen_rosenfeld", "laplace", "main1_curvature", "main2_curvature", "mean_curvature", "none", "x", "xx", "xxx", "xxy", "xy", "xyy", "y", "yy", "yyy", "zuniga_haralick"

List of values (for compute devices):
"none", "x", "y", "gradient", "gradient_dir", "xx", "yy", "xy", "xxx", "yyy", "xxy", "xyy", "laplace"

## Example (C)

```
read_image(&Image,"mreut");
derivate_gauss(Image,&Gauss,3.0,"x");
zero_crossing(Gauss,&ZeroCrossings);
```

## Possible Successors

`ZeroCrossing`,
`DualThreshold`

## Alternatives

`Laplace`,
`LaplaceOfGauss`,
`BinomialFilter`,
`GaussFilter`,
`SmoothImage`,
`IsotropicDiffusion`

## See also

`ZeroCrossing`,
`DualThreshold`

## Module

Foundation
