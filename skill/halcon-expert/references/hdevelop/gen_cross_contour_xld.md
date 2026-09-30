# gen_cross_contour_xld (Operator)

## Name

`gen_cross_contour_xld` — Generate one XLD contour in the shape of a cross for each input point.

## Signature

`gen_cross_contour_xld( : Cross : Row, Col, Size, Angle : )`

## Description

`gen_cross_contour_xld` generates an XLD contour in the shape of a
cross for each input point (*`Row`*,*`Col`*).
Conceptually, the contour consists of two lines of length *`Size`*,
which intersect exactly in the input point. Their orientation is determined
by *`Angle`*. The cross is returned in *`Cross`*.

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

**`Cross`** (output_object)  xld_cont(-array) `→` object

Generated XLD contours.

**`Row`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinates of the input points.

**`Col`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinates of the input points.

Restriction:
`number(Col) == number(Row)`

**`Size`** (input_control)  number `→`  (real / integer)

Length of the cross bars.

Default:
6.0

Suggested values:
4.0, 6.0, 8.0, 10.0

Restriction:
`0.0 <= Size`

**`Angle`** (input_control)  angle.rad `→`  (real)

Orientation of the crosses.

Default:
0.785398

Suggested values:
0.0, 0.785398

## Result

`gen_cross_contour_xld` returns 2 (
H_MSG_TRUE)
if all parameters are correct
and no error occurs during execution.

## Possible Predecessors

`points_foerstner`,
`points_harris`,
`critical_points_sub_pix`,
`local_max_sub_pix`,
`local_min_sub_pix`,
`saddle_points_sub_pix`

## Alternatives

`disp_cross`

## Module

Foundation
