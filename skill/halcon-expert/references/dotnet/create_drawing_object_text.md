# CreateDrawingObjectText (Operator)

## Name

`CreateDrawingObjectText` — Create a text object which can be moved interactively.

## Signature

`static void HOperatorSet.CreateDrawingObjectText(HTuple row, HTuple column, HTuple stringVal, out HTuple drawID)`

`void HDrawingObject.CreateDrawingObjectText(int row, int column, string stringVal)`

## Description

`CreateDrawingObjectText` creates a text object which can be moved
interactively across a HALCON window. The coordinates *`row`* and
*`column`* define the position of the text.

These parameters can be queried any time with [`GetDrawingObjectParams`](get_drawing_object_params.md),
as well as its corresponding HALCON object with [`GetDrawingObjectIconic`](get_drawing_object_iconic.md).

In addition to those parameters, every drawing object has a number of
parameters which determine the appearance of the object in the HALCON window.
See [`SetDrawingObjectParams`](set_drawing_object_params.md) for details on the number and meaning
of those parameters.

In order to enable the interactive modification with the drawing object, the
text object must be attached to an existing window. See
[`AttachDrawingObjectToWindow`](attach_drawing_object_to_window.md) for further details.
The text will be displayed with the current font settings of the HALCON
window by default. However, the font setting can be adjusted with
[`SetDrawingObjectParams`](set_drawing_object_params.md).
Once attached, the text can be moved by the user through interaction
with the window.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`row`** (input_control)  point.y `→` [HTuple](HTuple.md) (*int* / long)

Row coordinate of the text position.

Default:
12

**`column`** (input_control)  point.x `→` [HTuple](HTuple.md) (*int* / long)

Column coordinate of the text position.

Default:
12

**`stringVal`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Character string to be displayed.

Default:
"Text"

**`drawID`** (output_control)  drawing_object `→` [HDrawingObject](HDrawingObject.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the drawing object.

## Result

If the parameter values are correct, the operator
`CreateDrawingObjectText` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`OpenWindow`

## Possible Successors

`AttachDrawingObjectToWindow`,
`GetDrawingObjectParams`,
`SetDrawingObjectParams`

## Alternatives

`WriteString`

## See also

`WriteString`,
`AttachDrawingObjectToWindow`

## Module

Foundation
