# CreateDrawingObjectCircle (Operator)

## Name

`CreateDrawingObjectCircle` — Create a circle which can be modified interactively.

## Signature

`static void HOperatorSet.CreateDrawingObjectCircle(HTuple row, HTuple column, HTuple radius, out HTuple drawID)`

`public HDrawingObject(double row, double column, double radius)`

`void HDrawingObject.CreateDrawingObjectCircle(double row, double column, double radius)`

## Description

`CreateDrawingObjectCircle` creates a circular region which can be
interactively modified in a HALCON window by the user. The circle is defined
by the coordinates *`row`* and *`column`* of its center, and
by its *`radius`*. The created circle is returned in the handle
*`drawID`*.

These parameters can be queried any time with [`GetDrawingObjectParams`](get_drawing_object_params.md),
as well as its corresponding HALCON object with [`GetDrawingObjectIconic`](get_drawing_object_iconic.md).

In addition to those parameters, every drawing object has a number of
parameters which determine the appearance of the object in the HALCON window.
See [`SetDrawingObjectParams`](set_drawing_object_params.md) for details on the number and meaning
of those parameters.

In order to enable the interactive modification with the drawing object, the
object must be attached to an existing window. See [`AttachDrawingObjectToWindow`](attach_drawing_object_to_window.md)
for further details. Once attached, the circle is editable by the user
through interaction within the window.
There are two possible transformations for a circle object: resizing and displacement.
By clicking close to the circular arc you can modify the *`radius`* of
the circle. By clicking on the center, the circle can be dragged
across the HALCON window.

In contrast to the operator [`DrawCircle`](draw_circle.md), this interaction does not
block the calling thread.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`row`** (input_control)  circle.center.y `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the center.

Default:
100

**`column`** (input_control)  circle.center.x `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the center.

Default:
100

**`radius`** (input_control)  circle.radius `→` [HTuple](HTuple.md) (*double*)

Radius of the circle.

Default:
80

**`drawID`** (output_control)  drawing_object `→` [HDrawingObject](HDrawingObject.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the drawing object.

## Result

If the parameter values are correct the operator `CreateDrawingObjectCircle`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`OpenWindow`

## Possible Successors

`AttachDrawingObjectToWindow`,
`GetDrawingObjectParams`,
`GetDrawingObjectIconic`

## Alternatives

`DrawCircle`,
`DrawRegion`,
`CreateDrawingObjectCircleSector`,
`CreateDrawingObjectEllipse`,
`CreateDrawingObjectEllipseSector`

## See also

`CreateDrawingObjectRectangle1`,
`CreateDrawingObjectRectangle2`,
`CreateDrawingObjectEllipse`,
`CreateDrawingObjectCircleSector`,
`CreateDrawingObjectEllipseSector`,
`CreateDrawingObjectXld`

## Module

Foundation
