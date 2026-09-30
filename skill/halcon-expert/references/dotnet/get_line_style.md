# GetLineStyle (Operator)

## Name

`GetLineStyle` — Get the current graphic mode for contours.

## Signature

`static void HOperatorSet.GetLineStyle(HTuple windowHandle, out HTuple style)`

`HTuple HWindow.GetLineStyle()`

## Description

`GetLineStyle` returns the display mode for contours
when displaying regions. It is used by operators like
[`DispRegion`](disp_region.md), [`DispLine`](disp_line.md),
[`DispPolygon`](disp_polygon.md), etc. *`style`* is set with the
operator [`SetLineStyle`](set_line_style.md).
*`style`* is only
important for displaying the contour of objects, especially if a line
style was set with [`SetLineStyle`](set_line_style.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`style`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Template for contour display.

## Result

`GetLineStyle` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## See also

`SetLineStyle`,
`DispRegion`

## Module

Foundation
