# dist_ellipse_contour_points_xld (Operator)

## Name

`dist_ellipse_contour_points_xld` — Compute the distances of all contour points to an ellipse.

## Signature

`dist_ellipse_contour_points_xld(Contour : : DistanceMode, ClippingEndPoints, Row, Column, Phi, Radius1, Radius2 : Distances)`

## Description

The operator `dist_ellipse_contour_points_xld` determines the
distances between points of a contour *`Contour`* and an ellipse
specified by the center (*`Row`*, *`Column`*), the
orientation of the main axis *`Phi`*,
the length of the larger half axis *`Radius1`*, and the
length of the smaller half axis *`Radius2`*.

The distance measure is the geometric distance, sometimes also called
orthogonal distance. The distances *`Distances`* are returned for
all points of the contour.
Normally, the distance is a positive value. In this case
*`DistanceMode`* equal to *'unsigned'* must be chosen.
If this option is switched to *'signed'* the distances can take
positive or negative sign, depending on whether the contour points lie
outside or inside the ellipse respectively.

Because of artifacts in the preprocessing, the start and end points
of a contour might be faulty. In this case, the operator
[`fit_ellipse_contour_xld`](fit_ellipse_contour_xld.md) is typically called with the parameter
*`ClippingEndPoints`* set to a value greater than zero to exclude
points at the beginning and the end of the contour from the computation.
In order to get the geometric distances of the same set of points as used
in the fitting process *`ClippingEndPoints`* should take
the same value.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contour`** (input_object)  xld_cont `→` object

Input contours.

**`DistanceMode`** (input_control)  string `→`  (string)

Mode for unsigned or signed distance values.

Default:
'unsigned'

List of values:
'signed', 'unsigned'

**`ClippingEndPoints`** (input_control)  integer `→`  (integer)

Number of points at the beginning and the end of the
contours to be ignored for the computation of
distances.

Default:
0

Restriction:
`ClippingEndPoints >= 0`

**`Row`** (input_control)  ellipse.center.y `→`  (real)

Row coordinate of the center of the ellipse.

**`Column`** (input_control)  ellipse.center.x `→`  (real)

Column coordinate of the center of the ellipse.

**`Phi`** (input_control)  ellipse.angle.rad `→`  (real)

Orientation of the main axis in radian.

Restriction:
`Phi >= 0 && Phi <= 6.283185307`

**`Radius1`** (input_control)  ellipse.radius1 `→`  (real)

Length of the larger half axis.

Restriction:
`Radius1 > 0`

**`Radius2`** (input_control)  ellipse.radius2 `→`  (real)

Length of the smaller half axis.

Restriction:
`Radius2 >= 0 && Radius2 <= Radius1`

**`Distances`** (output_control)  real-array `→`  (real)

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
