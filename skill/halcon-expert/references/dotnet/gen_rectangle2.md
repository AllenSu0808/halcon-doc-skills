# GenRectangle2 (Operator)

## Name

`GenRectangle2` — Create a rectangle of any orientation.

## Signature

`static void HOperatorSet.GenRectangle2(out HObject rectangle, HTuple row, HTuple column, HTuple phi, HTuple length1, HTuple length2)`

`void HRegion.GenRectangle2(HTuple row, HTuple column, HTuple phi, HTuple length1, HTuple length2)`

`void HRegion.GenRectangle2(double row, double column, double phi, double length1, double length2)`

## Description

The operator `GenRectangle2` generates one or more rectangles
with the center
(*`row`*, *`column`*) , the orientation *`phi`* and
the half edge lengths *`length1`* and *`length2`*.
The orientation is given in arc measure and indicates the angle between
the horizontal axis and the edge (with *`length1`*)
(mathematically positive).
The coordinate system runs from (0,0) (upper left corner) to
(Width-1,Height-1). See [`GetSystem`](get_system.md) and
[`ResetObjDb`](reset_obj_db.md) in this context.
More than one region can be created by passing one tuple of corner points.

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* or *N*.
Parameters with tuple length *1* will be repeated internally
such that the number of created items is always *N*.

## Attention

The gray values of the output objects are undefined. For speed
reasons, the resulting region may contain additional pixels at the
border and some individual pixels at the border may be missing.
This may lead to an inconsistency between the operators
[`SmallestRectangle2`](smallest_rectangle2.md) and `GenRectangle2`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`rectangle`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Created rectangle.

**`row`** (input_control)  rectangle2.center.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Line index of the center.

Default:
300.0

Suggested values:
10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0

Value range:
`row` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`column`** (input_control)  rectangle2.center.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column index of the center.

Default:
200.0

Suggested values:
10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0

Value range:
`column` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`phi`** (input_control)  rectangle2.angle.rad(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Angle of the first edge to the horizontal (in radians).

Default:
0.0

Suggested values:
-1.178097, -0.785398, -0.392699, 0.0, 0.392699, 0.785398, 1.178097

Value range:
`phi` (lin)

Restriction:
`- pi / 2 < Phi && Phi <= pi / 2`

**`length1`** (input_control)  rectangle2.hwidth(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Half width.

Default:
100.0

Suggested values:
3.0, 5.0, 10.0, 15.0, 20.0, 50.0, 100.0, 200.0, 300.0, 500.0

Value range:
`length1` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`length2`** (input_control)  rectangle2.hheight(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Half height.

Default:
20.0

Suggested values:
1.0, 2.0, 3.0, 5.0, 10.0, 15.0, 20.0, 50.0, 100.0, 200.0

Value range:
`length2` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

## Result

If the parameter values are correct the operator `GenRectangle2`
returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.
The clipping according to the current image format is set via the
operator `set_system('clip_region',<'true'/'false'>)`.

## Possible Successors

`PaintRegion`,
`ReduceDomain`

## Alternatives

`GenRectangle1`,
`GenRegionPolygonFilled`,
`GenRegionPolygon`,
`GenRegionPoints`,
`FillUp`

## See also

`DrawRectangle2`,
`ReduceDomain`,
`SmallestRectangle2`,
`GenEllipse`

## Module

Foundation
