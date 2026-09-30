# dist_ellipse_contour_xld (Operator)

## Name

`dist_ellipse_contour_xld` — Compute the distance of contours to an ellipse.

## Signature

`def dist_ellipse_contour_xld(contours: HObject, mode: str, max_num_points: int, clipping_end_points: int, row: float, column: float, phi: float, radius_1: float, radius_2: float) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

`def dist_ellipse_contour_xld_s(contours: HObject, mode: str, max_num_points: int, clipping_end_points: int, row: float, column: float, phi: float, radius_1: float, radius_2: float) -> Tuple[float, float, float, float]`

## Description

`dist_ellipse_contour_xld` determines the distance
between the contours in *`contours`* and an ellipse
specified by the center (*`row`*, *`column`*), the
orientation of the main axis *`phi`*,
the length of the larger half axis *`radius_1`*, and the
length of the smaller half axis *`radius_2`*. Different
measures for the distance of a contour point
$X=(x_{i},y_{i})$ to the ellipse are
available (*`mode`*):

- ***"geometric"*** —

  The underlying distance measure is the geometric distance between a point
  on the contour and the ellipse. This measure is also called
  orthogonal or Euclidean distance.
- ***"algebraic"*** —

  The distance is measured by the algebraic distance
  $$ax_{i}^{2}+bx_{i}y_{i}+cy_{i}^{2}+dx_{i}+ey_{i}+f$$, where the
  parameters a - f describing the ellipse are normalized in order
  to obtain *`radius_2`* as distance of the center of the
  ellipse. This measure shows a *high curvature bias*: Near points of
  high curvature on the ellipse (like the poles on the main axis)
  the distance is smaller than near points with low curvature.
- ***"focpoints"*** —

  The distance is measured by the deviation
  $XF_{1}+XF_{2}-2a$,
  where $F_{1},F_{2}$ are the focal points and a corresponds to
  *`radius_1`*. This measure shows a *low curvature bias*:
  Near points of high curvature on the ellipse (like the poles on the main
  axis) the distance is larger than near points with low curvature.
- ***"bisec"*** —

  The distance is measured by the distance between X and the
  intersection of the angular bisector of the two lines through X and the
  focal points with the ellipse. This is a good approximation of
  the orthogonal distance from X to the ellipse.
  The accuracy of the approximation depends on both the aspect ratio of the
  ellipse and the distance.

The operator returns the minimum absolute distance *`min_dist`*,
the maximum absolute distance *`max_dist`*, the average
absolute distance *`avg_dist`*, and the standard deviation of
the absolute distances *`sigma_dist`* of all contour points.

To reduce the computational load, the computation of the distances
can be restricted to a subset of the contour points: If a value other
than -1 is assigned to *`max_num_points`*, only up to
*`max_num_points`* points - uniformly distributed over the
contour - are used.
Due to artifacts in the pre-processing the start and end points
of a contour might be faulty. Therefore, it is possible to
exclude *`clipping_end_points`* points at the beginning and at
the end of a contour from the computation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont(-array) `→` HObject

Input contours.

**`mode`** (input_control)  string `→` str

Method for the determination of the distances.

Default:
"geometric"

List of values:
"algebraic", "bisec", "focpoints", "geometric"

**`max_num_points`** (input_control)  integer `→` int

Maximum number of contour points used for the
computation (-1 for all points).

Default:
-1

Restriction:
`MaxNumPoints >= 3`

**`clipping_end_points`** (input_control)  integer `→` int

Number of points at the beginning and the end of the
contours to be ignored for the computation of
distances.

Default:
0

Restriction:
`ClippingEndPoints >= 0`

**`row`** (input_control)  ellipse.center.y `→` float

Row coordinate of the center of the ellipse.

**`column`** (input_control)  ellipse.center.x `→` float

Column coordinate of the center of the ellipse.

**`phi`** (input_control)  ellipse.angle.rad `→` float

Orientation of the main axis in radian.

Restriction:
`Phi >= 0 && Phi <= 6.283185307`

**`radius_1`** (input_control)  ellipse.radius1 `→` float

Length of the larger half axis.

Restriction:
`Radius1 > 0`

**`radius_2`** (input_control)  ellipse.radius2 `→` float

Length of the smaller half axis.

Restriction:
`Radius2 >= 0 && Radius2 <= Radius1`

**`min_dist`** (output_control)  real(-array) `→` Sequence[float]

Minimum distance.

**`max_dist`** (output_control)  real(-array) `→` Sequence[float]

Maximum distance.

**`avg_dist`** (output_control)  real(-array) `→` Sequence[float]

Mean distance.

**`sigma_dist`** (output_control)  real(-array) `→` Sequence[float]

Standard deviation of the distance.

## Result

`dist_ellipse_contour_xld` returns 2 (
H_MSG_TRUE)
if all parameter
values are correct. If necessary, an exception is raised.

## Possible Predecessors

`fit_ellipse_contour_xld`

## Alternatives

`dist_ellipse_contour_points_xld`

## Module

Foundation
