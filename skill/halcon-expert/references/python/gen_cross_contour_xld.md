# gen_cross_contour_xld (Operator)

## Name

`gen_cross_contour_xld` — Generate one XLD contour in the shape of a cross for each input point.

## Signature

`def gen_cross_contour_xld(row: MaybeSequence[Union[float, int]], col: MaybeSequence[Union[float, int]], size: Union[float, int], angle: float) -> HObject`

## Description

`gen_cross_contour_xld` generates an XLD contour in the shape of a
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

**`cross`** (output_object)  xld_cont(-array) `→` HObject

Generated XLD contours.

**`row`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinates of the input points.

**`col`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinates of the input points.

Restriction:
`number(Col) == number(Row)`

**`size`** (input_control)  number `→` Union[float, int]

Length of the cross bars.

Default:
6.0

Suggested values:
4.0, 6.0, 8.0, 10.0

Restriction:
`0.0 <= Size`

**`angle`** (input_control)  angle.rad `→` float

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
