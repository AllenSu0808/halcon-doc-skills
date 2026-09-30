# create_drawing_object_line (Operator)

## Name

`create_drawing_object_line` — Create a line which can be modified interactively.

## Signature

`def create_drawing_object_line(row_1: float, column_1: float, row_2: float, column_2: float) -> HHandle`

## Description

`create_drawing_object_line` creates a line which can be modified interactively
in a HALCON window by the user. The line is defined by the coordinates
of the first line point, *`row_1`* and *`column_1`*, and the
second line point, *`row_2`* and *`column_2`*.

These parameters can be queried any time with [`get_drawing_object_params`](get_drawing_object_params.md),
as well as its corresponding HALCON object with [`get_drawing_object_iconic`](get_drawing_object_iconic.md).

In addition to those parameters, every drawing object has a number of
parameters which determine the appearance of the object in the HALCON window.
See [`set_drawing_object_params`](set_drawing_object_params.md) for details on the number and meaning
of those parameters.

In order to enable the interactive modification with the drawing object, the
object must be attached to an existing window. See
[`attach_drawing_object_to_window`](attach_drawing_object_to_window.md) for further details.
Once attached, the line is editable by the user through interaction
with the window.
There are two possible transformations for a line object: resizing and
displacement.
A line point can be moved by dragging on the point handle. The whole
line can be moved by dragging the center of the line.

In contrast to the operator [`draw_line`](draw_line.md), this interaction does not
block the calling thread.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`row_1`** (input_control)  line.begin.y `→` float

Row coordinate of the first line point.

Default:
100

**`column_1`** (input_control)  line.begin.x `→` float

Column coordinate of the first line point.

Default:
100

**`row_2`** (input_control)  line.end.y `→` float

Row coordinate of the second line point.

Default:
200

**`column_2`** (input_control)  line.end.x `→` float

Column coordinate of the second line point.

Default:
200

**`draw_id`** (output_control)  drawing_object `→` HHandle

Handle of the drawing object.

## Result

If the parameter values are correct the operator
[`create_drawing_object_circle_sector`](create_drawing_object_circle_sector.md) returns the value 2 (
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

`draw_line`,
`draw_line_mod`,
`create_drawing_object_xld`

## See also

`create_drawing_object_rectangle1`,
`create_drawing_object_rectangle2`,
`create_drawing_object_ellipse`,
`create_drawing_object_circle_sector`,
`create_drawing_object_ellipse_sector`,
`create_drawing_object_xld`

## Module

Foundation
