# set_content_update_callback (Operator)

## Name

`set_content_update_callback` — Sets the callback for content updates in buffer window.

## Signature

`def set_content_update_callback(window_handle: HHandle, callback_function: int, callback_context: Union[int, HHandle]) -> None`

## Description

`set_content_update_callback` sets a callback *`callback_function`*,
which is called whenever the contents of the buffer window
*`window_handle`* change.
The parameter *`callback_context`* is always passed to the
callback.

The type of *`callback_function`* is: Herror callback(void *context)

On Windows systems, the __stdcall calling convention is used:
Herror __stdcall callback(void *context)

The callback function must not call a HALCON operator. Doing so is
undefined behavior. It is advised to perform only computationally
inexpensive tasks in the callback, e.g., setting a flag or triggering an
asynchronous operation.

In combination with the operators [`send_mouse_down_event`](send_mouse_down_event.md),
[`send_mouse_up_event`](send_mouse_up_event.md), and [`send_mouse_double_click_event`](send_mouse_double_click_event.md),
`set_content_update_callback` can be used to create a buffer based
control for a GUI Toolkit (such as Qt), where the control passes mouse
events to the buffer, while the buffer notifies the control on changes by
calling the function *`callback_function`*.
The control then can obtain the contents of the buffer with
[`dump_window_image`](dump_window_image.md) and display them.

## Attention

`set_content_update_callback` depends on the library libcanvas, which
might not be available on embedded systems.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`callback_function`** (input_control)  pointer `→` int

Callback for content updates.

**`callback_context`** (input_control)  pointer `→` Union[int, HHandle]

Parameter to CallbackFunction.

## Result

If the window exists and is a buffer window,
`set_content_update_callback` returns 2 (
H_MSG_TRUE)
.

## See also

`flush_buffer`

## Module

Foundation
