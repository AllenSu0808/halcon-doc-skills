# dist_ellipse_contour_points_xld (Operator)

## Name

`dist_ellipse_contour_points_xld` — Compute the distances of all contour points to an ellipse.

## Signature

`def dist_ellipse_contour_points_xld(contour: HObject, distance_mode: str, clipping_end_points: int, row: float, column: float, phi: float, radius_1: float, radius_2: float) -> Sequence[float]`

## Description

The operator `dist_ellipse_contour_points_xld` determines the
distances between points of a contour *`contour`* and an ellipse
specified by the center (*`row`*, *`column`*), the
orientation of the main axis *`phi`*,
the length of the larger half axis *`radius_1`*, and the
length of the smaller half axis *`radius_2`*.

The distance measure is the geometric distance, sometimes also called
orthogonal distance. The distances *`distances`* are returned for
all points of the contour.
Normally, the distance is a positive value. In this case
*`distance_mode`* equal to *"unsigned"* must be chosen.
If this option is switched to *"signed"* the distances can take
positive or negative sign, depending on whether the contour points lie
outside or inside the ellipse respectively.

Because of artifacts in the preprocessing, the start and end points
of a contour might be faulty. In this case, the operator
[`fit_ellipse_contour_xld`](fit_ellipse_contour_xld.md) is typically called with the parameter
*`clipping_end_points`* set to a value greater than zero to exclude
points at the beginning and the end of the contour from the computation.
In order to get the geometric distances of the same set of points as used
in the fitting process *`clipping_end_points`* should take
the same value.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont `→` HObject

Input contours.

**`distance_mode`** (input_control)  string `→` str

Mode for unsigned or signed distance values.

Default:
"unsigned"

List of values:
"signed", "unsigned"

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

**`distances`** (output_control)  real-array `→` Sequence[float]

Distances of the contour points to the ellipse.

## Result

`dist_ellipse_contour_points_xld` returns 2 (
H_MSG_TRUE)
if all parameter
values are correct. If necessary, an exception is raised.

## Possible Predecessors

`fit_ellipse_contour_xld`

## Alternatives

`dist_ellipse_contour_xld`

## Module

Foundation
