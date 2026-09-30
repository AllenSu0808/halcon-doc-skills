# get_part (Operator)

## Name

`get_part` — Get the image part.

## Signature

`get_part( : : WindowHandle : Row1, Column1, Row2, Column2)`

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

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Row1`** (output_control)  rectangle.origin.y `→`  (integer / real)

Row index of the image part's upper left corner.

**`Column1`** (output_control)  rectangle.origin.x `→`  (integer / real)

Column index of the image part's upper left corner.

**`Row2`** (output_control)  rectangle.corner.y `→`  (integer / real)

Row index of the image part's lower right corner.

**`Column2`** (output_control)  rectangle.corner.x `→`  (integer / real)

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
