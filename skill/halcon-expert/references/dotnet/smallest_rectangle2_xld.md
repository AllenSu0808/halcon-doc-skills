# SmallestRectangle2Xld (Operator)

## Name

`SmallestRectangle2Xld` — Smallest enclosing rectangle with arbitrary orientation of contours or
polygons.

## Signature

`static void HOperatorSet.SmallestRectangle2Xld(HObject XLD, out HTuple row, out HTuple column, out HTuple phi, out HTuple length1, out HTuple length2)`

`void HXLD.SmallestRectangle2Xld(out HTuple row, out HTuple column, out HTuple phi, out HTuple length1, out HTuple length2)`

`void HXLD.SmallestRectangle2Xld(out double row, out double column, out double phi, out double length1, out double length2)`

## Description

The operator `SmallestRectangle2Xld` determines the smallest
enclosing rectangle of each input contour or polygon, i.e., the rectangle
with the smallest area of all rectangles containing the contour. For this
rectangle the center, the inclination, and the two radii are calculated.

If more than one contour or polygon is passed, the results are stored
in tuples in the same order as the respective contours or polygons in
*`XLD`*. In case of an empty contour all parameters
have the value 0.0 if no other behavior was set (see [`SetSystem`](set_system.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` [HXLD](HXLD.md)

Contours or polygons to be examined.

**`row`** (output_control)  rectangle2.center.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the center point of the enclosing
rectangle.

**`column`** (output_control)  rectangle2.center.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the center point of the
enclosing rectangle.

**`phi`** (output_control)  rectangle2.angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Orientation of the enclosing rectangle
(arc measure)

Assertion:
`- pi / 2 < Phi && Phi <= pi / 2`

**`length1`** (output_control)  rectangle2.hwidth(-array) `→` [HTuple](HTuple.md) (*double*)

First radius (half length) of the enclosing
rectangle.

Assertion:
`Length1 >= 0.0`

**`length2`** (output_control)  rectangle2.hheight(-array) `→` [HTuple](HTuple.md) (*double*)

Second radius (half width) of the enclosing
rectangle.

Assertion:
`Length2 >= 0.0 && Length2 <= Length1`

## Complexity

If N is the number of contour points and C is the number of points
in the convex hull, the runtime complexity is O(N*ln(N)+C^2).

## Result

`SmallestRectangle2Xld` returns 2 (
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

`SmallestRectangle1`,
`ShapeTransXld`

## See also

`SmallestRectangle1`,
`SmallestCircle`,
`EllipticAxisXld`

## Module

Foundation
