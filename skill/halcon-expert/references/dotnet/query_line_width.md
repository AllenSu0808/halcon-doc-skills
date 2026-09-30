# QueryLineWidth (Operator)

## Name

`QueryLineWidth` — Query the possible line widths.

## Signature

`static void HOperatorSet.QueryLineWidth(out HTuple min, out HTuple max)`

`static void HInfo.QueryLineWidth(out int min, out int max)`

## Description

`QueryLineWidth` returns the minimal (*`min`*)
and maximal (*`max`*) values of widths of region
border which can be displayed. Setting of the border width is done with
[`SetLineWidth`](set_line_width.md). Border width is used by operators like
[`DispRegion`](disp_region.md), [`DispLine`](disp_line.md),
[`DispCircle`](disp_circle.md), [`DispRectangle1`](disp_rectangle1.md),
[`DispRectangle2`](disp_rectangle2.md) etc. if the drawing mode is “margin”
([`SetDraw`](set_draw.md)(::WindowHandle,'margin':)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`min`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Displayable minimum width.

**`max`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Displayable maximum width.

## Result

`QueryLineWidth` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`GetLineWidth`,
`SetLineWidth`,
`SetLineStyle`,
`DispLine`

## See also

`DispCircle`,
`DispLine`,
`DispRectangle1`,
`DispRectangle2`,
`DispRegion`,
`SetLineWidth`,
`GetLineWidth`,
`SetLineStyle`

## Module

Foundation
