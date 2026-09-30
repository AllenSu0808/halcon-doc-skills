# get_window_pointer3 (Operator)

## Name

`get_window_pointer3` — Access to a window's pixel data.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`get_window_pointer3( : : WindowHandle : ImageRed, ImageGreen, ImageBlue, Width, Height)`

## Description

`get_window_pointer3` enables (in some window systems) the
direct access to the bitmap. Result values are the three pointers on the
color extracts of a 24-bit window (*`ImageRed`*, *`ImageGreen`*,
*`ImageBlue`*), as well as the window size (*`Width`*,
*`Height`*).
In the language C the type of the image points is unsigned char.

## Attention

`get_window_pointer3` is usable only for window type
*'pixmap'*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`ImageRed`** (output_control)  integer `→`  (integer)

Pointer on red channel of pixel data.

**`ImageGreen`** (output_control)  integer `→`  (integer)

Pointer on green channel of pixel data.

**`ImageBlue`** (output_control)  integer `→`  (integer)

Pointer on blue channel of pixel data.

**`Width`** (output_control)  extent.x `→`  (integer)

Length of an image line.

**`Height`** (output_control)  extent.y `→`  (integer)

Number of image lines.

## Result

If a window of type *'pixmap'* exists and it is valid
`get_window_pointer3` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`open_window`

## See also

`open_window`,
`set_window_type`

## Module

Foundation
