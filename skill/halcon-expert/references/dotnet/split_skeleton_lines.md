# SplitSkeletonLines (Operator)

## Name

`SplitSkeletonLines` — Split lines represented by one pixel wide, non-branching lines.

## Signature

`static void HOperatorSet.SplitSkeletonLines(HObject skeletonRegion, HTuple maxDistance, out HTuple beginRow, out HTuple beginCol, out HTuple endRow, out HTuple endCol)`

`void HRegion.SplitSkeletonLines(int maxDistance, out HTuple beginRow, out HTuple beginCol, out HTuple endRow, out HTuple endCol)`

## Description

`SplitSkeletonLines` splits lines represented by one pixel
wide, non-branching regions into shorter lines based on their
curvature. A line is split if the maximum distance of a point on
the line to the line segment connecting its end points is larger
than *`maxDistance`* (split & merge algorithm). The start
and end points of the approximating line segments are returned in
*`beginRow`*, *`beginCol`*, *`endRow`*, and
*`endCol`*.

## Attention

The input regions must represent non-branching lines, that is single
branches of the skeleton.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`skeletonRegion`** (input_object)  region-array `→` [HRegion](HRegion.md)

Input lines (represented by 1 pixel wide, non-branching
regions).

**`maxDistance`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum distance of the line points to the line segment
connecting both end points.

Default:
3

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Value range:
`1
≤
maxDistance
≤
500` (lin)

Minimum increment:
1

Recommended increment:
1

**`beginRow`** (output_control)  line.begin.y-array `→` [HTuple](HTuple.md) (*int* / long)

Row coordinates of the start points of the
output lines.

**`beginCol`** (output_control)  line.begin.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column coordinates of the start points of the
output lines.

**`endRow`** (output_control)  line.end.y-array `→` [HTuple](HTuple.md) (*int* / long)

Row coordinates of the end points of the
output lines.

**`endCol`** (output_control)  line.end.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column coordinates of the end points of the
output lines.

## Example (HDevelop)

```
read_image(Image,'fabrik')
edges_image (Image, ImaAmp, ImaDir, 'lanser2', 0.5, 'nms', 8, 16)
threshold (ImaAmp, RawEdges, 8, 255)
skeleton (RawEdges, Skeleton)
junctions_skeleton (Skeleton, EndPoints, JuncPoints)
difference (Skeleton, JuncPoints, SkelWithoutJunc)
connection (SkelWithoutJunc, SingleBranches)
select_shape (SingleBranches, SelectedBranches, 'area', 'and', 16, 99999)
split_skeleton_lines (SelectedBranches, 3, BeginRow, BeginCol, EndRow, \
                      EndCol)
```

## Result

`SplitSkeletonLines` always returns the value 2 (
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

`Connection`,
`SelectShape`,
`Skeleton`,
`JunctionsSkeleton`,
`Difference`

## Possible Successors

`SelectLines`,
`PartitionLines`,
`DispLine`

## See also

`SplitSkeletonRegion`,
`DetectEdgeSegments`

## Module

Foundation
