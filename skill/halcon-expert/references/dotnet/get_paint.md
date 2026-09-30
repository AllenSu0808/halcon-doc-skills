# GetPaint (Operator)

## Name

`GetPaint` — Get the current display mode for gray values.

## Signature

`static void HOperatorSet.GetPaint(HTuple windowHandle, out HTuple mode)`

`HTuple HWindow.GetPaint()`

## Description

`GetPaint` returns the display mode for gray values in the
window. *`mode`* is used by the operator
[`DispImage`](disp_image.md). `GetPaint` is used for temporary
changes of the gray value display mode. The current value is queried,
then changed (with the operator [`SetPaint`](set_paint.md)) and finally the
old value is written back. The available modes can be viewed with
the operator [`QueryPaint`](query_paint.md). *`mode`* is the name
of the display mode. If a mode can be customized with parameters,
the parameter values are passed in a tuple after the mode name. The
order of values is the same as in [`SetPaint`](set_paint.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`mode`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string* / int / long / double)

Name and parameter values of the current display mode.

## Result

`GetPaint` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Predecessors

`QueryPaint`

## Possible Successors

`SetPaint`,
`DispRegion`,
`DispImage`

## See also

`SetPaint`,
`QueryPaint`,
`DispImage`

## Module

Foundation
