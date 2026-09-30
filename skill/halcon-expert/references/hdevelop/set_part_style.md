# set_part_style (Operator)

## Name

`set_part_style` — Define an interpolation method for gray value output.

## Signature

`set_part_style( : : WindowHandle, Style : )`

## Description

`set_part_style` defines the interpolation method to
zoom an image part which is displayed in the window. Interpolation
takes place, if the output window has different size than the image
to display (e.g., after a call to [`set_part`](set_part.md) or a
window resize). Three modes are supported:

- **0** —

  no interpolation (low quality, very fast).
- **1** —

  unweighted interpolation (medium quality and run time)
- **2** —

  weighted interpolation (high quality, slow)

The current value can be queried with [`get_part_style`](get_part_style.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Style`** (input_control)  integer `→`  (integer)

Interpolation method for image output:
0 (fast, low quality) to 2 (slow, high quality).

Default:
0

List of values:
0, 1, 2

## Result

`set_part_style` returns 2 (
H_MSG_TRUE)
if the parameter is correct
and the window is valid. Otherwise an exception is raised.

## Possible Predecessors

`get_part_style`

## Possible Successors

`set_part`,
`disp_image`,
`disp_region`

## Alternatives

`affine_trans_image`

## See also

`get_part_style`,
`set_part`,
`disp_image`,
`disp_color`

## Module

Foundation
