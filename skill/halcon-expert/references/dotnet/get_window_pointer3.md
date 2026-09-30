# GetWindowPointer3 (Operator)

## Name

`GetWindowPointer3` — Access to a window's pixel data.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`static void HOperatorSet.GetWindowPointer3(HTuple windowHandle, out HTuple imageRed, out HTuple imageGreen, out HTuple imageBlue, out HTuple width, out HTuple height)`

`void HWindow.GetWindowPointer3(out int imageRed, out int imageGreen, out int imageBlue, out int width, out int height)`

## Description

`GetWindowPointer3` enables (in some window systems) the
direct access to the bitmap. Result values are the three pointers on the
color extracts of a 24-bit window (*`imageRed`*, *`imageGreen`*,
*`imageBlue`*), as well as the window size (*`width`*,
*`height`*).
In the language C the type of the image points is unsigned char.

## Attention

`GetWindowPointer3` is usable only for window type
*"pixmap"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`imageRed`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Pointer on red channel of pixel data.

**`imageGreen`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Pointer on green channel of pixel data.

**`imageBlue`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Pointer on blue channel of pixel data.

**`width`** (output_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Length of an image line.

**`height`** (output_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Number of image lines.

## Result

If a window of type *"pixmap"* exists and it is valid
`GetWindowPointer3` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`OpenWindow`

## See also

`OpenWindow`,
`SetWindowType`

## Module

Foundation
