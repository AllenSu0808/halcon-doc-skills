# CreateDrawingObjectEllipse (Operator)

## Name

`CreateDrawingObjectEllipse` — Create an ellipse which can be modified interactively.

## Signature

`static void HOperatorSet.CreateDrawingObjectEllipse(HTuple row, HTuple column, HTuple phi, HTuple radius1, HTuple radius2, out HTuple drawID)`

`void HDrawingObject.CreateDrawingObjectEllipse(double row, double column, double phi, double radius1, double radius2)`

## Description

`CreateDrawingObjectEllipse` creates an ellipse which can be
modified interactively in a HALCON window by the user. The ellipse is defined
by the coordinates of its center point, *`row`* and *`column`*,
the lengths of its respective half axis, *`radius1`* and
*`radius2`*, and its orientation *`phi`*.

The parameters can be queried with [`GetDrawingObjectParams`](get_drawing_object_params.md),
as well as its corresponding HALCON object with [`GetDrawingObjectIconic`](get_drawing_object_iconic.md).

In addition to those parameters, every drawing object has a number of
parameters which determine the appearance of the object in the HALCON window.
See [`SetDrawingObjectParams`](set_drawing_object_params.md) for details on the number and meaning
of those parameters.

In order to enable the interactive modification with the drawing object, the
object must be attached to an existing window. See
[`AttachDrawingObjectToWindow`](attach_drawing_object_to_window.md) for further details.
Once attached, the ellipse is editable by the user through interaction
with the window.
There are three possible transformations for an ellipse object:
resizing, displacement and rotation.
The ellipse can be resized by clicking close to the vertex handles.
The orientation and thus the rotation of the ellipse can be modified by
dragging on a vertex of the first half axis. The ellipse can be moved in
the HALCON window by dragging the center.

In contrast to the operator [`DrawEllipse`](draw_ellipse.md), this interaction does not
block the calling thread.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`row`** (input_control)  ellipse.center.y `→` [HTuple](HTuple.md) (*double*)

Row index of the center.

Default:
200

**`column`** (input_control)  ellipse.center.x `→` [HTuple](HTuple.md) (*double*)

Column index of the center.

Default:
200

**`phi`** (input_control)  ellipse.angle.rad `→` [HTuple](HTuple.md) (*double*)

Orientation of the first half axis in radians.

Default:
0

**`radius1`** (input_control)  ellipse.radius1 `→` [HTuple](HTuple.md) (*double*)

First half axis.

Default:
100

**`radius2`** (input_control)  ellipse.radius2 `→` [HTuple](HTuple.md) (*double*)

Second half axis.

Default:
60

**`drawID`** (output_control)  drawing_object `→` [HDrawingObject](HDrawingObject.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the drawing object.

## Result

If the parameter values are correct the operator
`CreateDrawingObjectEllipse` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`OpenWindow`

## Possible Successors

`DispRegion`,
`SetColored`,
`SetLineWidth`,
`SetDraw`,
`AttachDrawingObjectToWindow`

## Alternatives

`DrawEllipseMod`,
`DrawEllipse`,
`DrawRegion`

## See also

`GenEllipse`,
`DrawCircle`,
`DrawRectangle2`

## Module

Foundation
