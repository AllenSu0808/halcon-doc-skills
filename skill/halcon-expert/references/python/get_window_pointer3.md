# get_window_pointer3 (Operator)

## Name

`get_window_pointer3` — Access to a window's pixel data.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`def get_window_pointer3(window_handle: HHandle) -> Tuple[int, int, int, int, int]`

## Description

`get_window_pointer3` enables (in some window systems) the
direct access to the bitmap. Result values are the three pointers on the
color extracts of a 24-bit window (*`image_red`*, *`image_green`*,
*`image_blue`*), as well as the window size (*`width`*,
*`height`*).
In the language C the type of the image points is unsigned char.

## Attention

`get_window_pointer3` is usable only for window type
*"pixmap"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`image_red`** (output_control)  integer `→` int

Pointer on red channel of pixel data.

**`image_green`** (output_control)  integer `→` int

Pointer on green channel of pixel data.

**`image_blue`** (output_control)  integer `→` int

Pointer on blue channel of pixel data.

**`width`** (output_control)  extent.x `→` int

Length of an image line.

**`height`** (output_control)  extent.y `→` int

Number of image lines.

## Result

If a window of type *"pixmap"* exists and it is valid
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
