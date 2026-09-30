# GetDraw (Operator)

## Name

`GetDraw` — Get the current region fill mode.

## Signature

`static void HOperatorSet.GetDraw(HTuple windowHandle, out HTuple mode)`

`string HWindow.GetDraw()`

## Description

`GetDraw` returns the region fill mode of the
output window. It is used by operators as [`DispRegion`](disp_region.md),
[`DispCircle`](disp_circle.md), [`DispArrow`](disp_arrow.md),
[`DispRectangle1`](disp_rectangle1.md), [`DispRectangle2`](disp_rectangle2.md) etc.
The region fill mode is set with [`SetDraw`](set_draw.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`mode`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Current region fill mode.

## Result

`GetDraw` returns 2 (
H_MSG_TRUE)
, if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`SetDraw`,
`DispRegion`

## See also

`SetDraw`,
`DispRegion`,
`SetPaint`

## Module

Foundation
