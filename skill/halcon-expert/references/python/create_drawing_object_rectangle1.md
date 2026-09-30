# create_drawing_object_rectangle1 (Operator)

## Name

`create_drawing_object_rectangle1` — Create a rectangle parallel to the coordinate axis which can be
modified interactively.

## Signature

`def create_drawing_object_rectangle1(row_1: float, column_1: float, row_2: float, column_2: float) -> HHandle`

## Description

`create_drawing_object_rectangle1` creates a rectangle aligned along the
coordinate axis which can be modified interactively in a HALCON window by the
user. The rectangle is defined by the coordinates *`row_1`*, *`column_1`*,
*`row_2`*, and *`column_2`* of its upper left and lower
right corner. The created rectangle is returned in the
handle *`draw_id`*.

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
There are two possible transformations for a rectangle1 object:
resizing and displacement.
The rectangle can be moved by dragging in the middle of the rectangle
and resized by dragging the handles of the corners.

In contrast to the operator [`draw_rectangle1`](draw_rectangle1.md), this interaction
does not block the calling thread.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`row_1`** (input_control)  rectangle.origin.y `→` float

Row coordinate of the upper left corner.

Default:
100

**`column_1`** (input_control)  rectangle.origin.x `→` float

Column coordinate of the upper left corner.

Default:
100

**`row_2`** (input_control)  rectangle.corner.y `→` float

Row coordinate of the lower right corner.

Default:
200

**`column_2`** (input_control)  rectangle.corner.x `→` float

Column coordinate of the lower right corner.

Default:
200

**`draw_id`** (output_control)  drawing_object `→` HHandle

Handle of the drawing object.

## Result

If the parameter values are correct, the operator
`create_drawing_object_rectangle1` returns the value 2 (
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

`draw_rectangle1_mod`,
`draw_rectangle2`,
`draw_region`

## See also

`gen_rectangle1`,
`draw_circle`,
`draw_ellipse`

## Module

Foundation
