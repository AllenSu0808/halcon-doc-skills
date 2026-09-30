# detach_drawing_object_from_window (Operator)

## Name

`detach_drawing_object_from_window` — Detach an existing drawing object from a HALCON window.

## Signature

`detach_drawing_object_from_window( : : WindowHandle, DrawHandle : )`

## Description

This operator can be used to detach the drawing object *`DrawHandle`* from
the HALCON window *`WindowHandle`* to which it is currently attached.
The drawing object will not longer be displayed in the window.
If a callback function was defined for the drawing object on the
event 'on_detach' or 'on_select' with [`set_drawing_object_callback`](set_drawing_object_callback.md) this
will also be called.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window Handle.

**`DrawHandle`** (input_control)  drawing_object `→`  (handle)

Handle of the drawing object.

## Result

`detach_drawing_object_from_window` returns 2 (
H_MSG_TRUE)
, if the
*`DrawHandle`* and *`WindowHandle`* are valid. Otherwise an exception
is raised.

## Possible Predecessors

`attach_drawing_object_to_window`,
`get_drawing_object_iconic`,
`get_drawing_object_params`

## Possible Successors

`close_window`,
`clear_drawing_object`

## See also

`attach_drawing_object_to_window`

## Module

Foundation
