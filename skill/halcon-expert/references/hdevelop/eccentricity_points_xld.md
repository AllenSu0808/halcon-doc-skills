# eccentricity_points_xld (Operator)

## Name

`eccentricity_points_xld` — Anisometry of contours or polygons treated as point clouds.

## Signature

`eccentricity_points_xld(XLD : : : Anisometry)`

## Description

The operator `eccentricity_points_xld` calculates the shape
feature *`Anisometry`* derived from the geometric moments of the
point cloud given by the contour or polygon *`XLD`* (i.e., the order
of the points in the contour or polygon is not taken into account). If the
contour or polygon is closed (end point = start point), the end point of
the contour or polygon is not taken into account to avoid that it receives
twice the weight of the other points.

**Calculation:**
If the ellipse radii Ra, Rb ([`elliptic_axis_points_xld`](elliptic_axis_points_xld.md)) are
given, the following applies:
$$Anisometry = \frac{R a}{R b}$$ ![figure](../assets/82a3d81084561c26.svg)
The anisometry of a circle is 1.0.

`eccentricity_points_xld` should be used if the contour *`XLD`*
intersects itself or if it is not possible to close the contour using a line
from end to start point without self-intersection, because in this case
[`eccentricity_xld`](eccentricity_xld.md) does not produce useful results. To test whether
the contours or polygons intersect themselves,
[`test_self_intersection_xld`](test_self_intersection_xld.md) can be used.

If more than one contour or polygon is passed, the values of the anisometry
are stored in a tuple in the same order as the respective contours or
polygons in *`XLD`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` object

Contours or polygons to be examined.

**`Anisometry`** (output_control)  real(-array) `→`  (real)

Anisometry of the contours or polygons.

Assertion:
`Anisometry >= 1.0`

## Result

The operator `eccentricity_points_xld` returns the value 2 (
H_MSG_TRUE)
if the input is not empty. The behavior in case of empty input (no
input contours available) is set via the operator
`set_system('no_object_result',<Result>)`. If necessary an
exception is raised.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`edges_sub_pix`,
`threshold_sub_pix`,
`gen_contour_polygon_xld`,
`test_self_intersection_xld`

## Alternatives

`eccentricity_xld`

## See also

`elliptic_axis_points_xld`,
`moments_region_2nd`,
`select_shape_xld`

## Module

Foundation
