# SetContentUpdateCallback (Operator)

## Name

`SetContentUpdateCallback` — Sets the callback for content updates in buffer window.

## Signature

`static void HOperatorSet.SetContentUpdateCallback(HTuple windowHandle, HTuple callbackFunction, HTuple callbackContext)`

`void HWindow.SetContentUpdateCallback(IntPtr callbackFunction, HTuple callbackContext)`

`void HWindow.SetContentUpdateCallback(IntPtr callbackFunction, IntPtr callbackContext)`

## Description

`SetContentUpdateCallback` sets a callback *`callbackFunction`*,
which is called whenever the contents of the buffer window
*`windowHandle`* change.
The parameter *`callbackContext`* is always passed to the
callback.

The type of *`callbackFunction`* is: Herror callback(void *context)

On Windows systems, the __stdcall calling convention is used:
Herror __stdcall callback(void *context)

The callback function must not call a HALCON operator. Doing so is
undefined behavior. It is advised to perform only computationally
inexpensive tasks in the callback, e.g., setting a flag or triggering an
asynchronous operation.

In combination with the operators [`SendMouseDownEvent`](send_mouse_down_event.md),
[`SendMouseUpEvent`](send_mouse_up_event.md), and [`SendMouseDoubleClickEvent`](send_mouse_double_click_event.md),
`SetContentUpdateCallback` can be used to create a buffer based
control for a GUI Toolkit (such as Qt), where the control passes mouse
events to the buffer, while the buffer notifies the control on changes by
calling the function *`callbackFunction`*.
The control then can obtain the contents of the buffer with
[`DumpWindowImage`](dump_window_image.md) and display them.

## Attention

`SetContentUpdateCallback` depends on the library libcanvas, which
might not be available on embedded systems.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`callbackFunction`** (input_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Callback for content updates.

**`callbackContext`** (input_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr* / IntPtr)

Parameter to CallbackFunction.

## Result

If the window exists and is a buffer window,
`SetContentUpdateCallback` returns 2 (
H_MSG_TRUE)
.

## See also

`FlushBuffer`

## Module

Foundation
