# SlideImage (Operator)

## Name

`SlideImage` — Interactive output from two window buffers.

## Warning

**The operator `SlideImage` does not work with HDevelop graphics windows.
It is only provided for reasons of backward compatibility.**

## Signature

`static void HOperatorSet.SlideImage(HTuple windowHandleSource1, HTuple windowHandleSource2, HTuple windowHandle)`

`void HWindow.SlideImage(HWindow windowHandleSource2, HWindow windowHandle)`

## Description

`SlideImage` divides the window horizontal in two logical
areas dependent of the mouse position. The content of the first indicated
window is copied in the upper area, the content of the second window is copied
in the lower area. If you press the left mouse button you may scroll the
delimitation between the two areas (you may move the mouse outside the
window, too. In doing so the position of the mouse relative to the
window determines the borderline).

Pressing the right mouse button in the window terminates the operator
`SlideImage`.

A useful application of the operator `SlideImage` might be the
visualization of the effect of a filtering operation for an image.
The output is directed to the currently set window (*`windowHandle`*).

## Attention

The three windows must have the same size and have to reside on the
same computer.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandleSource1`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Source window handle of the “upper window”.

**`windowHandleSource2`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Source window handle of the “lower window”.

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Output window handle.

## Example (HDevelop)

```
read_image (Image, 'fabrik')
sobel_dir (Image, EdgeAmplitude, EdgeDirection, 'sum_abs', 3)
dev_open_window (0, 0, 512, 512, 'black', WindowHandle1)
dev_display (EdgeAmplitude)
dev_open_window (0, 0, 512, 512, 'black', WindowHandle2)
dev_display (EdgeDirection)
dev_open_window (0, 0, 512, 512, 'black', WindowHandle)
slide_image (WindowHandle1, WindowHandle2, WindowHandle)
```

## Result

If the both windows exist and one of these windows is valid
`SlideImage` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`OpenWindow`

## Alternatives

`CopyRectangle`,
`GetMposition`

## See also

`OpenWindow`,
`MoveRectangle`

## Module

Foundation
