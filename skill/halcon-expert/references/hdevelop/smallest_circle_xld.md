# smallest_circle_xld (Operator)

## Name

`smallest_circle_xld` — Smallest enclosing circle of contours or polygons.

## Signature

`smallest_circle_xld(XLD : : : Row, Column, Radius)`

## Description

The operator `smallest_circle_xld` determines the smallest
enclosing circle of contours or polygons, i.e., the circle with the smallest
area of all circles containing the contour. For this circle the center
(*`Row`*,*`Column`*) and the radius (*`Radius`*)
are calculated.

If several contours or polygons are passed in *`XLD`* corresponding
tuples are returned as output parameter.
In case of empty contours all parameters have the value 0.0 if no other
behavior was set (see [`set_system`](set_system.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` object

Contours or polygons to be examined.

**`Row`** (output_control)  circle.center.y(-array) `→`  (real)

Row coordinate of the center of the enclosing
circle.

**`Column`** (output_control)  circle.center.x(-array) `→`  (real)

Column coordinate of the center of the enclosing
circle.

**`Radius`** (output_control)  circle.radius(-array) `→`  (real)

Radius of the enclosing circle.

Assertion:
`Radius >= 0`

## Complexity

If N is the number of contour points then the runtime complexity is
O(N*ln(N)).

## Result

The operator `smallest_circle_xld` returns the value 2 (
H_MSG_TRUE)
if the input is not empty. If the input is empty the behavior can be
set via `set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`edges_sub_pix`,
`threshold_sub_pix`,
`gen_contour_polygon_xld`

## Possible Successors

`gen_ellipse_contour_xld`

## Alternatives

`smallest_rectangle1_xld`,
`smallest_rectangle2_xld`

## See also

`elliptic_axis_xld`,
`smallest_rectangle1_xld`,
`smallest_rectangle2_xld`,
`shape_trans_xld`

## Module

Foundation
