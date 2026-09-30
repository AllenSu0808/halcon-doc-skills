# get_part (Operator)

## Name

`get_part` — Get the image part.

## Signature

`def get_part(window_handle: HHandle) -> Tuple[Union[int, float], Union[int, float], Union[int, float], Union[int, float]]`

## Description

`get_part` returns the upper left and lower right corner
of the image part shown in the window. The image part can be
changed with the operator [`set_part`](set_part.md) (Default is the
whole image).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`row_1`** (output_control)  rectangle.origin.y `→` Union[int, float]

Row index of the image part's upper left corner.

**`column_1`** (output_control)  rectangle.origin.x `→` Union[int, float]

Column index of the image part's upper left corner.

**`row_2`** (output_control)  rectangle.corner.y `→` Union[int, float]

Row index of the image part's lower right corner.

**`column_2`** (output_control)  rectangle.corner.x `→` Union[int, float]

Column index of the image part's lower right corner.

## Result

`get_part` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`set_part`,
`disp_region`,
`disp_image`

## See also

`set_part`,
`disp_image`,
`disp_region`,
`disp_color`

## Module

Foundation
