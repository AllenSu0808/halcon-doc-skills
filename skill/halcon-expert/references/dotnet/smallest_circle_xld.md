# SmallestCircleXld (Operator)

## Name

`SmallestCircleXld` — Smallest enclosing circle of contours or polygons.

## Signature

`static void HOperatorSet.SmallestCircleXld(HObject XLD, out HTuple row, out HTuple column, out HTuple radius)`

`void HXLD.SmallestCircleXld(out HTuple row, out HTuple column, out HTuple radius)`

`void HXLD.SmallestCircleXld(out double row, out double column, out double radius)`

## Description

The operator `SmallestCircleXld` determines the smallest
enclosing circle of contours or polygons, i.e., the circle with the smallest
area of all circles containing the contour. For this circle the center
(*`row`*,*`column`*) and the radius (*`radius`*)
are calculated.

If several contours or polygons are passed in *`XLD`* corresponding
tuples are returned as output parameter.
In case of empty contours all parameters have the value 0.0 if no other
behavior was set (see [`SetSystem`](set_system.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` [HXLD](HXLD.md)

Contours or polygons to be examined.

**`row`** (output_control)  circle.center.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the center of the enclosing
circle.

**`column`** (output_control)  circle.center.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the center of the enclosing
circle.

**`radius`** (output_control)  circle.radius(-array) `→` [HTuple](HTuple.md) (*double*)

Radius of the enclosing circle.

Assertion:
`Radius >= 0`

## Complexity

If N is the number of contour points then the runtime complexity is
O(N*ln(N)).

## Result

The operator `SmallestCircleXld` returns the value 2 (
H_MSG_TRUE)
if the input is not empty. If the input is empty the behavior can be
set via `set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`GenContoursSkeletonXld`,
`EdgesSubPix`,
`ThresholdSubPix`,
`GenContourPolygonXld`

## Possible Successors

`GenEllipseContourXld`

## Alternatives

`SmallestRectangle1Xld`,
`SmallestRectangle2Xld`

## See also

`EllipticAxisXld`,
`SmallestRectangle1Xld`,
`SmallestRectangle2Xld`,
`ShapeTransXld`

## Module

Foundation
