# get_line_style (Operator)

## Name

`get_line_style` — Get the current graphic mode for contours.

## Signature

`get_line_style( : : WindowHandle : Style)`

## Description

`get_line_style` returns the display mode for contours
when displaying regions. It is used by operators like
[`disp_region`](disp_region.md), [`disp_line`](disp_line.md),
[`disp_polygon`](disp_polygon.md), etc. *`Style`* is set with the
operator [`set_line_style`](set_line_style.md).
*`Style`* is only
important for displaying the contour of objects, especially if a line
style was set with [`set_line_style`](set_line_style.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Style`** (output_control)  integer-array `→`  (integer)

Template for contour display.

## Result

`get_line_style` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## See also

`set_line_style`,
`disp_region`

## Module

Foundation
