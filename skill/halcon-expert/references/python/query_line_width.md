# query_line_width (Operator)

## Name

`query_line_width` — Query the possible line widths.

## Signature

`def query_line_width() -> Tuple[int, int]`

## Description

`query_line_width` returns the minimal (*`min`*)
and maximal (*`max`*) values of widths of region
border which can be displayed. Setting of the border width is done with
[`set_line_width`](set_line_width.md). Border width is used by operators like
[`disp_region`](disp_region.md), [`disp_line`](disp_line.md),
[`disp_circle`](disp_circle.md), [`disp_rectangle1`](disp_rectangle1.md),
[`disp_rectangle2`](disp_rectangle2.md) etc. if the drawing mode is “margin”
([`set_draw`](set_draw.md)(::WindowHandle,'margin':)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`min`** (output_control)  integer `→` int

Displayable minimum width.

**`max`** (output_control)  integer `→` int

Displayable maximum width.

## Result

`query_line_width` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`get_line_width`,
`set_line_width`,
`set_line_style`,
`disp_line`

## See also

`disp_circle`,
`disp_line`,
`disp_rectangle1`,
`disp_rectangle2`,
`disp_region`,
`set_line_width`,
`get_line_width`,
`set_line_style`

## Module

Foundation
