# SetPixel (Operator)

## Name

`SetPixel` — Define a color lookup table index.

## Warning

**`SetPixel` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.SetPixel(HTuple windowHandle, HTuple pixel)`

`void HWindow.SetPixel(HTuple pixel)`

`void HWindow.SetPixel(int pixel)`

## Description

`SetPixel` sets pixel values: colors
([`SetColor`](set_color.md), [`SetRgb`](set_rgb.md), etc.) and gray values
([`SetGray`](set_gray.md)) are coded together into a number, called
pixel. This 'pixel' is an index in the color lookup table. It ranges
from 0 to 1 in b/w images and 0 to 255 color images with 8 bit
planes. It is different from the 'pixel' ("picture element") in
image processing. Therefore HALCON distinguishes between pixel and
image element (or gray value).

The current value can be queried with [`GetPixel`](get_pixel.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`pixel`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

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

`SetPixel` returns 2 (
H_MSG_TRUE)
if the parameter is correct and
the window is valid. Otherwise an exception is raised.

## Possible Predecessors

`GetPixel`

## Possible Successors

`DispImage`,
`DispRegion`

## Alternatives

`SetRgb`,
`SetColor`,
`SetHsi`

## See also

`GetPixel`,
`SetLut`,
`DispRegion`,
`DispImage`,
`DispColor`

## Module

Foundation
