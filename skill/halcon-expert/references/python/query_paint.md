# query_paint (Operator)

## Name

`query_paint` — Query the gray value display modes.

## Signature

`def query_paint(window_handle: HHandle) -> Sequence[str]`

## Description

`query_paint` returns the names of all gray value display
modes (e.g., 'gray', '3d_plot', etc.) for the
output window. These modes are used by
[`set_paint`](set_paint.md). `query_paint` only returns the
names of the display values, not the additional parameters that may
be necessary for some modes.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`mode`** (output_control)  string-array `→` Sequence[str]

Gray value display mode names.

## Result

`query_paint` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`get_paint`,
`set_paint`,
`disp_image`

## See also

`set_paint`,
`get_paint`,
`disp_image`

## Module

Foundation
