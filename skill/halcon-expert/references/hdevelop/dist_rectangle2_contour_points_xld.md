# dist_rectangle2_contour_points_xld (Operator)

## Name

`dist_rectangle2_contour_points_xld` — Compute the distances of all contour points to a rectangle.

## Signature

`dist_rectangle2_contour_points_xld(Contour : : ClippingEndPoints, Row, Column, Phi, Length1, Length2 : Distances)`

## Description

`dist_rectangle2_contour_points_xld` determines the Euclidean
distances between the points of a contour *`Contour`* and a
rectangle of arbitrary orientation specified by the center
(*`Row`*, *`Column`*), the orientation *`Phi`*, and
the half edge lengths *`Length1`* and *`Length2`*. The
angle *`Phi`* must be given in radians and specifies the angle
between the horizontal axis and the edge with the half length
*`Length1`* in the mathematically positive direction
(counterclockwise).

Depending on the processing used to create *`Contour`*, the
start and end points of a contour may contain positional errors. In
this case, the operator [`fit_rectangle2_contour_xld`](fit_rectangle2_contour_xld.md) is
typically called with the parameter *`ClippingEndPoints`* set
to a value greater than zero to exclude points at the beginning and
the end of the contour from the computation. To compute the
distances of the same set of points as used in the fitting process,
*`ClippingEndPoints`* should be set to the same value as in
[`fit_rectangle2_contour_xld`](fit_rectangle2_contour_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contour`** (input_object)  xld_cont `→` object

Input contour.

**`ClippingEndPoints`** (input_control)  integer `→`  (integer)

Number of points at the beginning and the end of the
contours to be ignored for the computation of
distances.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Restriction:
`ClippingEndPoints >= 0`

**`Row`** (input_control)  rectangle2.center.y `→`  (real)

Row coordinate of the center of the rectangle.

**`Column`** (input_control)  rectangle2.center.x `→`  (real)

Column coordinate of the center of the rectangle.

**`Phi`** (input_control)  rectangle2.angle.rad `→`  (real)

Orientation of the main axis of the rectangle [rad].

**`Length1`** (input_control)  rectangle2.hwidth `→`  (real)

First radius (half length) of the rectangle.

Restriction:
`Length1 > 0`

**`Length2`** (input_control)  rectangle2.hheight `→`  (real)

Second radius (half width) of the rectangle.

Restriction:
`Length2 >= 0`

**`Distances`** (output_control)  real-array `→`  (real)

Distances of the contour points to the rectangle.

## Result

`dist_rectangle2_contour_points_xld` returns 2 (
H_MSG_TRUE)
if all
parameter values are correct. If necessary, an exception is
raised.

## Possible Predecessors

`fit_rectangle2_contour_xld`

## Module

Foundation
