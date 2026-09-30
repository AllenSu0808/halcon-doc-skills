# get_hsi (Operator)

## Name

`get_hsi` — Get the HSI coding of the current color.

## Signature

`def get_hsi(window_handle: HHandle) -> Tuple[Sequence[int], Sequence[int], Sequence[int]]`

## Description

`get_hsi` returns the output color or gray values, respectively, for
the window, described in *`hue`*, *`saturation`* and
*`intensity`*. The values returned by
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

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`hue`** (output_control)  integer-array `→` Sequence[int]

Hue (color value) of the current color.

**`saturation`** (output_control)  integer-array `→` Sequence[int]

Saturation of the current color.

**`intensity`** (output_control)  integer-array `→` Sequence[int]

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
