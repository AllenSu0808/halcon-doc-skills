# critical_points_sub_pix (Operator)

## Name

`critical_points_sub_pix` — Subpixel precise detection of critical points in an image.

## Signature

`def critical_points_sub_pix(image: HObject, filter: str, sigma: float, threshold: float) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

## Description

`critical_points_sub_pix` extracts critical points, i.e., local
maxima, local minima, and saddle points, from the image *`image`* with
subpixel precision.
To do so, in each point the input image is approximated by a quadratic
polynomial in x and y and subsequently the polynomial is examined for
extremal values and saddle points. The partial derivatives, which are
necessary for setting up the polynomial, are calculated either with various
Gaussian derivatives or using the facet model, depending on *`filter`*.
In the first case, *`sigma`* determines the size of the Gaussian
kernels, while in the second case, before being processed the input image is
smoothed by a Gaussian whose size is determined by *`sigma`*.
Therefore, *"facet"* results in a faster extraction at the expense
of slightly less accurate results. A point
is accepted to be a critical point if the absolute values of both
eigenvalues of the Hessian matrix are greater than *`threshold`*. The
eigenvalues correspond to the curvature of the gray
value surface. If both eigenvalues are negative, the point is a local
maximum, if both are positive, a local minimum, and if they have different
signs, a saddle point.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  singlechannelimage `→` HObject (byte / int1 / int2 / uint2 / int4 / real)

Input image.

**`filter`** (input_control)  string `→` str

Method for the calculation of the partial derivatives.

Default:
"facet"

List of values:
"facet", "gauss"

**`sigma`** (input_control)  real `→` float

Sigma of the Gaussian.
If *`filter`* is 'facet', *`sigma`* may be 0.0
to avoid the smoothing of the input image.

Suggested values:
0.7, 0.8, 0.9, 1.0, 1.2, 1.5, 2.0, 3.0

Restriction:
`Sigma >= 0.0`

**`threshold`** (input_control)  real `→` float

Minimum absolute value of the eigenvalues of the
Hessian matrix.

Default:
5.0

Suggested values:
2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0

Restriction:
`Threshold >= 0.0`

**`row_min`** (output_control)  point.y-array `→` Sequence[float]

Row coordinates of the detected minima.

**`column_min`** (output_control)  point.x-array `→` Sequence[float]

Column coordinates of the detected minima.

**`row_max`** (output_control)  point.y-array `→` Sequence[float]

Row coordinates of the detected maxima.

**`column_max`** (output_control)  point.x-array `→` Sequence[float]

Column coordinates of the detected maxima.

**`row_saddle`** (output_control)  point.y-array `→` Sequence[float]

Row coordinates of the detected saddle points.

**`column_saddle`** (output_control)  point.x-array `→` Sequence[float]

Column coordinates of the detected saddle points.

## Result

`critical_points_sub_pix` returns 2 (
H_MSG_TRUE)
if all parameters are
correct and no error occurs during the execution. If the input is
empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Successors

`gen_cross_contour_xld`,
`disp_cross`

## Alternatives

`local_min_sub_pix`,
`local_max_sub_pix`,
`saddle_points_sub_pix`

## See also

`local_min`,
`local_max`,
`plateaus`,
`plateaus_center`,
`lowlands`,
`lowlands_center`

## Module

Foundation
