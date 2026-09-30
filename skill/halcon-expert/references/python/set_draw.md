# set_draw (Operator)

## Name

`set_draw` — Define the region fill mode.

## Signature

`def set_draw(window_handle: HHandle, mode: str) -> None`

## Description

`set_draw` defines the region fill mode. If
*`mode`* is set to 'fill', output regions are filled, if set
to 'margin', only contours are displayed. Setting *`mode`*
only affects the valid window. It is used by operators with region
output like [`disp_region`](disp_region.md), [`disp_circle`](disp_circle.md),
[`disp_rectangle1`](disp_rectangle1.md), [`disp_rectangle2`](disp_rectangle2.md),
[`disp_arrow`](disp_arrow.md) etc.
It is also used by operators with gray value output for some gray value
output modes. If the mode is 'margin', the contour can
be affected with [`set_line_width`](set_line_width.md) and [`set_line_style`](set_line_style.md).

## Attention

If the output mode is 'margin' and the line width is more than one,
objects may not be displayed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`mode`** (input_control)  string `→` str

Fill mode for region output.

Default:
"fill"

List of values:
"fill", "margin"

## Result

`set_draw` returns 2 (
H_MSG_TRUE)
if *`mode`*
is correct and the window is valid. Otherwise an exception is
raised.

## Possible Predecessors

`get_draw`

## Possible Successors

`disp_region`

## See also

`get_draw`,
`disp_region`,
`set_paint`,
`disp_image`,
`set_line_width`,
`set_line_style`

## Module

Foundation
