# diameter_xld (Operator)

## Name

`diameter_xld` — Maximum distance between two contour or polygon points.

## Signature

`def diameter_xld(xld: HObject) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

`def diameter_xld_s(xld: HObject) -> Tuple[float, float, float, float, float]`

## Description

The operator `diameter_xld` calculates the
maximum distance between two points of each input contour or polygon.
The coordinates of these two extremes
and the distance between them will be returned. The input contour or polygon
must not intersect itself, otherwise the resulting parameters are not
meaningful (Whether the input contour or polygon intersects itself or not
can be determined with [`test_self_intersection_xld`](test_self_intersection_xld.md)). If
the input contour or polygon is not closed it will be closed automatically.
If more than one contour or polygon is passed, the results are stored
in tuples in the same order as the respective contours or polygons in
*`xld`*.

## Attention

If the contour or polygon is empty, the results of *`row_1`*,
*`column_1`*, *`row_2`* and *`column_2`* (all of them = 0) may
lead to confusion.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`xld`** (input_object)  xld(-array) `→` HObject

Contours or polygons to be examined.

**`row_1`** (output_control)  line.begin.y(-array) `→` Sequence[float]

Row coordinate of the first extreme point of the
contours or polygons.

**`column_1`** (output_control)  line.begin.x(-array) `→` Sequence[float]

Column coordinate of the first extreme point of the
contours or polygons.

**`row_2`** (output_control)  line.end.y(-array) `→` Sequence[float]

Row coordinate of the second extreme point of the
contour or polygons.

**`column_2`** (output_control)  line.end.x(-array) `→` Sequence[float]

Column coordinate of the second extreme point of the
contours or polygons.

**`diameter`** (output_control)  number(-array) `→` Sequence[float]

Distance of the two extreme points of the contours or
polygons.

## Result

The operator `diameter_xld` returns the value 2 (
H_MSG_TRUE)
, if the input
is not empty. The reaction to empty input (no input contours are
available) may be determined with the help of the operator
`set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`edges_sub_pix`,
`threshold_sub_pix`,
`gen_contour_polygon_xld`,
`test_self_intersection_xld`

## Alternatives

`smallest_rectangle2_xld`

## See also

`area_center_xld`

## Module

Foundation
