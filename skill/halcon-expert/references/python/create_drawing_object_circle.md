# create_drawing_object_circle (Operator)

## Name

`create_drawing_object_circle` — Create a circle which can be modified interactively.

## Signature

`def create_drawing_object_circle(row: float, column: float, radius: float) -> HHandle`

## Description

`create_drawing_object_circle` creates a circular region which can be
interactively modified in a HALCON window by the user. The circle is defined
by the coordinates *`row`* and *`column`* of its center, and
by its *`radius`*. The created circle is returned in the handle
*`draw_id`*.

These parameters can be queried any time with [`get_drawing_object_params`](get_drawing_object_params.md),
as well as its corresponding HALCON object with [`get_drawing_object_iconic`](get_drawing_object_iconic.md).

In addition to those parameters, every drawing object has a number of
parameters which determine the appearance of the object in the HALCON window.
See [`set_drawing_object_params`](set_drawing_object_params.md) for details on the number and meaning
of those parameters.

In order to enable the interactive modification with the drawing object, the
object must be attached to an existing window. See [`attach_drawing_object_to_window`](attach_drawing_object_to_window.md)
for further details. Once attached, the circle is editable by the user
through interaction within the window.
There are two possible transformations for a circle object: resizing and displacement.
By clicking close to the circular arc you can modify the *`radius`* of
the circle. By clicking on the center, the circle can be dragged
across the HALCON window.

In contrast to the operator [`draw_circle`](draw_circle.md), this interaction does not
block the calling thread.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`row`** (input_control)  circle.center.y `→` float

Row coordinate of the center.

Default:
100

**`column`** (input_control)  circle.center.x `→` float

Column coordinate of the center.

Default:
100

**`radius`** (input_control)  circle.radius `→` float

Radius of the circle.

Default:
80

**`draw_id`** (output_control)  drawing_object `→` HHandle

Handle of the drawing object.

## Result

If the parameter values are correct the operator `create_drawing_object_circle`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`open_window`

## Possible Successors

`attach_drawing_object_to_window`,
`get_drawing_object_params`,
`get_drawing_object_iconic`

## Alternatives

`draw_circle`,
`draw_region`,
`create_drawing_object_circle_sector`,
`create_drawing_object_ellipse`,
`create_drawing_object_ellipse_sector`

## See also

`create_drawing_object_rectangle1`,
`create_drawing_object_rectangle2`,
`create_drawing_object_ellipse`,
`create_drawing_object_circle_sector`,
`create_drawing_object_ellipse_sector`,
`create_drawing_object_xld`

## Module

Foundation
