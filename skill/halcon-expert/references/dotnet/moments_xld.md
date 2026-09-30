# MomentsXld (Operator)

## Name

`MomentsXld` — Geometric moments $M_{20}$, $M_{02}$, and
$M_{11}$ of contours or polygons.

## Signature

`static void HOperatorSet.MomentsXld(HObject XLD, out HTuple m11, out HTuple m20, out HTuple m02)`

`HTuple HXLD.MomentsXld(out HTuple m20, out HTuple m02)`

`double HXLD.MomentsXld(out double m20, out double m02)`

## Description

`MomentsXld` calculates the moments (*`m20`*,
*`m02`*, and *`m11`*) of the region enclosed by the
contours or polygons *`XLD`*. See [`MomentsRegion2nd`](moments_region_2nd.md)
for the definition of these features. The moments are computed by
applying Green's theorem using only the points on the contour or
polygon, i.e., no region is generated explicitly for the purpose of
calculating the features. It is assumed that the contours or
polygons are closed. If this is not the case `MomentsXld`
will artificially close the contours or polygons.

It should be noted that `MomentsXld` only returns useful
results if the contour or polygon encloses a region in the plane. In
particular, the contour or polygon must not intersect itself. This
is particularly important if open contours or polygons are passed
because they are closed automatically, which can produce a
self-intersection. To test whether the contours or polygons
intersect themselves, [`TestSelfIntersectionXld`](test_self_intersection_xld.md) can be
used. If the contour or polygon intersects itself, useful values
for the moments can be calculated with [`MomentsPointsXld`](moments_points_xld.md).

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

`MomentsXld` returns 2 (
H_MSG_TRUE)
if the input is not empty. If
the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`GenContoursSkeletonXld`,
`SmoothContoursXld`,
`GenPolygonsXld`

## Alternatives

`MomentsAnyXld`,
`MomentsPointsXld`,
`MomentsAnyPointsXld`

## See also

`MomentsAnyXld`,
`AreaCenterXld`,
`MomentsRegion2nd`,
`AreaCenter`

## Module

Foundation
