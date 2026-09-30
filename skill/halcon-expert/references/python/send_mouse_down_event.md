# send_mouse_down_event (Operator)

## Name

`send_mouse_down_event` — Send an event to a window buffer signaling a mouse down event.

## Signature

`def send_mouse_down_event(window_handle: HHandle, row: Union[float, int], column: Union[float, int], button: int) -> str`

## Description

`send_mouse_down_event` sends an event
at the position (*`row`*, *`column`*) to the buffer window
*`window_handle`*, signaling that the mouse button encoded by
*`button`* has been pressed. Please refer to [`get_mbutton`](get_mbutton.md)
to see how to encode *`button`*.

The purpose of this operator is to manipulate drawing objects in a
buffer window. If the coordinates *`row`* and *`column`*
are pointing on a drawing object, it is activated and can be moved
or changed by sending more events with the `send_mouse_down_event`
operator. To simplify the interaction with the drawing object, the
coordinates *`row`* and *`column`* are given in the image
coordinate system. To convert window coordinates into image
coordinates, the operator [`convert_coordinates_window_to_image`](convert_coordinates_window_to_image.md)
can be used.

If the event could be processed, `send_mouse_down_event` returns
*"true"* in *`processed`*. If no action for the event could be
determined (e.g., because there is no drawing object below the mouse
position), *"false"* is returned in *`processed`*. In this case
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

**`window_handle`** (input_control)  window `→` HHandle

Window handle of the buffer window.

**`row`** (input_control)  point.y `→` Union[float, int]

Row coordinate of the mouse cursor in the image
coordinate system.

**`column`** (input_control)  point.x `→` Union[float, int]

Column coordinate of the mouse cursor in the image
coordinate system.

**`button`** (input_control)  integer `→` int

Mouse button(s) pressed.

**`processed`** (output_control)  string `→` str

'true', if HALCON processed the event.

## Result

`send_mouse_down_event` returns the value 2 (
H_MSG_TRUE)
if the window handle
*`window_handle`* corresponds to a window of valid type, and the event
is properly encoded. Otherwise, an exception is raised.

## Possible Predecessors

`open_window`

## See also

`send_mouse_up_event`,
`send_mouse_double_click_event`,
`open_window`

## Module

Foundation
