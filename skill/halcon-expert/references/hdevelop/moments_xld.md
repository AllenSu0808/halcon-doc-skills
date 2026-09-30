# moments_xld (Operator)

## Name

`moments_xld` — Geometric moments $M_{20}$, $M_{02}$, and
$M_{11}$ of contours or polygons.

## Signature

`moments_xld(XLD : : : M11, M20, M02)`

## Description

`moments_xld` calculates the moments (*`M20`*,
*`M02`*, and *`M11`*) of the region enclosed by the
contours or polygons *`XLD`*. See [`moments_region_2nd`](moments_region_2nd.md)
for the definition of these features. The moments are computed by
applying Green's theorem using only the points on the contour or
polygon, i.e., no region is generated explicitly for the purpose of
calculating the features. It is assumed that the contours or
polygons are closed. If this is not the case `moments_xld`
will artificially close the contours or polygons.

It should be noted that `moments_xld` only returns useful
results if the contour or polygon encloses a region in the plane. In
particular, the contour or polygon must not intersect itself. This
is particularly important if open contours or polygons are passed
because they are closed automatically, which can produce a
self-intersection. To test whether the contours or polygons
intersect themselves, [`test_self_intersection_xld`](test_self_intersection_xld.md) can be
used. If the contour or polygon intersects itself, useful values
for the moments can be calculated with [`moments_points_xld`](moments_points_xld.md).

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

**`M11`** (output_control)  real(-array) `→`  (real)

Mixed second order moment.

**`M20`** (output_control)  real(-array) `→`  (real)

Second order moment along the row axis.

**`M02`** (output_control)  real(-array) `→`  (real)

Second order moment along the column axis.

## Complexity

Let n be the number of points of the contour or polygon.
Then the run time is O(n).

## Result

`moments_xld` returns 2 (
H_MSG_TRUE)
if the input is not empty. If
the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`smooth_contours_xld`,
`gen_polygons_xld`

## Alternatives

`moments_any_xld`,
`moments_points_xld`,
`moments_any_points_xld`

## See also

`moments_any_xld`,
`area_center_xld`,
`moments_region_2nd`,
`area_center`

## Module

Foundation
