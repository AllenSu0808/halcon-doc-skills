# area_center_xld (Operator)

## Name

`area_center_xld` — Area and center of gravity (centroid) of contours and polygons.

## Signature

`area_center_xld(XLD : : : Area, Row, Column, PointOrder)`

## Description

`area_center_xld` calculates the area and center of gravity
(centroid) of the regions enclosed by the contours or polygons
*`XLD`* as well as the order of the points along the
boundary. The area and centroid are computed by applying Green's
theorem using only the points on the contour or polygon, i.e., no
region is generated explicitly for the purpose of calculating the
features. If the points are arranged counterclockwise (i.e., in a
positive mathematical sense) in the contour or polygon, *`PointOrder`*
will be *'positive'*. It is assumed that the contours or
polygons are closed. If this is not the case
`area_center_xld` will artificially close the contour respectively
polygon.

It should be noted that `area_center_xld` only returns useful
results if the contour or polygon encloses a region in the plane. In
particular, the contour or polygon must not intersect itself. This
is particularly important if open contours or polygons are passed
because they are closed automatically, which can produce a
self-intersection. To test whether the contours or polygons
intersect themselves, [`test_self_intersection_xld`](test_self_intersection_xld.md) can be
used. If the contour or polygon intersects itself, a useful value
for the center of gravity can be calculated with
[`area_center_points_xld`](area_center_points_xld.md).

If more than one contour or polygon is passed, the results are stored
in tuples in the same order as the respective contours or polygons in
*`XLD`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` object

Contours or polygons to be examined.

**`Area`** (output_control)  real(-array) `→`  (real)

Area enclosed by the contour or polygon.

**`Row`** (output_control)  point.y(-array) `→`  (real)

Row coordinate of the centroid.

**`Column`** (output_control)  point.x(-array) `→`  (real)

Column coordinate of the centroid.

**`PointOrder`** (output_control)  string(-array) `→`  (string)

point order along the boundary
('positive'/'negative').

## Complexity

Let n be the number of points of the contour or polygon.
Then the run time is O(n).

## Result

`area_center_xld` returns 2 (
H_MSG_TRUE)
if the input is not empty.
If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`smooth_contours_xld`,
`gen_polygons_xld`

## Alternatives

`area_center_points_xld`

## See also

`moments_xld`,
`moments_any_xld`,
`area_center`,
`moments_region_2nd`

## Module

Foundation
