# create_drawing_object_circle_sector (Operator)

## Name

`create_drawing_object_circle_sector` — Create a circle sector which can be modified interactively.

## Signature

`def create_drawing_object_circle_sector(row: float, column: float, radius: float, start_angle: float, end_angle: float) -> HHandle`

## Description

`create_drawing_object_circle_sector` creates a circle sector region which can
be modified interactively in a HALCON window by the user. The circle sector
is defined by the coordinates *`row`* and
*`column`* of the center point, the *`radius`*, and the start and end angle
*`start_angle`* and *`end_angle`*.

These parameters can be queried any time with [`get_drawing_object_params`](get_drawing_object_params.md),
as well as its corresponding HALCON object with [`get_drawing_object_iconic`](get_drawing_object_iconic.md).

In addition to those parameters, every drawing object has a number of
parameters which determine the appearance of the object in the HALCON window.
See [`set_drawing_object_params`](set_drawing_object_params.md) for details on the number and meaning
of those parameters.

In order to enable the interactive modification with the drawing object, the
object must be attached to an existing window. See [`attach_drawing_object_to_window`](attach_drawing_object_to_window.md)
for further details.
Once attached, the circle is editable by the user through interaction
with the window.
There are three possible transformations for a circle sector object:
resizing, displacement and changing the arc angle.
The *`radius`* of the circle can be modified by dragging the circular arc.
By clicking on the center, the circle sector can be moved across the
HALCON window. The angle arc can be modified by dragging the handles of the
circle sector.

In contrast to the operator [`draw_circle`](draw_circle.md), this interaction does not block the
calling thread.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`row`** (input_control)  coordinates.y `→` float

Row coordinate of the center.

Default:
100

**`column`** (input_control)  coordinates.x `→` float

Column coordinate of the center.

Default:
100

**`radius`** (input_control)  number `→` float

Radius of the circle.

Default:
80

**`start_angle`** (input_control)  angle.rad `→` float

Start angle of the arc.

Default:
0

**`end_angle`** (input_control)  angle.rad `→` float

End angle of the arc.

Default:
3.14159

**`draw_id`** (output_control)  drawing_object `→` HHandle

Handle of the drawing object.

## Result

If the parameter values are correct the operator
`create_drawing_object_circle_sector` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`open_window`

## Possible Successors

`attach_drawing_object_to_window`,
`get_drawing_object_params`,
`get_drawing_object_iconic`

## Alternatives

`draw_rectangle1_mod`,
`draw_rectangle2`,
`draw_region`,
`create_drawing_object_circle`,
`create_drawing_object_ellipse_sector`

## See also

`create_drawing_object_rectangle1`,
`create_drawing_object_rectangle2`,
`create_drawing_object_ellipse`,
`create_drawing_object_circle`,
`create_drawing_object_ellipse_sector`,
`create_drawing_object_xld`,
`create_drawing_object_line`

## Module

Foundation
