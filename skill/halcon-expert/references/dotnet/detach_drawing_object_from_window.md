# DetachDrawingObjectFromWindow (Operator)

## Name

`DetachDrawingObjectFromWindow` — Detach an existing drawing object from a HALCON window.

## Signature

`static void HOperatorSet.DetachDrawingObjectFromWindow(HTuple windowHandle, HTuple drawHandle)`

`void HWindow.DetachDrawingObjectFromWindow(HDrawingObject drawHandle)`

## Description

This operator can be used to detach the drawing object *`drawHandle`* from
the HALCON window *`windowHandle`* to which it is currently attached.
The drawing object will not longer be displayed in the window.
If a callback function was defined for the drawing object on the
event 'on_detach' or 'on_select' with [`SetDrawingObjectCallback`](set_drawing_object_callback.md) this
will also be called.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window Handle.

**`drawHandle`** (input_control)  drawing_object `→` [HDrawingObject](HDrawingObject.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the drawing object.

## Result

`DetachDrawingObjectFromWindow` returns 2 (
H_MSG_TRUE)
, if the
*`drawHandle`* and *`windowHandle`* are valid. Otherwise an exception
is raised.

## Possible Predecessors

`AttachDrawingObjectToWindow`,
`GetDrawingObjectIconic`,
`GetDrawingObjectParams`

## Possible Successors

`CloseWindow`,
`ClearDrawingObject`

## See also

`AttachDrawingObjectToWindow`

## Module

Foundation
