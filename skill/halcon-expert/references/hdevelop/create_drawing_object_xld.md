# create_drawing_object_xld (Operator)

## Name

`create_drawing_object_xld` — Create a XLD contour which can be modified interactively.

## Signature

`create_drawing_object_xld( : : Row, Column : DrawID)`

## Description

`create_drawing_object_xld` creates an XLD contour which can be modified
interactively in a HALCON window by the user. The contour is defined by the
coordinates *`Row`* and *`Column`* of its points.

These parameters can be queried any time with [`get_drawing_object_params`](get_drawing_object_params.md),
as well as its corresponding HALCON object with [`get_drawing_object_iconic`](get_drawing_object_iconic.md).

In addition to those parameters, every drawing object has a number of
parameters which determine the appearance of the object in the HALCON window.
See [`set_drawing_object_params`](set_drawing_object_params.md) for details on the number and meaning
of those parameters.

In order to enable the interactive modification with the drawing object, the
object must be attached to an existing window. See
[`attach_drawing_object_to_window`](attach_drawing_object_to_window.md) for further details.
Once attached, the contour is editable by the user through interaction
with the window.
Further points can be added by left clicking on the window.
When clicking the contour segment between two consecutive points,
a new point is added between those points.
Each contour point can be moved by dragging its point handle.
A single contour point can be deleted by dragging it over one of the
neighboring contour points directly connected to it.
The contour can be closed by moving the last point onto the first
contour point. The contour can be moved as a whole by dragging it by the
handle in the center.
In addition, it is possible to assign a new contour to a drawing object with
[`set_drawing_object_xld`](set_drawing_object_xld.md).

In contrast to the operator [`draw_xld`](draw_xld.md), this interaction does not block
the calling thread.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`Row`** (input_control)  coordinates.y-array `→`  (real / integer)

Row coordinates of the polygon.

Default:
[100,200,200,100]

Suggested values:
0, 10, 20, 50, 100, 200, 500

**`Column`** (input_control)  coordinates.x-array `→`  (real / integer)

Column coordinates of the polygon.

Default:
[100,100,200,200]

Suggested values:
0, 10, 20, 50, 100, 200, 500

**`DrawID`** (output_control)  drawing_object `→`  (handle)

Handle of the drawing object.

## Result

If the parameter values are correct the operator
`create_drawing_object_xld` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`open_window`

## Possible Successors

`attach_drawing_object_to_window`,
`get_drawing_object_params`,
`get_drawing_object_iconic`,
`set_drawing_object_xld`

## Alternatives

`draw_xld`,
`draw_xld_mod`,
`draw_region`

## See also

`create_drawing_object_rectangle1`,
`create_drawing_object_rectangle2`,
`create_drawing_object_ellipse`,
`create_drawing_object_circle_sector`,
`create_drawing_object_ellipse_sector`,
`create_drawing_object_line`,
`create_drawing_object_circle`

## Module

Foundation
