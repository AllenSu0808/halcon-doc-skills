# get_pixel (Operator)

## Name

`get_pixel` — Get the current color lookup table index.

## Warning

**`get_pixel` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def get_pixel(window_handle: HHandle) -> Sequence[int]`

## Description

`get_pixel` returns the internal coding of the output
gray value or color, respectively, for the window. If the output mode is
set to color(s) or gray value(s) (see [`set_color`](set_color.md) or
[`set_gray`](set_gray.md)), then the color- or gray values are transformed
for internal use. The internal code is then used for (physical)
screen display. The transformation depends on the mapping
characteristics and the condition of the output device and can be
different in different program runs. Don't confuse the term “pixel”
with the term “pixel” in image processing (the other operator
is [`get_grayval`](get_grayval.md)). Here a pixel is meant to be the
color lookup table index.

With `get_pixel` it is possible to save the output mode
without knowing whether colors or gray values are
used. *`pixel`* is set with the operator
[`set_pixel`](set_pixel.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`pixel`** (output_control)  integer-array `→` Sequence[int]

Index of the current color look-up table.

## Result

[`get_part_style`](get_part_style.md) returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`set_pixel`,
`disp_region`,
`disp_image`

## See also

`set_pixel`

## Module

Foundation
