# GetHsi (Operator)

## Name

`GetHsi` — Get the HSI coding of the current color.

## Signature

`static void HOperatorSet.GetHsi(HTuple windowHandle, out HTuple hue, out HTuple saturation, out HTuple intensity)`

`HTuple HWindow.GetHsi(out HTuple saturation, out HTuple intensity)`

## Description

`GetHsi` returns the output color or gray values, respectively, for
the window, described in *`hue`*, *`saturation`* and
*`intensity`*. The values returned by
`GetHsi` can be set with [`SetHsi`](set_hsi.md).

## Attention

The values returned by `GetHsi` may be inaccurate due to
rounding errors. They do not necessarily match the values set with
[`SetHsi`](set_hsi.md) exactly (colors are stored in RGB internally).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`hue`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Hue (color value) of the current color.

**`saturation`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Saturation of the current color.

**`intensity`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Intensity of the current color.

## Result

`GetHsi` returns 2 (
H_MSG_TRUE)
, if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`SetHsi`,
`SetRgb`,
`DispImage`

## See also

`SetHsi`,
`SetColor`,
`SetRgb`,
`TransToRgb`,
`TransFromRgb`

## Module

Foundation
