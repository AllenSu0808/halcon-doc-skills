# CircularityXld (Operator)

## Name

`CircularityXld` — Shape factor for the circularity (similarity to a circle) of contours or
polygons.

## Signature

`static void HOperatorSet.CircularityXld(HObject XLD, out HTuple circularity)`

`HTuple HXLD.CircularityXld()`

## Description

The operator `CircularityXld` calculates the similarity of
each input contour or polygon with a circle. The input contour or polygon
must not intersect itself, otherwise the resulting parameter is not
meaningful (Whether the input contour or polygon intersects itself or not
can be determined with [`TestSelfIntersectionXld`](test_self_intersection_xld.md)). If
the input contour or polygon is not closed it will be closed automatically.

**Calculation:**
If F is the enclosed area of the contour or polygon and max is the
maximum distance from the center to all contour or polygon pixels, the
shape factor *`circularity`* is defined as:
$$Circularity = \frac{F}{(\max^2 * \pi)}$$ ![figure](../assets/b8e3c76f9941e60f.svg)
The shape factor *`circularity`* of a circle is 1. If the contour
or polygon encloses an elongated area *`circularity`* is smaller than 1.
The operator `CircularityXld` especially responds to large bulges.

If more than one contour or polygon is passed, the numerical values of the
shape factor are stored in a tuple in the same order as the respective
contours or polygons in *`XLD`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` [HXLD](HXLD.md)

Contours or polygons to be examined.

**`circularity`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Roundness of the input contours or polygons.

Assertion:
`0 <= Circularity && Circularity <= 1.0`

## Result

The operator `CircularityXld` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input contour available) is
set via the operator `set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`GenContoursSkeletonXld`,
`EdgesSubPix`,
`ThresholdSubPix`,
`GenContourPolygonXld`,
`TestSelfIntersectionXld`

## Alternatives

`CompactnessXld`,
`ConvexityXld`,
`EccentricityXld`,
`RectangularityXld`

## See also

`AreaCenterXld`,
`SelectShapeXld`

## Module

Foundation
