# CreateDrawingObjectXld (Operator)

## Name

`CreateDrawingObjectXld` — Create a XLD contour which can be modified interactively.

## Signature

`static void HOperatorSet.CreateDrawingObjectXld(HTuple row, HTuple column, out HTuple drawID)`

`void HDrawingObject.CreateDrawingObjectXld(HTuple row, HTuple column)`

## Description

`CreateDrawingObjectXld` creates an XLD contour which can be modified
interactively in a HALCON window by the user. The contour is defined by the
coordinates *`row`* and *`column`* of its points.

These parameters can be queried any time with [`GetDrawingObjectParams`](get_drawing_object_params.md),
as well as its corresponding HALCON object with [`GetDrawingObjectIconic`](get_drawing_object_iconic.md).

In addition to those parameters, every drawing object has a number of
parameters which determine the appearance of the object in the HALCON window.
See [`SetDrawingObjectParams`](set_drawing_object_params.md) for details on the number and meaning
of those parameters.

In order to enable the interactive modification with the drawing object, the
object must be attached to an existing window. See
[`AttachDrawingObjectToWindow`](attach_drawing_object_to_window.md) for further details.
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
[`SetDrawingObjectXld`](set_drawing_object_xld.md).

In contrast to the operator [`DrawXld`](draw_xld.md), this interaction does not block
the calling thread.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`row`** (input_control)  coordinates.y-array `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of the polygon.

Default:
[100,200,200,100]

Suggested values:
0, 10, 20, 50, 100, 200, 500

**`column`** (input_control)  coordinates.x-array `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of the polygon.

Default:
[100,100,200,200]

Suggested values:
0, 10, 20, 50, 100, 200, 500

**`drawID`** (output_control)  drawing_object `→` [HDrawingObject](HDrawingObject.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the drawing object.

## Result

If the parameter values are correct the operator
`CreateDrawingObjectXld` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`OpenWindow`

## Possible Successors

`AttachDrawingObjectToWindow`,
`GetDrawingObjectParams`,
`GetDrawingObjectIconic`,
`SetDrawingObjectXld`

## Alternatives

`DrawXld`,
`DrawXldMod`,
`DrawRegion`

## See also

`CreateDrawingObjectRectangle1`,
`CreateDrawingObjectRectangle2`,
`CreateDrawingObjectEllipse`,
`CreateDrawingObjectCircleSector`,
`CreateDrawingObjectEllipseSector`,
`CreateDrawingObjectLine`,
`CreateDrawingObjectCircle`

## Module

Foundation
