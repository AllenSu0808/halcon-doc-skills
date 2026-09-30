# create_drawing_object_ellipse_sector (Operator)

## Name

`create_drawing_object_ellipse_sector` — Create an elliptic sector which can be modified interactively.

## Signature

`create_drawing_object_ellipse_sector( : : Row, Column, Phi, Radius1, Radius2, StartAngle, EndAngle : DrawID)`

## Description

`create_drawing_object_ellipse_sector` creates an ellipse sector which can be
modified interactively in a HALCON window by the user. The ellipse sector
is defined by the coordinates *`Row`* and *`Column`* of its center,
the lengths of its respective half axis, *`Radius1`* and
*`Radius2`*, the start and end angles of the arc, *`StartAngle`*
and *`EndAngle`*, and its orientation *`Phi`*.

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

**`Row`** (input_control)  coordinates.y `→`  (real)

Row index of the center.

Default:
200

**`Column`** (input_control)  coordinates.x `→`  (real)

Column index of the center.

Default:
200

**`Phi`** (input_control)  angle.rad `→`  (real)

Orientation of the first half axis in radians.

Default:
0

**`Radius1`** (input_control)  number `→`  (real)

First half axis.

Default:
100

**`Radius2`** (input_control)  number `→`  (real)

Second half axis.

Default:
60

**`StartAngle`** (input_control)  angle.rad `→`  (real)

Start angle of the arc.

Default:
0

**`EndAngle`** (input_control)  angle.rad `→`  (real)

End angle of the arc.

Default:
3.14159

**`DrawID`** (output_control)  drawing_object `→`  (handle)

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
