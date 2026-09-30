# CreateDrawingObjectLine (Operator)

## Name

`CreateDrawingObjectLine` — Create a line which can be modified interactively.

## Signature

`static void HOperatorSet.CreateDrawingObjectLine(HTuple row1, HTuple column1, HTuple row2, HTuple column2, out HTuple drawID)`

`void HDrawingObject.CreateDrawingObjectLine(double row1, double column1, double row2, double column2)`

## Description

`CreateDrawingObjectLine` creates a line which can be modified interactively
in a HALCON window by the user. The line is defined by the coordinates
of the first line point, *`row1`* and *`column1`*, and the
second line point, *`row2`* and *`column2`*.

These parameters can be queried any time with [`GetDrawingObjectParams`](get_drawing_object_params.md),
as well as its corresponding HALCON object with [`GetDrawingObjectIconic`](get_drawing_object_iconic.md).

In addition to those parameters, every drawing object has a number of
parameters which determine the appearance of the object in the HALCON window.
See [`SetDrawingObjectParams`](set_drawing_object_params.md) for details on the number and meaning
of those parameters.

In order to enable the interactive modification with the drawing object, the
object must be attached to an existing window. See
[`AttachDrawingObjectToWindow`](attach_drawing_object_to_window.md) for further details.
Once attached, the line is editable by the user through interaction
with the window.
There are two possible transformations for a line object: resizing and
displacement.
A line point can be moved by dragging on the point handle. The whole
line can be moved by dragging the center of the line.

In contrast to the operator [`DrawLine`](draw_line.md), this interaction does not
block the calling thread.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`row1`** (input_control)  line.begin.y `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the first line point.

Default:
100

**`column1`** (input_control)  line.begin.x `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the first line point.

Default:
100

**`row2`** (input_control)  line.end.y `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the second line point.

Default:
200

**`column2`** (input_control)  line.end.x `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the second line point.

Default:
200

**`drawID`** (output_control)  drawing_object `→` [HDrawingObject](HDrawingObject.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the drawing object.

## Result

If the parameter values are correct the operator
[`CreateDrawingObjectCircleSector`](create_drawing_object_circle_sector.md) returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`OpenWindow`

## Possible Successors

`AttachDrawingObjectToWindow`,
`GetDrawingObjectParams`,
`GetDrawingObjectIconic`

## Alternatives

`DrawLine`,
`DrawLineMod`,
`CreateDrawingObjectXld`

## See also

`CreateDrawingObjectRectangle1`,
`CreateDrawingObjectRectangle2`,
`CreateDrawingObjectEllipse`,
`CreateDrawingObjectCircleSector`,
`CreateDrawingObjectEllipseSector`,
`CreateDrawingObjectXld`

## Module

Foundation
