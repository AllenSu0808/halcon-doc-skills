# QueryPaint (Operator)

## Name

`QueryPaint` — Query the gray value display modes.

## Signature

`static void HOperatorSet.QueryPaint(HTuple windowHandle, out HTuple mode)`

`HTuple HWindow.QueryPaint()`

## Description

`QueryPaint` returns the names of all gray value display
modes (e.g., 'gray', '3d_plot', etc.) for the
output window. These modes are used by
[`SetPaint`](set_paint.md). `QueryPaint` only returns the
names of the display values, not the additional parameters that may
be necessary for some modes.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`mode`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Gray value display mode names.

## Result

`QueryPaint` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`GetPaint`,
`SetPaint`,
`DispImage`

## See also

`SetPaint`,
`GetPaint`,
`DispImage`

## Module

Foundation
