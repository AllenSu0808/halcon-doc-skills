# OrientationPointsXld (Operator)

## Name

`OrientationPointsXld` — Calculate the orientation of contours or polygons treated as point clouds.

## Signature

`static void HOperatorSet.OrientationPointsXld(HObject XLD, out HTuple phi)`

`HTuple HXLD.OrientationPointsXld()`

## Description

The operator `OrientationPointsXld` calculates the
orientation *`phi`* of the point clouds given by the contours or
polygons *`XLD`* (the order of the points in the contour or
polygon is not taken into account). The orientation *`phi`* is calculated
the same way as in [`EllipticAxisPointsXld`](elliptic_axis_points_xld.md). If the contour or
polygon is closed (end point = start point), the end point of the contour or
polygon is not taken into account to avoid that it receives twice
the weight of the other points.

In addition, the contour point $p_{m}$ with maximum distance to the
center of gravity $c$ is calculated. If the angle between the
vector $\overline{p}_m c$ ![figure](../assets/852e3ee056332c0b.svg) and the vector given by
*`phi`* is
greater than $\pi$, the value of $\pi$ is added
to the angle. If *`XLD`* consists of only two points,
*`phi`* is given by the direction from the first point towards
the second point.

`OrientationPointsXld` should be used if the contour *`XLD`*
intersects itself or if it is not possible to close the contour using a line
from end to start point without self-intersection, because in this case
[`OrientationXld`](orientation_xld.md) does not produce useful results. To test whether the
contours or polygons intersect themselves,
[`TestSelfIntersectionXld`](test_self_intersection_xld.md) can be used.

If more than one contour or polygon is passed, the values of the
orientations are stored in a tuple in the same order as the respective
contours or polygons in *`XLD`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` [HXLD](HXLD.md)

Contours or polygons to be examined.

**`phi`** (output_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Orientation of the contours or polygons (radians).

Assertion:
`- pi < Phi && Phi <= pi`

## Possible Predecessors

`GenContoursSkeletonXld`,
`EdgesSubPix`,
`ThresholdSubPix`,
`GenContourPolygonXld`

## Alternatives

`OrientationXld`,
`EllipticAxisPointsXld`,
`SmallestRectangle2Xld`

## See also

`MomentsRegion2nd`

## Module

Foundation
