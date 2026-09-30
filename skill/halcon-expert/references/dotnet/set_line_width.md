# SetLineWidth (Operator)

## Name

`SetLineWidth` — Define the line width for region contour output.

## Signature

`static void HOperatorSet.SetLineWidth(HTuple windowHandle, HTuple width)`

`void HWindow.SetLineWidth(double width)`

## Description

`SetLineWidth` defines the line width (in pixel) in
which a region contour is displayed (e.g., with
[`DispRegion`](disp_region.md), [`DispLine`](disp_line.md),
[`DispPolygon`](disp_polygon.md), etc.) The operator
[`GetLineWidth`](get_line_width.md) returns the current value for the
window. Some output devices may not allow to change the contour
width. If it is possible for the current device, it can be queried with
[`QueryLineWidth`](query_line_width.md).

## Attention

The line width is important if the output mode was set to 'margin'
(see [`SetDraw`](set_draw.md)). If the line width is greater than one,
regions may not always be displayed correctly.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`width`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Line width for region output in contour mode.

Default:
1.0

Restriction:
`Width >= 1.0 && Width <= 2000.0`

## Result

`SetLineWidth` returns 2 (
H_MSG_TRUE)
if the parameter is
correct and the window is valid. Otherwise an exception is raised.

## Possible Predecessors

`QueryLineWidth`,
`GetLineWidth`

## Possible Successors

`DispRegion`

## See also

`GetLineWidth`,
`QueryLineWidth`,
`SetDraw`,
`DispRegion`

## Module

Foundation
