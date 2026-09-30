# send_mouse_down_event (Operator)

## Name

`send_mouse_down_event` — Send an event to a window buffer signaling a mouse down event.

## Signature

`send_mouse_down_event( : : WindowHandle, Row, Column, Button : Processed)`

## Description

`send_mouse_down_event` sends an event
at the position (*`Row`*, *`Column`*) to the buffer window
*`WindowHandle`*, signaling that the mouse button encoded by
*`Button`* has been pressed. Please refer to [`get_mbutton`](get_mbutton.md)
to see how to encode *`Button`*.

The purpose of this operator is to manipulate drawing objects in a
buffer window. If the coordinates *`Row`* and *`Column`*
are pointing on a drawing object, it is activated and can be moved
or changed by sending more events with the `send_mouse_down_event`
operator. To simplify the interaction with the drawing object, the
coordinates *`Row`* and *`Column`* are given in the image
coordinate system. To convert window coordinates into image
coordinates, the operator [`convert_coordinates_window_to_image`](convert_coordinates_window_to_image.md)
can be used.

If the event could be processed, `send_mouse_down_event` returns
*'true'* in *`Processed`*. If no action for the event could be
determined (e.g., because there is no drawing object below the mouse
position), *'false'* is returned in *`Processed`*. In this case
the caller may determine an action for the event.

The operators `send_mouse_down_event`, [`send_mouse_up_event`](send_mouse_up_event.md),
[`send_mouse_drag_event`](send_mouse_drag_event.md) and [`send_mouse_double_click_event`](send_mouse_double_click_event.md) are
the only means to manipulate drawing objects in buffer windows.

## Attention

`send_mouse_down_event` depends on the library libcanvas, which might
not be available on embedded systems.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle of the buffer window.

**`Row`** (input_control)  point.y `→`  (integer / real)

Row coordinate of the mouse cursor in the image
coordinate system.

**`Column`** (input_control)  point.x `→`  (integer / real)

Column coordinate of the mouse cursor in the image
coordinate system.

**`Button`** (input_control)  integer `→`  (integer)

Mouse button(s) pressed.

**`Processed`** (output_control)  string `→`  (string)

'true', if HALCON processed the event.

## Result

`send_mouse_down_event` returns the value 2 (
H_MSG_TRUE)
if the window handle
*`WindowHandle`* corresponds to a window of valid type, and the event
is properly encoded. Otherwise, an exception is raised.

## Possible Predecessors

`open_window`

## See also

`send_mouse_up_event`,
`send_mouse_double_click_event`,
`open_window`

## Module

Foundation
