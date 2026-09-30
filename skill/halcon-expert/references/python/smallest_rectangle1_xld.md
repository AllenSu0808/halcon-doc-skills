# smallest_rectangle1_xld (Operator)

## Name

`smallest_rectangle1_xld` — Enclosing rectangle parallel to the coordinate axes of contours or polygons.

## Signature

`def smallest_rectangle1_xld(xld: HObject) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

`def smallest_rectangle1_xld_s(xld: HObject) -> Tuple[float, float, float, float]`

## Description

The operator `smallest_rectangle1_xld` calculates the enclosing
rectangle (parallel to the coordinate axes) for each input contour or
polygon.
The enclosing rectangle is described by the coordinates of the corner
pixels (*`row_1`*,*`column_1`*,*`row_2`*,*`column_2`*)

If more than one contour or polygon is passed, the results are stored in
tuples in the same order as the respective contours or polygons in
*`xld`*. In case of an empty contour all parameters have the value 0
if no other behavior was set (see [`set_system`](set_system.md)).

## Attention

In case of empty contours the result of *`row_1`*,*`column_1`*,
*`row_2`* and *`column_2`* (all are 0) can lead to confusion.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`xld`** (input_object)  xld(-array) `→` HObject

Contours or polygons to be examined.

**`row_1`** (output_control)  rectangle.origin.y(-array) `→` Sequence[float]

Row coordinate of upper left corner point of the
enclosing rectangle.

**`column_1`** (output_control)  rectangle.origin.x(-array) `→` Sequence[float]

Column coordinate of upper left corner point of the
enclosing rectangle.

**`row_2`** (output_control)  rectangle.corner.y(-array) `→` Sequence[float]

Row coordinate of lower right corner point of the
enclosing rectangle.

**`column_2`** (output_control)  rectangle.corner.x(-array) `→` Sequence[float]

Column coordinate of lower right corner point of the
enclosing rectangle.

## Complexity

If N is the number of contour points, the runtime complexity is
O(N).

## Result

`smallest_rectangle1_xld` returns 2 (
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

`height_width_ratio_xld`,
`smallest_rectangle2_xld`,
`shape_trans_xld`

## See also

`shape_trans_xld`,
`smallest_rectangle2_xld`,
`smallest_circle_xld`,
`elliptic_axis_xld`,
`area_center_xld`

## Module

Foundation
