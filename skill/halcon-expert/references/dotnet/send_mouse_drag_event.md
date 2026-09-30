# SendMouseDragEvent (Operator)

## Name

`SendMouseDragEvent` — Send an event to a buffer window signaling a mouse drag event.

## Signature

`static void HOperatorSet.SendMouseDragEvent(HTuple windowHandle, HTuple row, HTuple column, HTuple button, out HTuple processed)`

`string HWindow.SendMouseDragEvent(HTuple row, HTuple column, int button)`

`string HWindow.SendMouseDragEvent(int row, int column, int button)`

`static string HDrawingObject.SendMouseDragEvent(HWindow windowHandle, HTuple row, HTuple column, int button)`

`static string HDrawingObject.SendMouseDragEvent(HWindow windowHandle, int row, int column, int button)`

## Description

`SendMouseDragEvent` sends an event
at the position (*`row`*, *`column`*) to the buffer window
*`windowHandle`*, signaling that the mouse button encoded by
*`button`* is been dragged. Please refer to
[`GetMbutton`](get_mbutton.md) to see how to encode *`button`*.

If the event could be processed, `SendMouseDragEvent` returns
*"true"* in *`processed`*. If no action for the event could be
determined (e.g., because there is no drawing object below the mouse
position), *"false"* is returned in *`processed`*. In this case
the caller may determine an action for the event.

The operators [`SendMouseDownEvent`](send_mouse_down_event.md), [`SendMouseUpEvent`](send_mouse_up_event.md),
`SendMouseDragEvent` and [`SendMouseDoubleClickEvent`](send_mouse_double_click_event.md) are
the only means to manipulate drawing objects in buffer windows.

## Attention

`SendMouseDragEvent` depends on the library libcanvas, which might
not be available on embedded systems.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle of the buffer window.

**`row`** (input_control)  point.y `→` [HTuple](HTuple.md) (*int* / long / double)

Row coordinate of the mouse cursor in the image
coordinate system.

**`column`** (input_control)  point.x `→` [HTuple](HTuple.md) (*int* / long / double)

Column coordinate of the mouse cursor in the image
coordinate system.

**`button`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Mouse button(s) pressed.

**`processed`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

'true', if HALCON processed the event.

## Result

`SendMouseDragEvent` returns the value 2 (
H_MSG_TRUE)
if the window
handle *`windowHandle`* corresponds to a window of valid type, and the
event is properly encoded. Otherwise, an exception is raised.

## Possible Predecessors

`OpenWindow`

## See also

`SendMouseUpEvent`,
`SendMouseDownEvent`,
`SendMouseDoubleClickEvent`,
`OpenWindow`

## Module

Foundation
