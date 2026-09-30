# EccentricityXld (Operator)

## Name

`EccentricityXld` — Shape features derived from the ellipse parameters of contours or polygons.

## Signature

`static void HOperatorSet.EccentricityXld(HObject XLD, out HTuple anisometry, out HTuple bulkiness, out HTuple structureFactor)`

`HTuple HXLD.EccentricityXld(out HTuple bulkiness, out HTuple structureFactor)`

`double HXLD.EccentricityXld(out double bulkiness, out double structureFactor)`

## Description

The operator `EccentricityXld` calculates the three shape
features *`anisometry`*, *`bulkiness`*, and
*`structureFactor`* derived from the geometric moments for each input
contour or polygon. If the
input contour or polygon is not closed it will be closed automatically.

**Calculation:**
If the ellipse radii Ra, Rb
([`EllipticAxisXld`](elliptic_axis_xld.md)) and the enclosed area A of the contour or
polygon are given, the following applies:
$$Anisometry = \frac{Ra}{Rb}\\ Bulkiness = \frac{\pi \cdot Ra \cdot Rb}{F}\\ StructureFactor = Anisometry \cdot Bulkiness - 1$$ ![figure](../assets/b1b44cfe22ff6989.svg)
The anisometry of a circle is 1.0.

It should be noted that `EccentricityXld` only returns useful
results if the contour or polygon encloses a region in the plane. In
particular, the contour or polygon must not intersect itself. This
is particularly important if open contours or polygons are passed
because they are closed automatically, which can produce a
self-intersection. To test whether the contours or polygons
intersect themselves, [`TestSelfIntersectionXld`](test_self_intersection_xld.md) can be
used. If the contour or polygon intersects itself, a useful value
for the anisometry can be calculated with
[`EccentricityPointsXld`](eccentricity_points_xld.md).

If more than one contour is passed the results are stored in tuples,
the index of a value in the tuple corresponding to the index of a
contour in the input.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` [HXLD](HXLD.md)

Contours or polygons to be examined.

**`anisometry`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Anisometry of the contours or polygons.

Assertion:
`Anisometry >= 1.0`

**`bulkiness`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Bulkiness of the contours or polygons.

**`structureFactor`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Structure factor of the contours or polygons.

## Result

The operator `EccentricityXld` returns the value 2 (
H_MSG_TRUE)
if the input is not empty. The behavior in case of empty input (no input
contours available) is set via the operator
`set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`GenContoursSkeletonXld`,
`EdgesSubPix`,
`ThresholdSubPix`,
`GenContourPolygonXld`,
`TestSelfIntersectionXld`

## Alternatives

`EccentricityPointsXld`

## See also

`EllipticAxisXld`,
`MomentsRegion2nd`,
`SelectShapeXld`,
`AreaCenterXld`

## Module

Foundation
