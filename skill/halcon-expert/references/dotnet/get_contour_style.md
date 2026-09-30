# GetContourStyle (Operator)

## Name

`GetContourStyle` — Get the current contour display fill style.

## Signature

`static void HOperatorSet.GetContourStyle(HTuple windowHandle, out HTuple style)`

`string HWindow.GetContourStyle()`

## Description

`GetContourStyle` returns the contour fill style of the
output window as set with [`SetContourStyle`](set_contour_style.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`style`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Current contour fill style.

## Result

`GetContourStyle` returns 2 (
H_MSG_TRUE)
, if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`SetContourStyle`,
`DispXld`

## See also

`SetContourStyle`,
`DispXld`

## Module

Foundation
