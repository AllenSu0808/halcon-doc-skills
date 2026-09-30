# elliptic_axis_points_xld (Operator)

## Name

`elliptic_axis_points_xld` — Parameters of the equivalent ellipse of contours or polygons treated as
point clouds.

## Signature

`def elliptic_axis_points_xld(xld: HObject) -> Tuple[Sequence[float], Sequence[float], Sequence[float]]`

`def elliptic_axis_points_xld_s(xld: HObject) -> Tuple[float, float, float]`

## Description

The operator `elliptic_axis_points_xld` calculates the radii
(*`ra`*, *`rb`*) and the orientation (*`phi`*, in radians)
of the ellipse
having the same orientation and the same aspect ratio as the point cloud
given by the contour or polygon
*`xld`* (i.e., the order of the points in the contour or
polygon is not taken into account). If the contour or
polygon is closed (end point = start point), the end point of the contour or
polygon is not taken into account to avoid that it receives twice
the weight of the other points.

**Calculation:**
If the moments $M_{20}$, $M_{02}$ and $M_{11}$
are normalized to the area (see [`moments_points_xld`](moments_points_xld.md)),
the major radius *`ra`* and the minor radius *`rb`* are calculated
as:
$$Ra = \frac{\sqrt{8(M_{20} + M_{02} + \sqrt{(M_{20} - M_{02})^2 + 4M_{11}^2})}}{2} \\ Rb = \frac{\sqrt{8(M_{20} + M_{02} - \sqrt{(M_{20} - M_{02})^2 + 4M_{11}^2})}}{2}$$ ![figure](../assets/0e7be60ed9aefa94.svg) The orientation *`phi`*, i.e., the angle between the major axis
and the x (column) axis, is defined by:
$$\texttt{Phi}=-0.5\text{atan2}(2M_{11},M_{02}-M_{20})$$

`elliptic_axis_points_xld` should be used if the contour *`xld`*
intersects itself or if it is not possible to close the contour using a line
from end to start point without self-intersection, because in this case
[`elliptic_axis_xld`](elliptic_axis_xld.md) does not produce useful results. To test whether
the contours or polygons intersect themselves,
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

**`ra`** (output_control)  real(-array) `→` Sequence[float]

Major radius.

Assertion:
`Ra >= 0.0`

**`rb`** (output_control)  real(-array) `→` Sequence[float]

Minor radius.

Assertion:
`Rb >= 0.0 && Rb <= Ra`

**`phi`** (output_control)  angle.rad(-array) `→` Sequence[float]

Angle between the major axis and the column axis
(radians).

Assertion:
`- pi / 2 < Phi && Phi <= pi / 2`

## Complexity

Let n be the number of points of the contour or polygon.
Then the run time is O(n).

## Result

`elliptic_axis_points_xld` returns 2 (
H_MSG_TRUE)
if the input is not
empty. If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`edges_sub_pix`,
`threshold_sub_pix`,
`gen_contour_polygon_xld`,
`test_self_intersection_xld`

## Possible Successors

`area_center_points_xld`,
`gen_ellipse_contour_xld`

## Alternatives

`elliptic_axis_xld`,
`smallest_rectangle2`

## See also

`moments_xld`,
`smallest_circle_xld`,
`smallest_rectangle1_xld`,
`smallest_rectangle2_xld`,
`shape_trans_xld`

## References

R. Haralick, L. Shapiro
“Computer and Robot Vision”
Addison-Wesley, 1992, pp. 73-75

## Module

Foundation
