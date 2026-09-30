# GetPixel (Operator)

## Name

`GetPixel` — Get the current color lookup table index.

## Warning

**`GetPixel` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.GetPixel(HTuple windowHandle, out HTuple pixel)`

`HTuple HWindow.GetPixel()`

## Description

`GetPixel` returns the internal coding of the output
gray value or color, respectively, for the window. If the output mode is
set to color(s) or gray value(s) (see [`SetColor`](set_color.md) or
[`SetGray`](set_gray.md)), then the color- or gray values are transformed
for internal use. The internal code is then used for (physical)
screen display. The transformation depends on the mapping
characteristics and the condition of the output device and can be
different in different program runs. Don't confuse the term “pixel”
with the term “pixel” in image processing (the other operator
is [`GetGrayval`](get_grayval.md)). Here a pixel is meant to be the
color lookup table index.

With `GetPixel` it is possible to save the output mode
without knowing whether colors or gray values are
used. *`pixel`* is set with the operator
[`SetPixel`](set_pixel.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`pixel`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Index of the current color look-up table.

## Result

[`GetPartStyle`](get_part_style.md) returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`SetPixel`,
`DispRegion`,
`DispImage`

## See also

`SetPixel`

## Module

Foundation
