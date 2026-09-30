# GetLineApprox (Operator)

## Name

`GetLineApprox` — Get the current approximation error for contour display.

## Warning

**`GetLineApprox` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.GetLineApprox(HTuple windowHandle, out HTuple approximation)`

`int HWindow.GetLineApprox()`

## Description

`GetLineApprox` returns a parameter that controls the
approximation error for region contour display in the
window. It is used by the operator
[`DispRegion`](disp_region.md). *`approximation`* controls the polygon
approximation for contour display ( 0 <=> no approximation). *`approximation`* is only
important for displaying the contour of objects, especially if a line
style was set with [`SetLineStyle`](set_line_style.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`approximation`** (output_control)  string `→` [HTuple](HTuple.md) (*int* / long)

Current approximation error for contour display.

## Result

`GetLineApprox` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`SetLineApprox`,
`SetLineStyle`,
`DispRegion`

## See also

`GetRegionPolygon`,
`SetLineApprox`,
`SetLineStyle`,
`DispRegion`

## Module

Foundation
