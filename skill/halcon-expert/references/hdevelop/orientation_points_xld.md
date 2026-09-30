# orientation_points_xld (Operator)

## Name

`orientation_points_xld` — Calculate the orientation of contours or polygons treated as point clouds.

## Signature

`orientation_points_xld(XLD : : : Phi)`

## Description

The operator `orientation_points_xld` calculates the
orientation *`Phi`* of the point clouds given by the contours or
polygons *`XLD`* (the order of the points in the contour or
polygon is not taken into account). The orientation *`Phi`* is calculated
the same way as in [`elliptic_axis_points_xld`](elliptic_axis_points_xld.md). If the contour or
polygon is closed (end point = start point), the end point of the contour or
polygon is not taken into account to avoid that it receives twice
the weight of the other points.

In addition, the contour point $p_{m}$ with maximum distance to the
center of gravity $c$ is calculated. If the angle between the
vector $\overline{p}_m c$ ![figure](../assets/852e3ee056332c0b.svg) and the vector given by
*`Phi`* is
greater than $\pi$, the value of $\pi$ is added
to the angle. If *`XLD`* consists of only two points,
*`Phi`* is given by the direction from the first point towards
the second point.

`orientation_points_xld` should be used if the contour *`XLD`*
intersects itself or if it is not possible to close the contour using a line
from end to start point without self-intersection, because in this case
[`orientation_xld`](orientation_xld.md) does not produce useful results. To test whether the
contours or polygons intersect themselves,
[`test_self_intersection_xld`](test_self_intersection_xld.md) can be used.

If more than one contour or polygon is passed, the values of the
orientations are stored in a tuple in the same order as the respective
contours or polygons in *`XLD`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` object

Contours or polygons to be examined.

**`Phi`** (output_control)  angle.rad(-array) `→`  (real)

Orientation of the contours or polygons (radians).

Assertion:
`- pi < Phi && Phi <= pi`

## Possible Predecessors

`gen_contours_skeleton_xld`,
`edges_sub_pix`,
`threshold_sub_pix`,
`gen_contour_polygon_xld`

## Alternatives

`orientation_xld`,
`elliptic_axis_points_xld`,
`smallest_rectangle2_xld`

## See also

`moments_region_2nd`

## Module

Foundation
