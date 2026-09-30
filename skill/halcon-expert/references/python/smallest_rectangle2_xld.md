# smallest_rectangle2_xld (Operator)

## Name

`smallest_rectangle2_xld` — Smallest enclosing rectangle with arbitrary orientation of contours or
polygons.

## Signature

`def smallest_rectangle2_xld(xld: HObject) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

`def smallest_rectangle2_xld_s(xld: HObject) -> Tuple[float, float, float, float, float]`

## Description

The operator `smallest_rectangle2_xld` determines the smallest
enclosing rectangle of each input contour or polygon, i.e., the rectangle
with the smallest area of all rectangles containing the contour. For this
rectangle the center, the inclination, and the two radii are calculated.

If more than one contour or polygon is passed, the results are stored
in tuples in the same order as the respective contours or polygons in
*`xld`*. In case of an empty contour all parameters
have the value 0.0 if no other behavior was set (see [`set_system`](set_system.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`xld`** (input_object)  xld(-array) `→` HObject

Contours or polygons to be examined.

**`row`** (output_control)  rectangle2.center.y(-array) `→` Sequence[float]

Row coordinate of the center point of the enclosing
rectangle.

**`column`** (output_control)  rectangle2.center.x(-array) `→` Sequence[float]

Column coordinate of the center point of the
enclosing rectangle.

**`phi`** (output_control)  rectangle2.angle.rad(-array) `→` Sequence[float]

Orientation of the enclosing rectangle
(arc measure)

Assertion:
`- pi / 2 < Phi && Phi <= pi / 2`

**`length_1`** (output_control)  rectangle2.hwidth(-array) `→` Sequence[float]

First radius (half length) of the enclosing
rectangle.

Assertion:
`Length1 >= 0.0`

**`length_2`** (output_control)  rectangle2.hheight(-array) `→` Sequence[float]

Second radius (half width) of the enclosing
rectangle.

Assertion:
`Length2 >= 0.0 && Length2 <= Length1`

## Complexity

If N is the number of contour points and C is the number of points
in the convex hull, the runtime complexity is O(N*ln(N)+C^2).

## Result

`smallest_rectangle2_xld` returns 2 (
H_MSG_TRUE)
if the input is not empty.
If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`edges_sub_pix`,
`threshold_sub_pix`,
`gen_contour_polygon_xld`

## Possible Successors

`gen_polygons_xld`

## Alternatives

`smallest_rectangle1`,
`shape_trans_xld`

## See also

`smallest_rectangle1`,
`smallest_circle`,
`elliptic_axis_xld`

## Module

Foundation
