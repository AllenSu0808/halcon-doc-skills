# GetLineWidth (Operator)

## Name

`GetLineWidth` — Get the current line width for contour display.

## Signature

`static void HOperatorSet.GetLineWidth(HTuple windowHandle, out HTuple width)`

`double HWindow.GetLineWidth()`

## Description

`GetLineWidth` returns the line width for region display
in the window. It is used by operators like
[`DispRegion`](disp_region.md), [`DispLine`](disp_line.md),
[`DispPolygon`](disp_polygon.md), etc. *`width`* is set with the
operator [`SetLineWidth`](set_line_width.md). *`width`* is only
important for displaying the contour of objects.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`width`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Current line width for contour display.

## Result

`GetLineWidth` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`SetLineWidth`,
`SetLineStyle`,
`DispRegion`

## See also

`SetLineWidth`,
`DispRegion`

## Module

Foundation
