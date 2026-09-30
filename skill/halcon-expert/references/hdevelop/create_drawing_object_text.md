# create_drawing_object_text (Operator)

## Name

`create_drawing_object_text` — Create a text object which can be moved interactively.

## Signature

`create_drawing_object_text( : : Row, Column, String : DrawID)`

## Description

`create_drawing_object_text` creates a text object which can be moved
interactively across a HALCON window. The coordinates *`Row`* and
*`Column`* define the position of the text.

These parameters can be queried any time with [`get_drawing_object_params`](get_drawing_object_params.md),
as well as its corresponding HALCON object with [`get_drawing_object_iconic`](get_drawing_object_iconic.md).

In addition to those parameters, every drawing object has a number of
parameters which determine the appearance of the object in the HALCON window.
See [`set_drawing_object_params`](set_drawing_object_params.md) for details on the number and meaning
of those parameters.

In order to enable the interactive modification with the drawing object, the
text object must be attached to an existing window. See
[`attach_drawing_object_to_window`](attach_drawing_object_to_window.md) for further details.
The text will be displayed with the current font settings of the HALCON
window by default. However, the font setting can be adjusted with
[`set_drawing_object_params`](set_drawing_object_params.md).
Once attached, the text can be moved by the user through interaction
with the window.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`Row`** (input_control)  point.y `→`  (integer)

Row coordinate of the text position.

Default:
12

**`Column`** (input_control)  point.x `→`  (integer)

Column coordinate of the text position.

Default:
12

**`String`** (input_control)  string `→`  (string)

Character string to be displayed.

Default:
'Text'

**`DrawID`** (output_control)  drawing_object `→`  (handle)

Handle of the drawing object.

## Result

If the parameter values are correct, the operator
`create_drawing_object_text` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`open_window`

## Possible Successors

`attach_drawing_object_to_window`,
`get_drawing_object_params`,
`set_drawing_object_params`

## Alternatives

`write_string`

## See also

`write_string`,
`attach_drawing_object_to_window`

## Module

Foundation
