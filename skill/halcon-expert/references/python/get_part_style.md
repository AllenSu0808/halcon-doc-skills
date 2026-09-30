# get_part_style (Operator)

## Name

`get_part_style` — Get the current interpolation mode for gray value display.

## Signature

`def get_part_style(window_handle: HHandle) -> int`

## Description

`get_part_style` returns the interpolation mode used for
displaying an image part in the window. An interpolation
takes place if the output window is larger than the image format or
the image output format (see [`set_part`](set_part.md)). HALCON supports
three interpolation modes:

- **0** —

  no interpolation (low quality, very fast).
- **1** —

  unweighted interpolation (average quality and computation time)
- **2** —

  weighted interpolation (high quality, slow)

The current mode can be changed with [`set_part_style`](set_part_style.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`style`** (output_control)  integer `→` int

Interpolation mode for image display:
0 (fast, low quality) to 2 (slow, high quality).

List of values:
0, 1, 2

## Result

`get_part_style` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`set_part_style`,
`disp_region`,
`disp_image`

## See also

`set_part_style`,
`set_part`,
`disp_image`,
`disp_color`

## Module

Foundation
