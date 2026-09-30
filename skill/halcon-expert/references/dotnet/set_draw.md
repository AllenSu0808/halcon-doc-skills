# SetDraw (Operator)

## Name

`SetDraw` — Define the region fill mode.

## Signature

`static void HOperatorSet.SetDraw(HTuple windowHandle, HTuple mode)`

`void HWindow.SetDraw(string mode)`

## Description

`SetDraw` defines the region fill mode. If
*`mode`* is set to 'fill', output regions are filled, if set
to 'margin', only contours are displayed. Setting *`mode`*
only affects the valid window. It is used by operators with region
output like [`DispRegion`](disp_region.md), [`DispCircle`](disp_circle.md),
[`DispRectangle1`](disp_rectangle1.md), [`DispRectangle2`](disp_rectangle2.md),
[`DispArrow`](disp_arrow.md) etc.
It is also used by operators with gray value output for some gray value
output modes. If the mode is 'margin', the contour can
be affected with [`SetLineWidth`](set_line_width.md) and [`SetLineStyle`](set_line_style.md).

## Attention

If the output mode is 'margin' and the line width is more than one,
objects may not be displayed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Fill mode for region output.

Default:
"fill"

List of values:
"fill", "margin"

## Result

`SetDraw` returns 2 (
H_MSG_TRUE)
if *`mode`*
is correct and the window is valid. Otherwise an exception is
raised.

## Possible Predecessors

`GetDraw`

## Possible Successors

`DispRegion`

## See also

`GetDraw`,
`DispRegion`,
`SetPaint`,
`DispImage`,
`SetLineWidth`,
`SetLineStyle`

## Module

Foundation
