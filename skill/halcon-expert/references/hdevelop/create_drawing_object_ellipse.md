# create_drawing_object_ellipse (Operator)

## Name

`create_drawing_object_ellipse` — Create an ellipse which can be modified interactively.

## Signature

`create_drawing_object_ellipse( : : Row, Column, Phi, Radius1, Radius2 : DrawID)`

## Description

`create_drawing_object_ellipse` creates an ellipse which can be
modified interactively in a HALCON window by the user. The ellipse is defined
by the coordinates of its center point, *`Row`* and *`Column`*,
the lengths of its respective half axis, *`Radius1`* and
*`Radius2`*, and its orientation *`Phi`*.

The parameters can be queried with [`get_drawing_object_params`](get_drawing_object_params.md),
as well as its corresponding HALCON object with [`get_drawing_object_iconic`](get_drawing_object_iconic.md).

In addition to those parameters, every drawing object has a number of
parameters which determine the appearance of the object in the HALCON window.
See [`set_drawing_object_params`](set_drawing_object_params.md) for details on the number and meaning
of those parameters.

In order to enable the interactive modification with the drawing object, the
object must be attached to an existing window. See
[`attach_drawing_object_to_window`](attach_drawing_object_to_window.md) for further details.
Once attached, the ellipse is editable by the user through interaction
with the window.
There are three possible transformations for an ellipse object:
resizing, displacement and rotation.
The ellipse can be resized by clicking close to the vertex handles.
The orientation and thus the rotation of the ellipse can be modified by
dragging on a vertex of the first half axis. The ellipse can be moved in
the HALCON window by dragging the center.

In contrast to the operator [`draw_ellipse`](draw_ellipse.md), this interaction does not
block the calling thread.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`Row`** (input_control)  ellipse.center.y `→`  (real)

Row index of the center.

Default:
200

**`Column`** (input_control)  ellipse.center.x `→`  (real)

Column index of the center.

Default:
200

**`Phi`** (input_control)  ellipse.angle.rad `→`  (real)

Orientation of the first half axis in radians.

Default:
0

**`Radius1`** (input_control)  ellipse.radius1 `→`  (real)

First half axis.

Default:
100

**`Radius2`** (input_control)  ellipse.radius2 `→`  (real)

Second half axis.

Default:
60

**`DrawID`** (output_control)  drawing_object `→`  (handle)

Handle of the drawing object.

## Result

If the parameter values are correct the operator
`create_drawing_object_ellipse` returns the value 2 (
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

`draw_ellipse_mod`,
`draw_ellipse`,
`draw_region`

## See also

`gen_ellipse`,
`draw_circle`,
`draw_rectangle2`

## Module

Foundation
