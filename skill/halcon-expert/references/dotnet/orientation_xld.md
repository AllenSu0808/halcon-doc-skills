# OrientationXld (Operator)

## Name

`OrientationXld` — Calculate the orientation of contours or polygons.

## Signature

`static void HOperatorSet.OrientationXld(HObject XLD, out HTuple phi)`

`HTuple HXLD.OrientationXld()`

## Description

The operator `OrientationXld` calculates the orientation
(*`phi`*) of each input contour or polygon (*`XLD`*).
The operator is based on [`EllipticAxisXld`](elliptic_axis_xld.md).
In addition, the contour respectively polygon
point with maximum distance to the center of gravity is calculated. If the
column coordinate of this point is less than the column coordinate
of the center of gravity the value of $\pi$ is added to the
angle. It is assumed that the contours or polygons are closed. If
this is not the case `OrientationXld` will artificially close
the contours or polygons.

It should be noted that `OrientationXld` only returns useful
results if the contour or polygon encloses a region in the plane. In
particular, the contour or polygon must not intersect itself. This
is particularly important if open contours or polygons are passed
because they are closed automatically, which can produce a
self-intersection. To test whether the contours or polygons
intersect themselves, [`TestSelfIntersectionXld`](test_self_intersection_xld.md) can be
used. If the contour or polygon intersects itself, useful values
for the orientation can be calculated with
[`OrientationPointsXld`](orientation_points_xld.md).

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

## Result

The operator `OrientationXld` returns the value 2 (
H_MSG_TRUE)
if the input
is not empty. The behavior in case of empty input (no input contours
available) is set via the operator
`set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`GenContoursSkeletonXld`,
`EdgesSubPix`,
`ThresholdSubPix`,
`GenContourPolygonXld`,
`TestSelfIntersectionXld`

## Alternatives

`EllipticAxisXld`,
`SmallestRectangle2Xld`

## See also

`MomentsRegion2nd`

## Module

Foundation
