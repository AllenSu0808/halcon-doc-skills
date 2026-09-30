# split_skeleton_lines (Operator)

## Name

`split_skeleton_lines` — Split lines represented by one pixel wide, non-branching lines.

## Signature

`def split_skeleton_lines(skeleton_region: HObject, max_distance: int) -> Tuple[Sequence[int], Sequence[int], Sequence[int], Sequence[int]]`

## Description

`split_skeleton_lines` splits lines represented by one pixel
wide, non-branching regions into shorter lines based on their
curvature. A line is split if the maximum distance of a point on
the line to the line segment connecting its end points is larger
than *`max_distance`* (split & merge algorithm). The start
and end points of the approximating line segments are returned in
*`begin_row`*, *`begin_col`*, *`end_row`*, and
*`end_col`*.

## Attention

The input regions must represent non-branching lines, that is single
branches of the skeleton.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`skeleton_region`** (input_object)  region-array `→` HObject

Input lines (represented by 1 pixel wide, non-branching
regions).

**`max_distance`** (input_control)  integer `→` int

Maximum distance of the line points to the line segment
connecting both end points.

Default:
3

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Value range:
`1
≤
max_distance
≤
500` (lin)

Minimum increment:
1

Recommended increment:
1

**`begin_row`** (output_control)  line.begin.y-array `→` Sequence[int]

Row coordinates of the start points of the
output lines.

**`begin_col`** (output_control)  line.begin.x-array `→` Sequence[int]

Column coordinates of the start points of the
output lines.

**`end_row`** (output_control)  line.end.y-array `→` Sequence[int]

Row coordinates of the end points of the
output lines.

**`end_col`** (output_control)  line.end.x-array `→` Sequence[int]

Column coordinates of the end points of the
output lines.

## Result

`split_skeleton_lines` always returns the value 2 (
H_MSG_TRUE)
. The
behavior in case of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`,
the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`,
and the behavior in case of an empty result region via
`set_system('store_empty_region',<'true'/'false'>)`.
If necessary, an exception is raised.

## Possible Predecessors

`connection`,
`select_shape`,
`skeleton`,
`junctions_skeleton`,
`difference`

## Possible Successors

`select_lines`,
`partition_lines`,
`disp_line`

## See also

`split_skeleton_region`,
`detect_edge_segments`

## Module

Foundation
