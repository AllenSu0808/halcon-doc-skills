# CreateDrawingObjectCircleSector (Operator)

## Name

`CreateDrawingObjectCircleSector` — Create a circle sector which can be modified interactively.

## Signature

`static void HOperatorSet.CreateDrawingObjectCircleSector(HTuple row, HTuple column, HTuple radius, HTuple startAngle, HTuple endAngle, out HTuple drawID)`

`void HDrawingObject.CreateDrawingObjectCircleSector(double row, double column, double radius, double startAngle, double endAngle)`

## Description

`CreateDrawingObjectCircleSector` creates a circle sector region which can
be modified interactively in a HALCON window by the user. The circle sector
is defined by the coordinates *`row`* and
*`column`* of the center point, the *`radius`*, and the start and end angle
*`startAngle`* and *`endAngle`*.

These parameters can be queried any time with [`GetDrawingObjectParams`](get_drawing_object_params.md),
as well as its corresponding HALCON object with [`GetDrawingObjectIconic`](get_drawing_object_iconic.md).

In addition to those parameters, every drawing object has a number of
parameters which determine the appearance of the object in the HALCON window.
See [`SetDrawingObjectParams`](set_drawing_object_params.md) for details on the number and meaning
of those parameters.

In order to enable the interactive modification with the drawing object, the
object must be attached to an existing window. See [`AttachDrawingObjectToWindow`](attach_drawing_object_to_window.md)
for further details.
Once attached, the circle is editable by the user through interaction
with the window.
There are three possible transformations for a circle sector object:
resizing, displacement and changing the arc angle.
The *`radius`* of the circle can be modified by dragging the circular arc.
By clicking on the center, the circle sector can be moved across the
HALCON window. The angle arc can be modified by dragging the handles of the
circle sector.

In contrast to the operator [`DrawCircle`](draw_circle.md), this interaction does not block the
calling thread.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`row`** (input_control)  coordinates.y `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the center.

Default:
100

**`column`** (input_control)  coordinates.x `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the center.

Default:
100

**`radius`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Radius of the circle.

Default:
80

**`startAngle`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Start angle of the arc.

Default:
0

**`endAngle`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

End angle of the arc.

Default:
3.14159

**`drawID`** (output_control)  drawing_object `→` [HDrawingObject](HDrawingObject.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the drawing object.

## Result

If the parameter values are correct the operator
`CreateDrawingObjectCircleSector` returns the value 2 (
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

`DrawRectangle1Mod`,
`DrawRectangle2`,
`DrawRegion`,
`CreateDrawingObjectCircle`,
`CreateDrawingObjectEllipseSector`

## See also

`CreateDrawingObjectRectangle1`,
`CreateDrawingObjectRectangle2`,
`CreateDrawingObjectEllipse`,
`CreateDrawingObjectCircle`,
`CreateDrawingObjectEllipseSector`,
`CreateDrawingObjectXld`,
`CreateDrawingObjectLine`

## Module

Foundation
