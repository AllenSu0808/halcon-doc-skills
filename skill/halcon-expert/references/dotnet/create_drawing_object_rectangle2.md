# CreateDrawingObjectRectangle2 (Operator)

## Name

`CreateDrawingObjectRectangle2` — Create a rectangle of any orientation which can be modified interactively.

## Signature

`static void HOperatorSet.CreateDrawingObjectRectangle2(HTuple row, HTuple column, HTuple phi, HTuple length1, HTuple length2, out HTuple drawID)`

`public HDrawingObject(double row, double column, double phi, double length1, double length2)`

`void HDrawingObject.CreateDrawingObjectRectangle2(double row, double column, double phi, double length1, double length2)`

## Description

`CreateDrawingObjectRectangle2` creates an oriented rectangle which can be
modified interactively in a HALCON window by the user. The rectangle is defined
by the coordinates *`row`* and *`column`* of its center,
its orientation *`phi`*, and the lengths of its half axis,
*`length1`* and *`length2`* respectively. The created rectangle is
returned in the handle *`drawID`*.

These parameters can be queried any time with [`GetDrawingObjectParams`](get_drawing_object_params.md),
as well as its corresponding HALCON object with [`GetDrawingObjectIconic`](get_drawing_object_iconic.md).

In addition to those parameters, every drawing object has a number of
parameters which determine the appearance of the object in the HALCON window.
See [`SetDrawingObjectParams`](set_drawing_object_params.md) for details on the number and meaning
of those parameters.

In order to enable the interactive modification with the drawing object, the
object must be attached to an existing window. See
[`AttachDrawingObjectToWindow`](attach_drawing_object_to_window.md) for further details.
Once attached, the rectangle is editable by the user through interaction
with the window.
There are three possible transformations for a rectangle2 object:
resizing, displacement and rotation.
The rectangle can be moved by dragging its center.
By dragging the side handles, the size of the rectangle can be modified.
The rectangle's orientation can only be changed by gripping a side
perpendicular to the first half axis.

In contrast to the operator [`DrawRectangle2`](draw_rectangle2.md), this interaction does not
block the calling thread.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`row`** (input_control)  rectangle2.center.y `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the center.

Default:
150

**`column`** (input_control)  rectangle2.center.x `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the center.

Default:
150

**`phi`** (input_control)  rectangle2.angle.rad `→` [HTuple](HTuple.md) (*double*)

Orientation of the first half axis in radians.

Default:
0

**`length1`** (input_control)  rectangle2.hwidth `→` [HTuple](HTuple.md) (*double*)

First half axis.

Default:
100

**`length2`** (input_control)  rectangle2.hheight `→` [HTuple](HTuple.md) (*double*)

Second half axis.

Default:
100

**`drawID`** (output_control)  drawing_object `→` [HDrawingObject](HDrawingObject.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the drawing object.

## Result

If the parameter values are correct the operator
`CreateDrawingObjectRectangle2` returns the value 2 (
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

`DrawRectangle2Mod`,
`DrawRectangle2`,
`DrawRegion`

## See also

`GenRectangle2`,
`DrawCircle`,
`DrawEllipse`

## Module

Foundation
