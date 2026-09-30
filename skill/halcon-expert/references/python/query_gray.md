# query_gray (Operator)

## Name

`query_gray` — Query the displayable gray values.

## Signature

`def query_gray(window_handle: HHandle) -> Sequence[int]`

## Description

`query_gray` returns all gray values that are used for
gray value output ([`disp_image`](disp_image.md)) and that can be reproduced
exactly in the window. They can be set with the
[`set_gray`](set_gray.md) call.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`grayval`** (output_control)  integer-array `→` Sequence[int]

Tuple of all displayable gray values.

## Result

`query_gray` returns 2 (
H_MSG_TRUE)
, if the window is
valid. Otherwise an exception is raised.

## Possible Successors

`set_gray`,
`disp_region`

## See also

`set_gray`,
`disp_image`

## Module

Foundation
