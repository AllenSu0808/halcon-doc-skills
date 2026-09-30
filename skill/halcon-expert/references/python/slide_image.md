# slide_image (Operator)

## Name

`slide_image` — Interactive output from two window buffers.

## Warning

**The operator `slide_image` does not work with HDevelop graphics windows.
It is only provided for reasons of backward compatibility.**

## Signature

`def slide_image(window_handle_source_1: HHandle, window_handle_source_2: HHandle, window_handle: HHandle) -> None`

## Description

`slide_image` divides the window horizontal in two logical
areas dependent of the mouse position. The content of the first indicated
window is copied in the upper area, the content of the second window is copied
in the lower area. If you press the left mouse button you may scroll the
delimitation between the two areas (you may move the mouse outside the
window, too. In doing so the position of the mouse relative to the
window determines the borderline).

Pressing the right mouse button in the window terminates the operator
`slide_image`.

A useful application of the operator `slide_image` might be the
visualization of the effect of a filtering operation for an image.
The output is directed to the currently set window (*`window_handle`*).

## Attention

The three windows must have the same size and have to reside on the
same computer.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle_source_1`** (input_control)  window `→` HHandle

Source window handle of the “upper window”.

**`window_handle_source_2`** (input_control)  window `→` HHandle

Source window handle of the “lower window”.

**`window_handle`** (input_control)  window `→` HHandle

Output window handle.

## Result

If the both windows exist and one of these windows is valid
`slide_image` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`open_window`

## Alternatives

`copy_rectangle`,
`get_mposition`

## See also

`open_window`,
`move_rectangle`

## Module

Foundation
