# GenCrossContourXld (Operator)

## Name

`GenCrossContourXld` — Generate one XLD contour in the shape of a cross for each input point.

## Signature

`static void HOperatorSet.GenCrossContourXld(out HObject cross, HTuple row, HTuple col, HTuple size, HTuple angle)`

`void HXLDCont.GenCrossContourXld(HTuple row, HTuple col, HTuple size, double angle)`

`void HXLDCont.GenCrossContourXld(double row, double col, double size, double angle)`

## Description

`GenCrossContourXld` generates an XLD contour in the shape of a
cross for each input point (*`row`*,*`col`*).
Conceptually, the contour consists of two lines of length *`size`*,
which intersect exactly in the input point. Their orientation is determined
by *`angle`*. The cross is returned in *`cross`*.

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

**`cross`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Generated XLD contours.

**`row`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of the input points.

**`col`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of the input points.

Restriction:
`number(Col) == number(Row)`

**`size`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Length of the cross bars.

Default:
6.0

Suggested values:
4.0, 6.0, 8.0, 10.0

Restriction:
`0.0 <= Size`

**`angle`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Orientation of the crosses.

Default:
0.785398

Suggested values:
0.0, 0.785398

## Result

`GenCrossContourXld` returns 2 (
H_MSG_TRUE)
if all parameters are correct
and no error occurs during execution.

## Possible Predecessors

`PointsFoerstner`,
`PointsHarris`,
`CriticalPointsSubPix`,
`LocalMaxSubPix`,
`LocalMinSubPix`,
`SaddlePointsSubPix`

## Alternatives

`DispCross`

## Module

Foundation
