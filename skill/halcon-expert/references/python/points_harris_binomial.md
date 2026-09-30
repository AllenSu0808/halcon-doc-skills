# points_harris_binomial (Operator)

## Name

`points_harris_binomial` — Detect points of interest using the binomial approximation of the Harris
operator.

## Signature

`def points_harris_binomial(image: HObject, mask_size_grad: int, mask_size_smooth: int, alpha: float, threshold: Union[float, int], subpix: str) -> Tuple[Sequence[float], Sequence[float]]`

## Description

[`points_harris`](points_harris.md) extracts points of interest from an image
*`image`*. The Harris operator is based upon the smoothed matrix
$$M = G_{\sigma} *\left(\begin{matrix} I_x^2 & I_x I_y \\ I_x I_y & I_y^2 \end{matrix}\right) ,$$ ![figure](../assets/63b840ee92d1c698.svg)
where $G_{\sigma}$ stands for a Binomial smoothing of size
*`mask_size_smooth`* and $I_{x}$ and $I_{y}$ are
the first derivatives of the image, computed with a Sobel
filter of size *`mask_size_grad`*. The resulting points are the
positive local extrema of
$$\mathrm{Det}M-\texttt{Alpha}\ast(\mathrm{Trace}M)^{2}.$$
If necessary, they can be restricted to points with a minimum filter
response of *`threshold`*. By default the coordinates of the points
are calculated with subpixel accuracy. This can be turned off by setting
the parameter *`subpix`* to 'off'.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` HObject (byte / uint2)

Input image.

**`mask_size_grad`** (input_control)  integer `→` int

Amount of binomial smoothing used for the calculation
of the gradient.

Default:
5

Suggested values:
3, 5, 7, 9, 11, 15, 21, 31

Value range:
`1
≤
mask_size_grad`

Recommended increment:
2

**`mask_size_smooth`** (input_control)  integer `→` int

Amount of smoothing used for the integration of the
gradients.

Default:
15

Suggested values:
3, 5, 7, 9, 11, 15, 21, 31

Value range:
`1
≤
mask_size_smooth`

Recommended increment:
2

**`alpha`** (input_control)  real `→` float

Weight of the squared trace of the squared gradient
matrix.

Default:
0.08

Suggested values:
0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08

Value range:
`0.0
≤
alpha`

Minimum increment:
0.001

Recommended increment:
0.01

**`threshold`** (input_control)  number `→` Union[float, int]

Minimum filter response for the points.

Default:
1000.0

Value range:
`0.0
≤
threshold`

**`subpix`** (input_control)  string `→` str

Turn on or off subpixel refinement.

Default:
"on"

List of values:
"off", "on"

**`row`** (output_control)  point.y-array `→` Sequence[float]

Row coordinates of the detected points.

**`column`** (output_control)  point.x-array `→` Sequence[float]

Column coordinates of the detected points.

## Result

[`points_harris`](points_harris.md) returns 2 (
H_MSG_TRUE)
if all parameters are correct
and no error occurs during the execution. If the input is empty the
behavior can be set via
`set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Successors

`gen_cross_contour_xld`

## Alternatives

`points_foerstner`,
`points_harris`,
`points_lepetit`,
`points_sojka`

## References

C. Harris, M. Stephens: “A combined corner and edge
detector”. Proceedings of the 4th Alvey Vision Conference,
pp. 147-151, 1988.
  
V. Gouet, N.Boujemaa: “Object-based queries using color points of
interest”. IEEE Workshop on Content-Based Access of Image and Video
Libraries, CVPR/CBAIVL 2001, Hawaii, USA, 2001.

## Module

Foundation
