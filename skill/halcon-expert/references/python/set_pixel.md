# set_pixel (Operator)

## Name

`set_pixel` — Define a color lookup table index.

## Warning

**`set_pixel` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def set_pixel(window_handle: HHandle, pixel: MaybeSequence[int]) -> None`

## Description

`set_pixel` sets pixel values: colors
([`set_color`](set_color.md), [`set_rgb`](set_rgb.md), etc.) and gray values
([`set_gray`](set_gray.md)) are coded together into a number, called
pixel. This 'pixel' is an index in the color lookup table. It ranges
from 0 to 1 in b/w images and 0 to 255 color images with 8 bit
planes. It is different from the 'pixel' ("picture element") in
image processing. Therefore HALCON distinguishes between pixel and
image element (or gray value).

The current value can be queried with [`get_pixel`](get_pixel.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`pixel`** (input_control)  integer(-array) `→` MaybeSequence[int]

Color lookup table index.

Default:
128

Value range:
`0
≤
pixel
≤
255`

## Result

`set_pixel` returns 2 (
H_MSG_TRUE)
if the parameter is correct and
the window is valid. Otherwise an exception is raised.

## Possible Predecessors

`get_pixel`

## Possible Successors

`disp_image`,
`disp_region`

## Alternatives

`set_rgb`,
`set_color`,
`set_hsi`

## See also

`get_pixel`,
`set_lut`,
`disp_region`,
`disp_image`,
`disp_color`

## Module

Foundation
