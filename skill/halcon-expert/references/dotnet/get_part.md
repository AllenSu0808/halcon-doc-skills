# GetPart (Operator)

## Name

`GetPart` — Get the image part.

## Signature

`static void HOperatorSet.GetPart(HTuple windowHandle, out HTuple row1, out HTuple column1, out HTuple row2, out HTuple column2)`

`void HWindow.GetPart(out HTuple row1, out HTuple column1, out HTuple row2, out HTuple column2)`

`void HWindow.GetPart(out int row1, out int column1, out int row2, out int column2)`

## Description

`GetPart` returns the upper left and lower right corner
of the image part shown in the window. The image part can be
changed with the operator [`SetPart`](set_part.md) (Default is the
whole image).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`row1`** (output_control)  rectangle.origin.y `→` [HTuple](HTuple.md) (*int* / long / double)

Row index of the image part's upper left corner.

**`column1`** (output_control)  rectangle.origin.x `→` [HTuple](HTuple.md) (*int* / long / double)

Column index of the image part's upper left corner.

**`row2`** (output_control)  rectangle.corner.y `→` [HTuple](HTuple.md) (*int* / long / double)

Row index of the image part's lower right corner.

**`column2`** (output_control)  rectangle.corner.x `→` [HTuple](HTuple.md) (*int* / long / double)

Column index of the image part's lower right corner.

## Result

`GetPart` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`SetPart`,
`DispRegion`,
`DispImage`

## See also

`SetPart`,
`DispImage`,
`DispRegion`,
`DispColor`

## Module

Foundation
