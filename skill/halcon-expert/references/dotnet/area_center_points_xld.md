# AreaCenterPointsXld (Operator)

## Name

`AreaCenterPointsXld` — Area and center of gravity (centroid) of contours and polygons
treated as point clouds.

## Signature

`static void HOperatorSet.AreaCenterPointsXld(HObject XLD, out HTuple area, out HTuple row, out HTuple column)`

`HTuple HXLD.AreaCenterPointsXld(out HTuple row, out HTuple column)`

`double HXLD.AreaCenterPointsXld(out double row, out double column)`

## Description

`AreaCenterPointsXld` calculates the area and center of
gravity (centroid) of the point clouds given by contours or polygons
*`XLD`* (i.e., the order of the points in the contour or
polygon is not taken into account). The area corresponds to the
number of points in the point cloud. The centroid is given by the
arithmetic mean of all points. If the contour or polygon is closed
(end point = start point), the end point of the contour or polygon is
not taken into account to avoid that it receives twice the weight of
the other points.

`AreaCenterPointsXld` should be used if the contour *`XLD`*
intersects itself or if it is not possible to close the contour using a line
from end to start point without self-intersection, because in this case
[`AreaCenterXld`](area_center_xld.md) does not produce useful results. To test whether the
contours or polygons intersect themselves,
[`TestSelfIntersectionXld`](test_self_intersection_xld.md) can be used.

If more than one contour or polygon is passed, the results are stored
in tuples in the same order as the respective contours or polygons in
*`XLD`*.

## Attention

Even if the contour or polygon *`XLD`* is not intersecting itself, the
result of `AreaCenterPointsXld` significantly differs from the
result of [`AreaCenterXld`](area_center_xld.md) as it is calculated from the point cloud
and not from the enclosed region.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` [HXLD](HXLD.md)

Point clouds to be examined in form of contours or
polygons.

**`area`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Area of the point cloud.

**`row`** (output_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the centroid.

**`column`** (output_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the centroid.

## Complexity

Let n be the number of points of the contour or polygon.
Then the run time is O(n).

## Result

`AreaCenterPointsXld` returns 2 (
H_MSG_TRUE)
if the input is not
empty. If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Predecessors

`GenContoursSkeletonXld`,
`SmoothContoursXld`,
`GenPolygonsXld`

## Alternatives

`AreaCenterXld`

## See also

`MomentsPointsXld`,
`MomentsAnyPointsXld`,
`AreaCenter`,
`MomentsRegion2nd`

## Module

Foundation
