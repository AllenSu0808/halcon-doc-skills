# CreateDrawingObjectRectangle1 (Operator)

## Name

`CreateDrawingObjectRectangle1` — Create a rectangle parallel to the coordinate axis which can be
modified interactively.

## Signature

`static void HOperatorSet.CreateDrawingObjectRectangle1(HTuple row1, HTuple column1, HTuple row2, HTuple column2, out HTuple drawID)`

`public HDrawingObject(double row1, double column1, double row2, double column2)`

`void HDrawingObject.CreateDrawingObjectRectangle1(double row1, double column1, double row2, double column2)`

## Description

`CreateDrawingObjectRectangle1` creates a rectangle aligned along the
coordinate axis which can be modified interactively in a HALCON window by the
user. The rectangle is defined by the coordinates *`row1`*, *`column1`*,
*`row2`*, and *`column2`* of its upper left and lower
right corner. The created rectangle is returned in the
handle *`drawID`*.

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
There are two possible transformations for a rectangle1 object:
resizing and displacement.
The rectangle can be moved by dragging in the middle of the rectangle
and resized by dragging the handles of the corners.

In contrast to the operator [`DrawRectangle1`](draw_rectangle1.md), this interaction
does not block the calling thread.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`row1`** (input_control)  rectangle.origin.y `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the upper left corner.

Default:
100

**`column1`** (input_control)  rectangle.origin.x `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the upper left corner.

Default:
100

**`row2`** (input_control)  rectangle.corner.y `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the lower right corner.

Default:
200

**`column2`** (input_control)  rectangle.corner.x `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the lower right corner.

Default:
200

**`drawID`** (output_control)  drawing_object `→` [HDrawingObject](HDrawingObject.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the drawing object.

## Result

If the parameter values are correct, the operator
`CreateDrawingObjectRectangle1` returns the value 2 (
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

`DrawRectangle1Mod`,
`DrawRectangle2`,
`DrawRegion`

## See also

`GenRectangle1`,
`DrawCircle`,
`DrawEllipse`

## Module

Foundation
