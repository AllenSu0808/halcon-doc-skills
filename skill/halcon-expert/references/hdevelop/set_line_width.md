# set_line_width (Operator)

## Name

`set_line_width` — Define the line width for region contour output.

## Signature

`set_line_width( : : WindowHandle, Width : )`

## Description

`set_line_width` defines the line width (in pixel) in
which a region contour is displayed (e.g., with
[`disp_region`](disp_region.md), [`disp_line`](disp_line.md),
[`disp_polygon`](disp_polygon.md), etc.) The operator
[`get_line_width`](get_line_width.md) returns the current value for the
window. Some output devices may not allow to change the contour
width. If it is possible for the current device, it can be queried with
[`query_line_width`](query_line_width.md).

## Attention

The line width is important if the output mode was set to 'margin'
(see [`set_draw`](set_draw.md)). If the line width is greater than one,
regions may not always be displayed correctly.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Width`** (input_control)  real `→`  (real)

Line width for region output in contour mode.

Default:
1.0

Restriction:
`Width >= 1.0 && Width <= 2000.0`

## Result

`set_line_width` returns 2 (
H_MSG_TRUE)
if the parameter is
correct and the window is valid. Otherwise an exception is raised.

## Possible Predecessors

`query_line_width`,
`get_line_width`

## Possible Successors

`disp_region`

## See also

`get_line_width`,
`query_line_width`,
`set_draw`,
`disp_region`

## Module

Foundation
