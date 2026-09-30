# split_skeleton_region (Operator)

## Name

`split_skeleton_region` — Split lines represented by one pixel wide, non-branching regions.

## Signature

`split_skeleton_region(SkeletonRegion : RegionLines : MaxDistance : )`

## Description

`split_skeleton_region` splits lines represented by one pixel
wide, non-branching regions into shorter lines based on their
curvature. A line is split if the maximum distance of a point on
the line to the line segment connecting its end points is larger
than *`MaxDistance`* (split & merge algorithm). However,
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

**`SkeletonRegion`** (input_object)  region(-array) `→` object

Input lines (represented by 1 pixel wide, non-branching
regions).

**`RegionLines`** (output_object)  region-array `→` object

Split lines.

**`MaxDistance`** (input_control)  integer `→`  (integer)

Maximum distance of the line points to the line segment
connecting both end points.

Default:
3

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Value range:
`1
≤
MaxDistance
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

`split_skeleton_region` always returns the value 2 (
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

`count_obj`,
`select_shape`,
`select_obj`,
`area_center`,
`elliptic_axis`,
`smallest_rectangle2`,
`get_region_polygon`,
`get_region_contour`

## See also

`split_skeleton_lines`,
`get_region_polygon`,
`gen_polygons_xld`

## Module

Foundation
