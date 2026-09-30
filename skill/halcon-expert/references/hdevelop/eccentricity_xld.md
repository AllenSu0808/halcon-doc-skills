# eccentricity_xld (Operator)

## Name

`eccentricity_xld` — Shape features derived from the ellipse parameters of contours or polygons.

## Signature

`eccentricity_xld(XLD : : : Anisometry, Bulkiness, StructureFactor)`

## Description

The operator `eccentricity_xld` calculates the three shape
features *`Anisometry`*, *`Bulkiness`*, and
*`StructureFactor`* derived from the geometric moments for each input
contour or polygon. If the
input contour or polygon is not closed it will be closed automatically.

**Calculation:**
If the ellipse radii Ra, Rb
([`elliptic_axis_xld`](elliptic_axis_xld.md)) and the enclosed area A of the contour or
polygon are given, the following applies:
$$Anisometry = \frac{Ra}{Rb}\\ Bulkiness = \frac{\pi \cdot Ra \cdot Rb}{F}\\ StructureFactor = Anisometry \cdot Bulkiness - 1$$ ![figure](../assets/b1b44cfe22ff6989.svg)
The anisometry of a circle is 1.0.

It should be noted that `eccentricity_xld` only returns useful
results if the contour or polygon encloses a region in the plane. In
particular, the contour or polygon must not intersect itself. This
is particularly important if open contours or polygons are passed
because they are closed automatically, which can produce a
self-intersection. To test whether the contours or polygons
intersect themselves, [`test_self_intersection_xld`](test_self_intersection_xld.md) can be
used. If the contour or polygon intersects itself, a useful value
for the anisometry can be calculated with
[`eccentricity_points_xld`](eccentricity_points_xld.md).

If more than one contour is passed the results are stored in tuples,
the index of a value in the tuple corresponding to the index of a
contour in the input.

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

**`Bulkiness`** (output_control)  real(-array) `→`  (real)

Bulkiness of the contours or polygons.

**`StructureFactor`** (output_control)  real(-array) `→`  (real)

Structure factor of the contours or polygons.

## Result

The operator `eccentricity_xld` returns the value 2 (
H_MSG_TRUE)
if the input is not empty. The behavior in case of empty input (no input
contours available) is set via the operator
`set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`edges_sub_pix`,
`threshold_sub_pix`,
`gen_contour_polygon_xld`,
`test_self_intersection_xld`

## Alternatives

`eccentricity_points_xld`

## See also

`elliptic_axis_xld`,
`moments_region_2nd`,
`select_shape_xld`,
`area_center_xld`

## Module

Foundation
