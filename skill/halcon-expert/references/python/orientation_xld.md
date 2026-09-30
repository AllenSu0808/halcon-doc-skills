# orientation_xld (Operator)

## Name

`orientation_xld` — Calculate the orientation of contours or polygons.

## Signature

`def orientation_xld(xld: HObject) -> Sequence[float]`

`def orientation_xld_s(xld: HObject) -> float`

## Description

The operator `orientation_xld` calculates the orientation
(*`phi`*) of each input contour or polygon (*`xld`*).
The operator is based on [`elliptic_axis_xld`](elliptic_axis_xld.md).
In addition, the contour respectively polygon
point with maximum distance to the center of gravity is calculated. If the
column coordinate of this point is less than the column coordinate
of the center of gravity the value of $\pi$ is added to the
angle. It is assumed that the contours or polygons are closed. If
this is not the case `orientation_xld` will artificially close
the contours or polygons.

It should be noted that `orientation_xld` only returns useful
results if the contour or polygon encloses a region in the plane. In
particular, the contour or polygon must not intersect itself. This
is particularly important if open contours or polygons are passed
because they are closed automatically, which can produce a
self-intersection. To test whether the contours or polygons
intersect themselves, [`test_self_intersection_xld`](test_self_intersection_xld.md) can be
used. If the contour or polygon intersects itself, useful values
for the orientation can be calculated with
[`orientation_points_xld`](orientation_points_xld.md).

If more than one contour or polygon is passed, the values of the
orientations are stored in a tuple in the same order as the respective
contours or polygons in *`xld`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`xld`** (input_object)  xld(-array) `→` HObject

Contours or polygons to be examined.

**`phi`** (output_control)  angle.rad(-array) `→` Sequence[float]

Orientation of the contours or polygons (radians).

Assertion:
`- pi < Phi && Phi <= pi`

## Result

The operator `orientation_xld` returns the value 2 (
H_MSG_TRUE)
if the input
is not empty. The behavior in case of empty input (no input contours
available) is set via the operator
`set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`edges_sub_pix`,
`threshold_sub_pix`,
`gen_contour_polygon_xld`,
`test_self_intersection_xld`

## Alternatives

`elliptic_axis_xld`,
`smallest_rectangle2_xld`

## See also

`moments_region_2nd`

## Module

Foundation
