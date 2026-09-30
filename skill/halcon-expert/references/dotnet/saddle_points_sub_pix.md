# SaddlePointsSubPix (Operator)

## Name

`SaddlePointsSubPix` — Subpixel precise detection of saddle points in an image.

## Signature

`static void HOperatorSet.SaddlePointsSubPix(HObject image, HTuple filter, HTuple sigma, HTuple threshold, out HTuple row, out HTuple column)`

`void HImage.SaddlePointsSubPix(string filter, double sigma, double threshold, out HTuple row, out HTuple column)`

## Description

`SaddlePointsSubPix` extracts saddle points from the image
*`image`* with subpixel precision, i.e.,
points where along one direction the image intensity is minimal while at the
same time along a different direction the image intensity is maximal.
To do so, in each point the input image is approximated by a quadratic
polynomial in x and y and subsequently the polynomial is examined for
saddle points. The partial derivatives, which are
necessary for setting up the polynomial, are calculated either with various
Gaussian derivatives or using the facet model, depending on *`filter`*.
In the first case, *`sigma`* determines the size of the Gaussian
kernels, while in the second case, before being processed the input image is
smoothed by a Gaussian whose size is determined by *`sigma`*.
Therefore, *"facet"* results in a faster extraction at the expense
of slightly less accurate results. A point
is accepted to be a saddle point if the absolute values of both
eigenvalues of the Hessian matrix are greater than *`threshold`* but
their signs differ. The eigenvalues correspond to the curvature of the gray
value surface.

`SaddlePointsSubPix` is especially useful for the detection of
corners, where fields of different intensity join together like the black
and white fields of a chess board. Their high contrast and shape facilitate
the location and the determination of the precise position of such corners.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / int1 / int2 / uint2 / int4 / real)

Input image.

**`filter`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Method for the calculation of the partial derivatives.

Default:
"facet"

List of values:
"facet", "gauss"

**`sigma`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Sigma of the Gaussian.
If *`filter`* is 'facet', *`sigma`* may be 0.0
to avoid the smoothing of the input image.

Suggested values:
0.7, 0.8, 0.9, 1.0, 1.2, 1.5, 2.0, 3.0

Restriction:
`Sigma >= 0.0`

**`threshold`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Minimum absolute value of the eigenvalues of the
Hessian matrix.

Default:
5.0

Suggested values:
2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0

Restriction:
`Threshold >= 0.0`

**`row`** (output_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the detected saddle points.

**`column`** (output_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the detected saddle points.

## Result

`SaddlePointsSubPix` returns 2 (
H_MSG_TRUE)
if all parameters are correct
and no error occurs during the execution. If the input is empty the
behavior can be set via
`set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Successors

`GenCrossContourXld`,
`DispCross`

## Alternatives

`CriticalPointsSubPix`,
`LocalMinSubPix`,
`LocalMaxSubPix`

## Module

Foundation
