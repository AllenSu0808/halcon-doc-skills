# SplitSkeletonRegion (Operator)

## Name

`SplitSkeletonRegion` — Split lines represented by one pixel wide, non-branching regions.

## Signature

`static void HOperatorSet.SplitSkeletonRegion(HObject skeletonRegion, out HObject regionLines, HTuple maxDistance)`

`HRegion HRegion.SplitSkeletonRegion(int maxDistance)`

## Description

`SplitSkeletonRegion` splits lines represented by one pixel
wide, non-branching regions into shorter lines based on their
curvature. A line is split if the maximum distance of a point on
the line to the line segment connecting its end points is larger
than *`maxDistance`* (split & merge algorithm). However,
not the approximating lines are returned, but rather the original
lines split into several output regions.

## Attention

The input regions must represent non-branching lines, that is single
branches of the skeleton.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`skeletonRegion`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Input lines (represented by 1 pixel wide, non-branching
regions).

**`regionLines`** (output_object)  region-array `→` [HRegion](HRegion.md)

Split lines.

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
split_skeleton_region (SelectedBranches, Lines, 3)
```

## Result

`SplitSkeletonRegion` always returns the value 2 (
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

`CountObj`,
`SelectShape`,
`SelectObj`,
`AreaCenter`,
`EllipticAxis`,
`SmallestRectangle2`,
`GetRegionPolygon`,
`GetRegionContour`

## See also

`SplitSkeletonLines`,
`GetRegionPolygon`,
`GenPolygonsXld`

## Module

Foundation
