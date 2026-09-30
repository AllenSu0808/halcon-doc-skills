# local_max_sub_pix (Operator)

## Name

`local_max_sub_pix` — Subpixel precise detection of local maxima in an image.

## Signature

`local_max_sub_pix(Image : : Filter, Sigma, Threshold : Row, Column)`

## Description

`local_max_sub_pix` extracts local maxima from the image
*`Image`* with subpixel precision.
To do so, in each point the input image is approximated by a quadratic
polynomial in x and y and subsequently the polynomial is examined for
local maxima. The partial derivatives, which are
necessary for setting up the polynomial, are calculated either with various
Gaussian derivatives or using the facet model, depending on *`Filter`*.
In the first case, *`Sigma`* determines the size of the Gaussian
kernels, while in the second case, before being processed the input image is
smoothed by a Gaussian whose size is determined by *`Sigma`*.
Therefore, *'facet'* results in a faster extraction at the expense
of slightly less accurate results. A point is accepted to be a local maximum
if both eigenvalues of the Hessian matrix are smaller than
-*`Threshold`*. The eigenvalues correspond to the curvature of the gray
value surface.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte / int1 / int2 / uint2 / int4 / real)

Input image.

**`Filter`** (input_control)  string `→`  (string)

Method for the calculation of the partial derivatives.

Default:
'facet'

List of values:
'facet', 'gauss'

**`Sigma`** (input_control)  real `→`  (real)

Sigma of the Gaussian.
If *`Filter`* is 'facet', *`Sigma`* may be 0.0
to avoid the smoothing of the input image.

Suggested values:
0.7, 0.8, 0.9, 1.0, 1.2, 1.5, 2.0, 3.0

Restriction:
`Sigma >= 0.0`

**`Threshold`** (input_control)  real `→`  (real)

Minimum absolute value of the eigenvalues of the
Hessian matrix.

Default:
5.0

Suggested values:
2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0

Restriction:
`Threshold >= 0.0`

**`Row`** (output_control)  point.y-array `→`  (real)

Row coordinates of the detected maxima.

**`Column`** (output_control)  point.x-array `→`  (real)

Column coordinates of the detected maxima.

## Result

`local_max_sub_pix` returns 2 (
H_MSG_TRUE)
if all parameters are correct
and no error occurs during the execution. If the input is empty the
behavior can be set via
`set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Successors

`gen_cross_contour_xld`,
`disp_cross`

## Alternatives

`critical_points_sub_pix`,
`local_min_sub_pix`,
`saddle_points_sub_pix`

## See also

`local_max`,
`plateaus`,
`plateaus_center`

## Module

Foundation
