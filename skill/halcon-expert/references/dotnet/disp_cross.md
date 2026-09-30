# DispCross (Operator)

## Name

`DispCross` — Displays crosses in a window.

## Signature

`static void HOperatorSet.DispCross(HTuple windowHandle, HTuple row, HTuple column, HTuple size, HTuple angle)`

`void HWindow.DispCross(HTuple row, HTuple column, double size, double angle)`

`void HWindow.DispCross(double row, double column, double size, double angle)`

## Description

`DispCross` displays one or several crosses in the output
window. A cross is described by the coordinates of the center point
(*`row`*,*`column`*), the length of its bars *`size`* and the
orientation *`angle`*.
The operators used to control the display of regions
(e.g., [`SetColor`](set_color.md), [`SetGray`](set_gray.md), [`SetDraw`](set_draw.md),
[`SetLineWidth`](set_line_width.md)) can also be used with crosses. Several crosses can
be displayed with one call by using tuple parameters. For the use of colors
with several crosses, see [`SetColor`](set_color.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`row`** (input_control)  coordinates.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the center.

Default:
32.0

Suggested values:
0.0, 64.0, 128.0, 256.0, 511.0

**`column`** (input_control)  coordinates.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the center.

Default:
32.0

Suggested values:
0.0, 64.0, 128.0, 256.0, 511.0

**`size`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Length of the bars.

Default:
6.0

Suggested values:
4.0, 6.0, 8.0, 10.0

Value range:
`0.0
≤
size`

**`angle`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Orientation.

Default:
0.0

Suggested values:
0.0, 0.78539816339744830961566084581988

## Result

`DispCross` returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`OpenWindow`,
`SetRgb`,
`SetLut`,
`SetHsi`,
`SetDraw`,
`SetColor`,
`SetColored`,
`SetLineWidth`

## Alternatives

`DispArrow`,
`DispRectangle1`,
`DispRectangle2`,
`DispCircle`

## See also

`OpenWindow`,
`SetColor`,
`SetRgb`,
`SetHsi`,
`SetLineWidth`

## Module

Foundation
