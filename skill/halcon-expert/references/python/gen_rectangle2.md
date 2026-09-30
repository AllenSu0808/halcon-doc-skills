# gen_rectangle2 (Operator)

## Name

`gen_rectangle2` — Create a rectangle of any orientation.

## Signature

`def gen_rectangle2(row: MaybeSequence[Union[int, float]], column: MaybeSequence[Union[int, float]], phi: MaybeSequence[Union[int, float]], length_1: MaybeSequence[Union[int, float]], length_2: MaybeSequence[Union[int, float]]) -> HObject`

## Description

The operator `gen_rectangle2` generates one or more rectangles
with the center
(*`row`*, *`column`*) , the orientation *`phi`* and
the half edge lengths *`length_1`* and *`length_2`*.
The orientation is given in arc measure and indicates the angle between
the horizontal axis and the edge (with *`length_1`*)
(mathematically positive).
The coordinate system runs from (0,0) (upper left corner) to
(Width-1,Height-1). See [`get_system`](get_system.md) and
[`reset_obj_db`](reset_obj_db.md) in this context.
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
[`smallest_rectangle2`](smallest_rectangle2.md) and `gen_rectangle2`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`rectangle`** (output_object)  region(-array) `→` HObject

Created rectangle.

**`row`** (input_control)  rectangle2.center.y(-array) `→` MaybeSequence[Union[int, float]]

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

**`column`** (input_control)  rectangle2.center.x(-array) `→` MaybeSequence[Union[int, float]]

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

**`phi`** (input_control)  rectangle2.angle.rad(-array) `→` MaybeSequence[Union[int, float]]

Angle of the first edge to the horizontal (in radians).

Default:
0.0

Suggested values:
-1.178097, -0.785398, -0.392699, 0.0, 0.392699, 0.785398, 1.178097

Value range:
`phi` (lin)

Restriction:
`- pi / 2 < Phi && Phi <= pi / 2`

**`length_1`** (input_control)  rectangle2.hwidth(-array) `→` MaybeSequence[Union[int, float]]

Half width.

Default:
100.0

Suggested values:
3.0, 5.0, 10.0, 15.0, 20.0, 50.0, 100.0, 200.0, 300.0, 500.0

Value range:
`length_1` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`length_2`** (input_control)  rectangle2.hheight(-array) `→` MaybeSequence[Union[int, float]]

Half height.

Default:
20.0

Suggested values:
1.0, 2.0, 3.0, 5.0, 10.0, 15.0, 20.0, 50.0, 100.0, 200.0

Value range:
`length_2` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

## Result

If the parameter values are correct the operator `gen_rectangle2`
returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.
The clipping according to the current image format is set via the
operator `set_system('clip_region',<'true'/'false'>)`.

## Possible Successors

`paint_region`,
`reduce_domain`

## Alternatives

`gen_rectangle1`,
`gen_region_polygon_filled`,
`gen_region_polygon`,
`gen_region_points`,
`fill_up`

## See also

`draw_rectangle2`,
`reduce_domain`,
`smallest_rectangle2`,
`gen_ellipse`

## Module

Foundation
