# get_line_width (Operator)

## Name

`get_line_width` — Get the current line width for contour display.

## Signature

`def get_line_width(window_handle: HHandle) -> float`

## Description

`get_line_width` returns the line width for region display
in the window. It is used by operators like
[`disp_region`](disp_region.md), [`disp_line`](disp_line.md),
[`disp_polygon`](disp_polygon.md), etc. *`width`* is set with the
operator [`set_line_width`](set_line_width.md). *`width`* is only
important for displaying the contour of objects.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`width`** (output_control)  real `→` float

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
