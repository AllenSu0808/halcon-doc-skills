# create_drawing_object_ellipse_sector (Operator)

## Name

`create_drawing_object_ellipse_sector` — Create an elliptic sector which can be modified interactively.

## Signature

`def create_drawing_object_ellipse_sector(row: float, column: float, phi: float, radius_1: float, radius_2: float, start_angle: float, end_angle: float) -> HHandle`

## Description

`create_drawing_object_ellipse_sector` creates an ellipse sector which can be
modified interactively in a HALCON window by the user. The ellipse sector
is defined by the coordinates *`row`* and *`column`* of its center,
the lengths of its respective half axis, *`radius_1`* and
*`radius_2`*, the start and end angles of the arc, *`start_angle`*
and *`end_angle`*, and its orientation *`phi`*.

These parameters can be queried any time with [`get_drawing_object_params`](get_drawing_object_params.md),
as well as its corresponding HALCON object with [`get_drawing_object_iconic`](get_drawing_object_iconic.md).

In addition to those parameters, every drawing object has a number of
parameters which determine the appearance of the object in the HALCON window.
See [`set_drawing_object_params`](set_drawing_object_params.md) for details on the number and meaning
of those parameters.

In order to enable the interactive modification with the drawing object, the
object must be attached to an existing window. See
[`attach_drawing_object_to_window`](attach_drawing_object_to_window.md) for further details.
Once attached, the ellipse sector is editable by the user through interaction
with the window.
There are four possible transformations for an ellipse sector
object: resizing, displacement, rotation, and changing the arc angle.
The ellipse sector can be moved in the HALCON window by dragging the center.
The orientation and thus the rotation of the ellipse sector can also be modified by
dragging on a vertex handle of the first half axis. The size and angles
of the ellipse sector can be modified by dragging close to the vertex handles.

In contrast to the operator [`draw_ellipse`](draw_ellipse.md), this interaction does not
block the calling thread.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`row`** (input_control)  coordinates.y `→` float

Row index of the center.

Default:
200

**`column`** (input_control)  coordinates.x `→` float

Column index of the center.

Default:
200

**`phi`** (input_control)  angle.rad `→` float

Orientation of the first half axis in radians.

Default:
0

**`radius_1`** (input_control)  number `→` float

First half axis.

Default:
100

**`radius_2`** (input_control)  number `→` float

Second half axis.

Default:
60

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
`create_drawing_object_ellipse_sector` returns the value 2 (
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

`draw_ellipse_mod`,
`draw_ellipse`,
`draw_region`,
`create_drawing_object_ellipse`

## See also

`gen_ellipse_contour_xld`,
`create_drawing_object_rectangle1`,
`create_drawing_object_rectangle2`,
`create_drawing_object_ellipse`,
`create_drawing_object_xld`,
`create_drawing_object_line`,
`create_drawing_object_circle`

## Module

Foundation
