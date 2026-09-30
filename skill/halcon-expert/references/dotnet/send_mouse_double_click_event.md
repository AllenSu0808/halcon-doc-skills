# SendMouseDoubleClickEvent (Operator)

## Name

`SendMouseDoubleClickEvent` — Send an event to a buffer window signaling a mouse double click event.

## Signature

`static void HOperatorSet.SendMouseDoubleClickEvent(HTuple windowHandle, HTuple row, HTuple column, HTuple button, out HTuple processed)`

`string HWindow.SendMouseDoubleClickEvent(HTuple row, HTuple column, int button)`

`string HWindow.SendMouseDoubleClickEvent(int row, int column, int button)`

`static string HDrawingObject.SendMouseDoubleClickEvent(HWindow windowHandle, HTuple row, HTuple column, int button)`

`static string HDrawingObject.SendMouseDoubleClickEvent(HWindow windowHandle, int row, int column, int button)`

## Description

`SendMouseDoubleClickEvent` sends an event
at the position (*`row`*, *`column`*) to the buffer window
*`windowHandle`*, signaling that the mouse button encoded by
*`button`* has been double clicked. Please refer to
[`GetMbutton`](get_mbutton.md) to see how to encode *`button`*.

The purpose of this operator is to select a drawing object in a
situation where multiple drawing objects are stacked on top of each
other in a buffer window. If the double click happens on either one
of the markers of the object border of the active object the object
below is selected. To simplify the interaction with the drawing
object, the coordinates *`row`* and *`column`* are given in
the image coordinate system. To convert window coordinates into
image coordinates, the operator
[`ConvertCoordinatesWindowToImage`](convert_coordinates_window_to_image.md) can be used.

If the event could be processed, `SendMouseDoubleClickEvent` returns
*"true"* in *`processed`*. If no action for the event could be
determined (e.g., because there is no drawing object below the mouse
position), *"false"* is returned in *`processed`*. In this case
the caller may determine an action for the event.

The operators [`SendMouseDownEvent`](send_mouse_down_event.md), [`SendMouseUpEvent`](send_mouse_up_event.md),
[`SendMouseDragEvent`](send_mouse_drag_event.md) and `SendMouseDoubleClickEvent` are
the only means to manipulate drawing objects in buffer windows.

## Attention

`SendMouseDoubleClickEvent` depends on the library libcanvas, which
might not be available on embedded systems.

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

`SendMouseDoubleClickEvent` returns the value 2 (
H_MSG_TRUE)
if the window handle
*`windowHandle`* corresponds to a window of valid type, and the event
is properly encoded. Otherwise, an exception is raised.

## Possible Predecessors

`OpenWindow`

## See also

`SendMouseUpEvent`,
`SendMouseDownEvent`,
`OpenWindow`

## Module

Foundation
