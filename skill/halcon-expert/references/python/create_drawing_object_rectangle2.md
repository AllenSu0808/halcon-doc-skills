# create_drawing_object_rectangle2 (Operator)

## Name

`create_drawing_object_rectangle2` — Create a rectangle of any orientation which can be modified interactively.

## Signature

`def create_drawing_object_rectangle2(row: float, column: float, phi: float, length_1: float, length_2: float) -> HHandle`

## Description

`create_drawing_object_rectangle2` creates an oriented rectangle which can be
modified interactively in a HALCON window by the user. The rectangle is defined
by the coordinates *`row`* and *`column`* of its center,
its orientation *`phi`*, and the lengths of its half axis,
*`length_1`* and *`length_2`* respectively. The created rectangle is
returned in the handle *`draw_id`*.

These parameters can be queried any time with [`get_drawing_object_params`](get_drawing_object_params.md),
as well as its corresponding HALCON object with [`get_drawing_object_iconic`](get_drawing_object_iconic.md).

In addition to those parameters, every drawing object has a number of
parameters which determine the appearance of the object in the HALCON window.
See [`set_drawing_object_params`](set_drawing_object_params.md) for details on the number and meaning
of those parameters.

In order to enable the interactive modification with the drawing object, the
object must be attached to an existing window. See
[`attach_drawing_object_to_window`](attach_drawing_object_to_window.md) for further details.
Once attached, the rectangle is editable by the user through interaction
with the window.
There are three possible transformations for a rectangle2 object:
resizing, displacement and rotation.
The rectangle can be moved by dragging its center.
By dragging the side handles, the size of the rectangle can be modified.
The rectangle's orientation can only be changed by gripping a side
perpendicular to the first half axis.

In contrast to the operator [`draw_rectangle2`](draw_rectangle2.md), this interaction does not
block the calling thread.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`row`** (input_control)  rectangle2.center.y `→` float

Row coordinate of the center.

Default:
150

**`column`** (input_control)  rectangle2.center.x `→` float

Column coordinate of the center.

Default:
150

**`phi`** (input_control)  rectangle2.angle.rad `→` float

Orientation of the first half axis in radians.

Default:
0

**`length_1`** (input_control)  rectangle2.hwidth `→` float

First half axis.

Default:
100

**`length_2`** (input_control)  rectangle2.hheight `→` float

Second half axis.

Default:
100

**`draw_id`** (output_control)  drawing_object `→` HHandle

Handle of the drawing object.

## Result

If the parameter values are correct the operator
`create_drawing_object_rectangle2` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`open_window`

## Possible Successors

`disp_region`,
`set_colored`,
`set_line_width`,
`set_draw`,
`attach_drawing_object_to_window`

## Alternatives

`draw_rectangle2_mod`,
`draw_rectangle2`,
`draw_region`

## See also

`gen_rectangle2`,
`draw_circle`,
`draw_ellipse`

## Module

Foundation
