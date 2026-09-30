# gen_rectangle2_contour_xld (Operator)

## Name

`gen_rectangle2_contour_xld` — Create an XLD contour in the shape of a rectangle.

## Signature

`def gen_rectangle2_contour_xld(row: MaybeSequence[float], column: MaybeSequence[float], phi: MaybeSequence[float], length_1: MaybeSequence[float], length_2: MaybeSequence[float]) -> HObject`

## Description

`gen_rectangle2_contour_xld` creates one or more XLD contours
in the shape of a rectangle with arbitrary orientation. The
rectangle has the center (*`row`*, *`column`*), the
orientation *`phi`*, and the half edge lengths *`length_1`*
and *`length_2`*. The angle *`phi`* must be given in
radians and specifies the angle between the horizontal axis and the
edge with the half length *`length_1`* in the mathematically
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

**`rectangle`** (output_object)  xld_cont(-array) `→` HObject

Rectangle contour.

**`row`** (input_control)  rectangle2.center.y(-array) `→` MaybeSequence[float]

Row coordinate of the center of the rectangle.

Default:
300.0

**`column`** (input_control)  rectangle2.center.x(-array) `→` MaybeSequence[float]

Column coordinate of the center of the rectangle.

Default:
200.0

**`phi`** (input_control)  rectangle2.angle.rad(-array) `→` MaybeSequence[float]

Orientation of the main axis of the rectangle [rad].

Default:
0.0

Restriction:
`- pi / 2 < Phi && Phi <= pi / 2`

**`length_1`** (input_control)  rectangle2.hwidth(-array) `→` MaybeSequence[float]

First radius (half length) of the rectangle.

Default:
100.5

**`length_2`** (input_control)  rectangle2.hheight(-array) `→` MaybeSequence[float]

Second radius (half width) of the rectangle.

Default:
20.5

## Result

`gen_rectangle2_contour_xld` returns 2 (
H_MSG_TRUE)
if all parameter
values are correct. If necessary, an exception is raised.

## Possible Predecessors

`fit_rectangle2_contour_xld`

## Alternatives

`gen_rectangle2`

## See also

`gen_contour_polygon_xld`

## Module

Foundation
