# SmallestRectangle1Xld (Operator)

## Name

`SmallestRectangle1Xld` — Enclosing rectangle parallel to the coordinate axes of contours or polygons.

## Signature

`static void HOperatorSet.SmallestRectangle1Xld(HObject XLD, out HTuple row1, out HTuple column1, out HTuple row2, out HTuple column2)`

`void HXLD.SmallestRectangle1Xld(out HTuple row1, out HTuple column1, out HTuple row2, out HTuple column2)`

`void HXLD.SmallestRectangle1Xld(out double row1, out double column1, out double row2, out double column2)`

## Description

The operator `SmallestRectangle1Xld` calculates the enclosing
rectangle (parallel to the coordinate axes) for each input contour or
polygon.
The enclosing rectangle is described by the coordinates of the corner
pixels (*`row1`*,*`column1`*,*`row2`*,*`column2`*)

If more than one contour or polygon is passed, the results are stored in
tuples in the same order as the respective contours or polygons in
*`XLD`*. In case of an empty contour all parameters have the value 0
if no other behavior was set (see [`SetSystem`](set_system.md)).

## Attention

In case of empty contours the result of *`row1`*,*`column1`*,
*`row2`* and *`column2`* (all are 0) can lead to confusion.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` [HXLD](HXLD.md)

Contours or polygons to be examined.

**`row1`** (output_control)  rectangle.origin.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of upper left corner point of the
enclosing rectangle.

**`column1`** (output_control)  rectangle.origin.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of upper left corner point of the
enclosing rectangle.

**`row2`** (output_control)  rectangle.corner.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of lower right corner point of the
enclosing rectangle.

**`column2`** (output_control)  rectangle.corner.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of lower right corner point of the
enclosing rectangle.

## Complexity

If N is the number of contour points, the runtime complexity is
O(N).

## Result

`SmallestRectangle1Xld` returns 2 (
H_MSG_TRUE)
if the input is not empty.
If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`GenContoursSkeletonXld`,
`EdgesSubPix`,
`ThresholdSubPix`,
`GenContourPolygonXld`

## Possible Successors

`GenPolygonsXld`

## Alternatives

`HeightWidthRatioXld`,
`SmallestRectangle2Xld`,
`ShapeTransXld`

## See also

`ShapeTransXld`,
`SmallestRectangle2Xld`,
`SmallestCircleXld`,
`EllipticAxisXld`,
`AreaCenterXld`

## Module

Foundation
