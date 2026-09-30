# EllipticAxisXld (Operator)

## Name

`EllipticAxisXld` — Parameters of the equivalent ellipse of contours or polygons.

## Signature

`static void HOperatorSet.EllipticAxisXld(HObject XLD, out HTuple ra, out HTuple rb, out HTuple phi)`

`HTuple HXLD.EllipticAxisXld(out HTuple rb, out HTuple phi)`

`double HXLD.EllipticAxisXld(out double rb, out double phi)`

## Description

The operator `EllipticAxisXld` calculates the radii and the
orientations of the ellipses having the same orientation and the same
aspect ratio as the input contours or polygons.
The length of the major radius
*`ra`* and the minor radius *`rb`* as well as the
orientation of the main axis with regard to the horizontal
(*`phi`*) are determined. The angle is indicated in radians.
It is assumed that the contours or polygons are closed. If this is
not the case `EllipticAxisXld` will artificially close the
contours or polygons.

**Calculation:**
If the moments $M_{20}$, $M_{02}$ and $M_{11}$ are
normalized and passed to the area (see [`MomentsXld`](moments_xld.md)),
the radii *`ra`* and *`rb`* are calculated as:
$$Ra = \frac{\sqrt{8(M_{20} + M_{02} + \sqrt{(M_{20} - M_{02})^2 + 4M_{11}^2})}}{2} \\ Rb = \frac{\sqrt{8(M_{20} + M_{02} - \sqrt{(M_{20} - M_{02})^2 + 4M_{11}^2})}}{2}$$ ![figure](../assets/0e7be60ed9aefa94.svg)
The orientation *`phi`* is defined by:
$$\texttt{Phi}=-0.5\text{atan2}(2M_{11},M_{02}-M_{20})$$

It should be noted that `EllipticAxisXld` only returns
useful results if the contour or polygon encloses a region in the
plane. In particular, the contour or polygon must not intersect
itself. This is particularly important if open contours or polygons
are passed because they are closed automatically, which can produce
a self-intersection. To test whether the contours or polygons
intersect themselves, [`TestSelfIntersectionXld`](test_self_intersection_xld.md) can be
used. If the contour or polygon intersects itself, useful values
for the ellipse parameters can be calculated with
[`EllipticAxisPointsXld`](elliptic_axis_points_xld.md).

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

**`ra`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Major radius.

Assertion:
`Ra >= 0.0`

**`rb`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Minor radius.

Assertion:
`Rb >= 0.0 && Rb <= Ra`

**`phi`** (output_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Angle between the major axis and the x axis
(radians).

Assertion:
`- pi / 2 < Phi && Phi <= pi / 2`

## Complexity

If N is the number of contour or polygon points, the runtime complexity is
O(N).

## Result

`EllipticAxisXld` returns 2 (
H_MSG_TRUE)
if the input is not empty.
If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`GenContoursSkeletonXld`,
`EdgesSubPix`,
`ThresholdSubPix`,
`GenContourPolygonXld`,
`TestSelfIntersectionXld`

## Possible Successors

`AreaCenterXld`,
`GenEllipseContourXld`

## Alternatives

`EllipticAxisPointsXld`,
`SmallestRectangle2`

## See also

`MomentsXld`,
`SmallestCircleXld`,
`SmallestRectangle1Xld`,
`SmallestRectangle2Xld`,
`ShapeTransXld`

## References

R. Haralick, L. Shapiro
“Computer and Robot Vision”
Addison-Wesley, 1992, pp. 73-75

## Module

Foundation
