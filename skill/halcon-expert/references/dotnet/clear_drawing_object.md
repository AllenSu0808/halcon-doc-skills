# ClearDrawingObject (Operator)

## Name

`ClearDrawingObject` — Delete drawing object.

## Signature

`static void HOperatorSet.ClearDrawingObject(HTuple drawID)`

`void HDrawingObject.ClearDrawingObject()`

## Description

This operator deletes the drawing object *`drawID`*.
The object is automatically detached from the windows to which it had been
previously attached. After calling `ClearDrawingObject` the draw
object can no longer be used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- drawID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`drawID`** (input_control, state is modified)  drawing_object `→` [HDrawingObject](HDrawingObject.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the drawing object.

## Result

`ClearDrawingObject` returns 2 (
H_MSG_TRUE)
if the *`drawID`* is valid.
Otherwise an exception is raised.

## Possible Predecessors

`CreateDrawingObjectRectangle1`,
`CreateDrawingObjectRectangle2`,
`CreateDrawingObjectEllipse`,
`CreateDrawingObjectCircleSector`,
`CreateDrawingObjectEllipseSector`,
`CreateDrawingObjectXld`,
`CreateDrawingObjectLine`,
`CreateDrawingObjectCircle`,
`CreateDrawingObjectText`,
`DetachDrawingObjectFromWindow`,
`AttachDrawingObjectToWindow`

## Possible Successors

`ClearWindow`,
`CloseWindow`

## See also

`CreateDrawingObjectRectangle1`,
`CreateDrawingObjectRectangle2`,
`CreateDrawingObjectEllipse`,
`CreateDrawingObjectCircleSector`,
`CreateDrawingObjectEllipseSector`,
`CreateDrawingObjectXld`,
`CreateDrawingObjectLine`,
`CreateDrawingObjectCircle`,
`CreateDrawingObjectText`

## Module

Foundation
