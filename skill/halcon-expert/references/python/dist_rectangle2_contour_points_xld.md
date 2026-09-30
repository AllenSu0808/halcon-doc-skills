# dist_rectangle2_contour_points_xld (Operator)

## Name

`dist_rectangle2_contour_points_xld` — Compute the distances of all contour points to a rectangle.

## Signature

`def dist_rectangle2_contour_points_xld(contour: HObject, clipping_end_points: int, row: float, column: float, phi: float, length_1: float, length_2: float) -> Sequence[float]`

## Description

`dist_rectangle2_contour_points_xld` determines the Euclidean
distances between the points of a contour *`contour`* and a
rectangle of arbitrary orientation specified by the center
(*`row`*, *`column`*), the orientation *`phi`*, and
the half edge lengths *`length_1`* and *`length_2`*. The
angle *`phi`* must be given in radians and specifies the angle
between the horizontal axis and the edge with the half length
*`length_1`* in the mathematically positive direction
(counterclockwise).

Depending on the processing used to create *`contour`*, the
start and end points of a contour may contain positional errors. In
this case, the operator [`fit_rectangle2_contour_xld`](fit_rectangle2_contour_xld.md) is
typically called with the parameter *`clipping_end_points`* set
to a value greater than zero to exclude points at the beginning and
the end of the contour from the computation. To compute the
distances of the same set of points as used in the fitting process,
*`clipping_end_points`* should be set to the same value as in
[`fit_rectangle2_contour_xld`](fit_rectangle2_contour_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont `→` HObject

Input contour.

**`clipping_end_points`** (input_control)  integer `→` int

Number of points at the beginning and the end of the
contours to be ignored for the computation of
distances.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Restriction:
`ClippingEndPoints >= 0`

**`row`** (input_control)  rectangle2.center.y `→` float

Row coordinate of the center of the rectangle.

**`column`** (input_control)  rectangle2.center.x `→` float

Column coordinate of the center of the rectangle.

**`phi`** (input_control)  rectangle2.angle.rad `→` float

Orientation of the main axis of the rectangle [rad].

**`length_1`** (input_control)  rectangle2.hwidth `→` float

First radius (half length) of the rectangle.

Restriction:
`Length1 > 0`

**`length_2`** (input_control)  rectangle2.hheight `→` float

Second radius (half width) of the rectangle.

Restriction:
`Length2 >= 0`

**`distances`** (output_control)  real-array `→` Sequence[float]

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
