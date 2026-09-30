# CompactnessXld (Operator)

## Name

`CompactnessXld` — Shape factor for the compactness of contours or polygons.

## Signature

`static void HOperatorSet.CompactnessXld(HObject XLD, out HTuple compactness)`

`HTuple HXLD.CompactnessXld()`

## Description

The operator `CompactnessXld` calculates the compactness of each
input contour or polygon in *`XLD`*. The input contour or polygon must
not intersect itself, otherwise the resulting parameter is not meaningful
(Whether the input contour or polygon intersects itself or not can be
determined with [`TestSelfIntersectionXld`](test_self_intersection_xld.md)). If
the input contour or polygon is not closed it will be closed automatically.

**Calculation:**
If L is the length and F the
enclosed area of the contour or polygon the shape
factor *`compactness`* is defined as:
$$\text{Compactness} = \frac{L^2}{4\pi F}$$ ![figure](../assets/f985e86fa6969b93.svg)
The shape factor *`compactness`* of a circle is 1.
If the contour or polygon encloses an elongated area *`compactness`*
is larger than 1. The operator `CompactnessXld` responds to the
course of the contour or polygon (roughness).
If more than one contour or polygon is passed, the shape factors are stored
in a tuple in the same order as the respective contours or polygons in
*`XLD`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` [HXLD](HXLD.md)

Contours or polygons to be examined.

**`compactness`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Compactness of the input contours or polygons.

Assertion:
`Compactness >= 1.0 || Compactness == 0`

## Result

The operator `CompactnessXld` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input contours available) is
set via the operator `set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`GenContoursSkeletonXld`,
`EdgesSubPix`,
`ThresholdSubPix`,
`GenContourPolygonXld`,
`TestSelfIntersectionXld`

## Alternatives

`CircularityXld`,
`ConvexityXld`,
`EccentricityXld`,
`RectangularityXld`

## See also

`AreaCenterXld`,
`SelectShapeXld`

## Module

Foundation
