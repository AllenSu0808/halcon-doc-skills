# EllipticAxisPointsXld (Operator)

## Name

`EllipticAxisPointsXld` — Parameters of the equivalent ellipse of contours or polygons treated as
point clouds.

## Signature

`static void HOperatorSet.EllipticAxisPointsXld(HObject XLD, out HTuple ra, out HTuple rb, out HTuple phi)`

`HTuple HXLD.EllipticAxisPointsXld(out HTuple rb, out HTuple phi)`

`double HXLD.EllipticAxisPointsXld(out double rb, out double phi)`

## Description

The operator `EllipticAxisPointsXld` calculates the radii
(*`ra`*, *`rb`*) and the orientation (*`phi`*, in radians)
of the ellipse
having the same orientation and the same aspect ratio as the point cloud
given by the contour or polygon
*`XLD`* (i.e., the order of the points in the contour or
polygon is not taken into account). If the contour or
polygon is closed (end point = start point), the end point of the contour or
polygon is not taken into account to avoid that it receives twice
the weight of the other points.

**Calculation:**
If the moments $M_{20}$, $M_{02}$ and $M_{11}$
are normalized to the area (see [`MomentsPointsXld`](moments_points_xld.md)),
the major radius *`ra`* and the minor radius *`rb`* are calculated
as:
$$Ra = \frac{\sqrt{8(M_{20} + M_{02} + \sqrt{(M_{20} - M_{02})^2 + 4M_{11}^2})}}{2} \\ Rb = \frac{\sqrt{8(M_{20} + M_{02} - \sqrt{(M_{20} - M_{02})^2 + 4M_{11}^2})}}{2}$$ ![figure](../assets/0e7be60ed9aefa94.svg) The orientation *`phi`*, i.e., the angle between the major axis
and the x (column) axis, is defined by:
$$\texttt{Phi}=-0.5\text{atan2}(2M_{11},M_{02}-M_{20})$$

`EllipticAxisPointsXld` should be used if the contour *`XLD`*
intersects itself or if it is not possible to close the contour using a line
from end to start point without self-intersection, because in this case
[`EllipticAxisXld`](elliptic_axis_xld.md) does not produce useful results. To test whether
the contours or polygons intersect themselves,
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

**`ra`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Major radius.

Assertion:
`Ra >= 0.0`

**`rb`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Minor radius.

Assertion:
`Rb >= 0.0 && Rb <= Ra`

**`phi`** (output_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Angle between the major axis and the column axis
(radians).

Assertion:
`- pi / 2 < Phi && Phi <= pi / 2`

## Complexity

Let n be the number of points of the contour or polygon.
Then the run time is O(n).

## Result

`EllipticAxisPointsXld` returns 2 (
H_MSG_TRUE)
if the input is not
empty. If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Predecessors

`GenContoursSkeletonXld`,
`EdgesSubPix`,
`ThresholdSubPix`,
`GenContourPolygonXld`,
`TestSelfIntersectionXld`

## Possible Successors

`AreaCenterPointsXld`,
`GenEllipseContourXld`

## Alternatives

`EllipticAxisXld`,
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
