# QueryGray (Operator)

## Name

`QueryGray` — Query the displayable gray values.

## Signature

`static void HOperatorSet.QueryGray(HTuple windowHandle, out HTuple grayval)`

`HTuple HWindow.QueryGray()`

## Description

`QueryGray` returns all gray values that are used for
gray value output ([`DispImage`](disp_image.md)) and that can be reproduced
exactly in the window. They can be set with the
[`SetGray`](set_gray.md) call.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`grayval`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Tuple of all displayable gray values.

## Result

`QueryGray` returns 2 (
H_MSG_TRUE)
, if the window is
valid. Otherwise an exception is raised.

## Possible Successors

`SetGray`,
`DispRegion`

## See also

`SetGray`,
`DispImage`

## Module

Foundation
