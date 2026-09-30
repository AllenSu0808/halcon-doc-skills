# flush_buffer (Operator)

## Name

`flush_buffer` — Flush the contents of a window.

## Signature

`def flush_buffer(window_handle: HHandle) -> None`

## Description

`flush_buffer` flushes the contents of the window
*`window_handle`*.

`flush_buffer` is only necessary if the window parameter
*"flush"* has been set to *"false"* with
[`set_window_param`](set_window_param.md). If *"flush"* is *"false"* all
display operations (such as [`disp_obj`](disp_obj.md) or [`disp_text`](disp_text.md)) are
redirected to a buffer and have no effect on *`window_handle`*
(this applies for all window modes). `flush_buffer` copies the
contents of this buffer to the window *`window_handle`*.

This is very useful to avoid flickering by batching several display
operations (e.g., a [`clear_window`](clear_window.md) followed by a [`disp_obj`](disp_obj.md))
and displaying the final result with `flush_buffer`.

This does not apply to drawing objects, which are always updated.

## Attention

`flush_buffer` depends on the library libcanvas, which might not be
available on embedded systems.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

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

If the window exists `flush_buffer` returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`disp_obj`

## Possible Successors

`dump_window_image`

## See also

`set_window_param`

## Module

Foundation
