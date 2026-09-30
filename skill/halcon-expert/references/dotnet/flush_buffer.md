# FlushBuffer (Operator)

## Name

`FlushBuffer` — Flush the contents of a window.

## Signature

`static void HOperatorSet.FlushBuffer(HTuple windowHandle)`

`void HWindow.FlushBuffer()`

## Description

`FlushBuffer` flushes the contents of the window
*`windowHandle`*.

`FlushBuffer` is only necessary if the window parameter
*"flush"* has been set to *"false"* with
[`SetWindowParam`](set_window_param.md). If *"flush"* is *"false"* all
display operations (such as [`DispObj`](disp_obj.md) or [`DispText`](disp_text.md)) are
redirected to a buffer and have no effect on *`windowHandle`*
(this applies for all window modes). `FlushBuffer` copies the
contents of this buffer to the window *`windowHandle`*.

This is very useful to avoid flickering by batching several display
operations (e.g., a [`ClearWindow`](clear_window.md) followed by a [`DispObj`](disp_obj.md))
and displaying the final result with `FlushBuffer`.

This does not apply to drawing objects, which are always updated.

## Attention

`FlushBuffer` depends on the library libcanvas, which might not be
available on embedded systems.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

## Example (HDevelop)

```
read_image (Image, 'printer_chip/printer_chip_01')
threshold (Image, Region, 128, 255)
dev_open_window (0, 0, 512, 512, 'black', WindowHandle)
set_window_param (WindowHandle, 'flush', 'false')
dev_display (Image)
dev_display (Region)
disp_text (WindowHandle, 'Result of threshold', 'window', \
           12, 12, 'black', [], [])
* nothing is displayed until flush_buffer is called
flush_buffer (WindowHandle)
```

## Result

If the window exists `FlushBuffer` returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`DispObj`

## Possible Successors

`DumpWindowImage`

## See also

`SetWindowParam`

## Module

Foundation
