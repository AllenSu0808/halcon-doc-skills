# get_hsi (Operator)

## Name

`get_hsi` — Get the HSI coding of the current color.

## Signature

`get_hsi( : : WindowHandle : Hue, Saturation, Intensity)`

## Description

`get_hsi` returns the output color or gray values, respectively, for
the window, described in *`Hue`*, *`Saturation`* and
*`Intensity`*. The values returned by
`get_hsi` can be set with [`set_hsi`](set_hsi.md).

## Attention

The values returned by `get_hsi` may be inaccurate due to
rounding errors. They do not necessarily match the values set with
[`set_hsi`](set_hsi.md) exactly (colors are stored in RGB internally).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Hue`** (output_control)  integer-array `→`  (integer)

Hue (color value) of the current color.

**`Saturation`** (output_control)  integer-array `→`  (integer)

Saturation of the current color.

**`Intensity`** (output_control)  integer-array `→`  (integer)

Intensity of the current color.

## Result

`get_hsi` returns 2 (
H_MSG_TRUE)
, if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`set_hsi`,
`set_rgb`,
`disp_image`

## See also

`set_hsi`,
`set_color`,
`set_rgb`,
`trans_to_rgb`,
`trans_from_rgb`

## Module

Foundation
