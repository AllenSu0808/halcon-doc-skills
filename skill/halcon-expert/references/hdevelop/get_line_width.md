# get_line_width (Operator)

## Name

`get_line_width` — Get the current line width for contour display.

## Signature

`get_line_width( : : WindowHandle : Width)`

## Description

`get_line_width` returns the line width for region display
in the window. It is used by operators like
[`disp_region`](disp_region.md), [`disp_line`](disp_line.md),
[`disp_polygon`](disp_polygon.md), etc. *`Width`* is set with the
operator [`set_line_width`](set_line_width.md). *`Width`* is only
important for displaying the contour of objects.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Width`** (output_control)  real `→`  (real)

Current line width for contour display.

## Result

`get_line_width` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`set_line_width`,
`set_line_style`,
`disp_region`

## See also

`set_line_width`,
`disp_region`

## Module

Foundation
