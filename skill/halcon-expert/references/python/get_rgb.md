# get_rgb (Operator)

## Name

`get_rgb` — Get the current color in RGB-coding.

## Signature

`def get_rgb(window_handle: HHandle) -> Tuple[Sequence[int], Sequence[int], Sequence[int]]`

## Description

`get_rgb` returns the output colors or gray values, respectively, for
the output window. They are defined by the three color
components red, green and blue.

The values returned by `get_rgb` can be set with
[`set_rgb`](set_rgb.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`red`** (output_control)  integer-array `→` Sequence[int]

The current color's red value.

**`green`** (output_control)  integer-array `→` Sequence[int]

The current color's green value.

**`blue`** (output_control)  integer-array `→` Sequence[int]

The current color's blue value.

## Result

`get_rgb` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`set_rgb`,
`disp_region`,
`disp_image`

## See also

`set_rgb`

## Module

Foundation
