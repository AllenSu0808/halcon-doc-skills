# MomentsPointsXld (Operator)

## Name

`MomentsPointsXld` — Geometric moments $M_{20}$, $M_{02}$, and $M_{11}$
of contours or polygons treated as point clouds.

## Signature

`static void HOperatorSet.MomentsPointsXld(HObject XLD, out HTuple m11, out HTuple m20, out HTuple m02)`

`HTuple HXLD.MomentsPointsXld(out HTuple m20, out HTuple m02)`

`double HXLD.MomentsPointsXld(out double m20, out double m02)`

## Description

`MomentsPointsXld` calculates the moments (*`m20`*,
*`m02`*, and *`m11`*) of a point cloud given by a contour or a
polygon *`XLD`* (i.e., the order of the points in the contour or
polygon is not taken into account). Therefore, the moments are given by
$$M_{p,q} = \sum_{i=0}^{n-1} (r_i - \bar{r})^{p} (c_i - \bar{c})^{q}.$$ ![figure](../assets/9d2b6c5f9f138767.svg).
Here, $\left(\bar{r},\bar{c}\right)$ ![figure](../assets/d5d96a8beaaa1bdf.svg) is the centroid and
n the number of points.

If the contour or polygon is closed
(end point = start point), the end point of the contour or polygon is
not taken into account to avoid that it receives twice the weight of
the other points.

`MomentsPointsXld` should be used if the contour *`XLD`*
intersects itself or if it is not possible to close the contour using a line
from end to start point without self-intersection, because in this case
[`MomentsXld`](moments_xld.md) does not produce useful results. To test whether the
contours or polygons intersect themselves,
[`TestSelfIntersectionXld`](test_self_intersection_xld.md) can be used.

If more than one contour or polygon is passed, the results are stored
in tuples in the same order as the respective contours or polygons in
*`XLD`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` [HXLD](HXLD.md)

Contours or polygons to be examined.

**`m11`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Mixed second order moment.

**`m20`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Second order moment along the row axis.

**`m02`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Second order moment along the column axis.

## Complexity

Let n be the number of points of the contour or polygon.
Then the run time is O(n).

## Result

`MomentsPointsXld` returns 2 (
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

`MomentsXld`,
`MomentsAnyXld`,
`MomentsAnyPointsXld`

## See also

`MomentsAnyPointsXld`,
`AreaCenterPointsXld`,
`MomentsRegion2nd`,
`AreaCenter`

## Module

Foundation
