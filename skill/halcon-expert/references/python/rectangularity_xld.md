# rectangularity_xld (Operator)

## Name

`rectangularity_xld` — Shape factor for the rectangularity of contours or polygons.

## Signature

`def rectangularity_xld(xld: HObject) -> Sequence[float]`

`def rectangularity_xld_s(xld: HObject) -> float`

## Description

The operator `rectangularity_xld` calculates the rectangularity of
each input contour or polygon in *`xld`*. The input contour or polygon
must not intersect itself, otherwise the resulting parameter is not
meaningful (Whether the input contour or polygon intersects itself or not
can be determined with [`test_self_intersection_xld`](test_self_intersection_xld.md)). If
the input contour or polygon is not closed it will be closed automatically.

To determine the rectangularity, first a rectangle is computed that has
the same first and second order moments as the input contour or polygon. The
computation of the rectangularity measure is finally based on the
area of the difference between the computed rectangle and the
input contour or polygon normalized with respect to the area of the rectangle.

For rectangles `rectangularity_xld` returns the value 1. The more the
input contour or polygon deviates from a perfect rectangle, the less the
returned value for *`rectangularity`* will be. If more than one contour
or polygon is passed, the results are stored in tuples in the same order as
the respective contours or polygons in *`xld`*.

## Attention

For input contours or polygons which orientation cannot be computed by using
second order moments (as it is the case for squares, for example), the
returned *`rectangularity`* is underestimated by up to 10% depending
on the orientation of the input contour or polygon.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`xld`** (input_object)  xld(-array) `→` HObject

Contours or polygons to be examined.

**`rectangularity`** (output_control)  real(-array) `→` Sequence[float]

Rectangularity of the input contours or polygons.

Assertion:
`0 <= Rectangularity && Rectangularity <= 1.0`

## Result

The operator `rectangularity_xld` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input contours or polygons available)
is set via the operator `set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`edges_sub_pix`,
`threshold_sub_pix`,
`gen_contour_polygon_xld`,
`test_self_intersection_xld`

## Alternatives

`circularity_xld`,
`convexity_xld`,
`compactness_xld`,
`eccentricity_xld`

## See also

`area_center_xld`,
`select_shape_xld`

## References

P. L. Rosin: “Measuring rectangularity”;
Machine Vision and Applications; vol. 11;
pp. 191-196; Springer-Verlag, 1999.

## Module

Foundation
