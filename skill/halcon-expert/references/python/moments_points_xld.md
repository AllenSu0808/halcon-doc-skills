# moments_points_xld (Operator)

## Name

`moments_points_xld` — Geometric moments $M_{20}$, $M_{02}$, and $M_{11}$
of contours or polygons treated as point clouds.

## Signature

`def moments_points_xld(xld: HObject) -> Tuple[Sequence[float], Sequence[float], Sequence[float]]`

`def moments_points_xld_s(xld: HObject) -> Tuple[float, float, float]`

## Description

`moments_points_xld` calculates the moments (*`m20`*,
*`m02`*, and *`m11`*) of a point cloud given by a contour or a
polygon *`xld`* (i.e., the order of the points in the contour or
polygon is not taken into account). Therefore, the moments are given by
$$M_{p,q} = \sum_{i=0}^{n-1} (r_i - \bar{r})^{p} (c_i - \bar{c})^{q}.$$ ![figure](../assets/9d2b6c5f9f138767.svg).
Here, $\left(\bar{r},\bar{c}\right)$ ![figure](../assets/d5d96a8beaaa1bdf.svg) is the centroid and
n the number of points.

If the contour or polygon is closed
(end point = start point), the end point of the contour or polygon is
not taken into account to avoid that it receives twice the weight of
the other points.

`moments_points_xld` should be used if the contour *`xld`*
intersects itself or if it is not possible to close the contour using a line
from end to start point without self-intersection, because in this case
[`moments_xld`](moments_xld.md) does not produce useful results. To test whether the
contours or polygons intersect themselves,
[`test_self_intersection_xld`](test_self_intersection_xld.md) can be used.

If more than one contour or polygon is passed, the results are stored
in tuples in the same order as the respective contours or polygons in
*`xld`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`xld`** (input_object)  xld(-array) `→` HObject

Contours or polygons to be examined.

**`m11`** (output_control)  real(-array) `→` Sequence[float]

Mixed second order moment.

**`m20`** (output_control)  real(-array) `→` Sequence[float]

Second order moment along the row axis.

**`m02`** (output_control)  real(-array) `→` Sequence[float]

Second order moment along the column axis.

## Complexity

Let n be the number of points of the contour or polygon.
Then the run time is O(n).

## Result

`moments_points_xld` returns 2 (
H_MSG_TRUE)
if the input is not
empty. If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`smooth_contours_xld`,
`gen_polygons_xld`

## Alternatives

`moments_xld`,
`moments_any_xld`,
`moments_any_points_xld`

## See also

`moments_any_points_xld`,
`area_center_points_xld`,
`moments_region_2nd`,
`area_center`

## Module

Foundation
