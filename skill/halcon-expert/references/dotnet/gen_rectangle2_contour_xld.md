# GenRectangle2ContourXld (Operator)

## Name

`GenRectangle2ContourXld` — Create an XLD contour in the shape of a rectangle.

## Signature

`static void HOperatorSet.GenRectangle2ContourXld(out HObject rectangle, HTuple row, HTuple column, HTuple phi, HTuple length1, HTuple length2)`

`void HXLDCont.GenRectangle2ContourXld(HTuple row, HTuple column, HTuple phi, HTuple length1, HTuple length2)`

`void HXLDCont.GenRectangle2ContourXld(double row, double column, double phi, double length1, double length2)`

## Description

`GenRectangle2ContourXld` creates one or more XLD contours
in the shape of a rectangle with arbitrary orientation. The
rectangle has the center (*`row`*, *`column`*), the
orientation *`phi`*, and the half edge lengths *`length1`*
and *`length2`*. The angle *`phi`* must be given in
radians and specifies the angle between the horizontal axis and the
edge with the half length *`length1`* in the mathematically
positive direction (counterclockwise).

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* or *N*.
Parameters with tuple length *1* will be repeated internally
such that the number of created items is always *N*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`rectangle`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Rectangle contour.

**`row`** (input_control)  rectangle2.center.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the center of the rectangle.

Default:
300.0

**`column`** (input_control)  rectangle2.center.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the center of the rectangle.

Default:
200.0

**`phi`** (input_control)  rectangle2.angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Orientation of the main axis of the rectangle [rad].

Default:
0.0

Restriction:
`- pi / 2 < Phi && Phi <= pi / 2`

**`length1`** (input_control)  rectangle2.hwidth(-array) `→` [HTuple](HTuple.md) (*double*)

First radius (half length) of the rectangle.

Default:
100.5

**`length2`** (input_control)  rectangle2.hheight(-array) `→` [HTuple](HTuple.md) (*double*)

Second radius (half width) of the rectangle.

Default:
20.5

## Result

`GenRectangle2ContourXld` returns 2 (
H_MSG_TRUE)
if all parameter
values are correct. If necessary, an exception is raised.

## Possible Predecessors

`FitRectangle2ContourXld`

## Alternatives

`GenRectangle2`

## See also

`GenContourPolygonXld`

## Module

Foundation
