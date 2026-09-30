# elliptic_axis_xld (Operator)

## Name

`elliptic_axis_xld` — Parameters of the equivalent ellipse of contours or polygons.

## Signature

`elliptic_axis_xld(XLD : : : Ra, Rb, Phi)`

## Description

The operator `elliptic_axis_xld` calculates the radii and the
orientations of the ellipses having the same orientation and the same
aspect ratio as the input contours or polygons.
The length of the major radius
*`Ra`* and the minor radius *`Rb`* as well as the
orientation of the main axis with regard to the horizontal
(*`Phi`*) are determined. The angle is indicated in radians.
It is assumed that the contours or polygons are closed. If this is
not the case `elliptic_axis_xld` will artificially close the
contours or polygons.

**Calculation:**
If the moments $M_{20}$, $M_{02}$ and $M_{11}$ are
normalized and passed to the area (see [`moments_xld`](moments_xld.md)),
the radii *`Ra`* and *`Rb`* are calculated as:
$$Ra = \frac{\sqrt{8(M_{20} + M_{02} + \sqrt{(M_{20} - M_{02})^2 + 4M_{11}^2})}}{2} \\ Rb = \frac{\sqrt{8(M_{20} + M_{02} - \sqrt{(M_{20} - M_{02})^2 + 4M_{11}^2})}}{2}$$ ![figure](../assets/0e7be60ed9aefa94.svg)
The orientation *`Phi`* is defined by:
$$\texttt{Phi}=-0.5\text{atan2}(2M_{11},M_{02}-M_{20})$$

It should be noted that `elliptic_axis_xld` only returns
useful results if the contour or polygon encloses a region in the
plane. In particular, the contour or polygon must not intersect
itself. This is particularly important if open contours or polygons
are passed because they are closed automatically, which can produce
a self-intersection. To test whether the contours or polygons
intersect themselves, [`test_self_intersection_xld`](test_self_intersection_xld.md) can be
used. If the contour or polygon intersects itself, useful values
for the ellipse parameters can be calculated with
[`elliptic_axis_points_xld`](elliptic_axis_points_xld.md).

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

**`Ra`** (output_control)  real(-array) `→`  (real)

Major radius.

Assertion:
`Ra >= 0.0`

**`Rb`** (output_control)  real(-array) `→`  (real)

Minor radius.

Assertion:
`Rb >= 0.0 && Rb <= Ra`

**`Phi`** (output_control)  angle.rad(-array) `→`  (real)

Angle between the major axis and the x axis
(radians).

Assertion:
`- pi / 2 < Phi && Phi <= pi / 2`

## Complexity

If N is the number of contour or polygon points, the runtime complexity is
O(N).

## Result

`elliptic_axis_xld` returns 2 (
H_MSG_TRUE)
if the input is not empty.
If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`edges_sub_pix`,
`threshold_sub_pix`,
`gen_contour_polygon_xld`,
`test_self_intersection_xld`

## Possible Successors

`area_center_xld`,
`gen_ellipse_contour_xld`

## Alternatives

`elliptic_axis_points_xld`,
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
