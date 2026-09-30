# DispLine (Operator)

## Name

`DispLine` — Draws lines in a window.

## Signature

`static void HOperatorSet.DispLine(HTuple windowHandle, HTuple row1, HTuple column1, HTuple row2, HTuple column2)`

`void HWindow.DispLine(HTuple row1, HTuple column1, HTuple row2, HTuple column2)`

`void HWindow.DispLine(double row1, double column1, double row2, double column2)`

## Description

`DispLine` displays one or several lines in the output
window. A line is described by the coordinates of the start
(*`row1`*,*`column1`*) and the coordinates of the end
(*`row2`*,*`column2`*).
The operators used to control the display of regions
(e.g., [`SetColor`](set_color.md), [`SetGray`](set_gray.md), [`SetDraw`](set_draw.md),
[`SetLineWidth`](set_line_width.md)) can also be used with lines. Several lines can
be displayed with one call by using tuple parameters. For the use of colors
with several lines, see [`SetColor`](set_color.md).

## Attention

The starting points and the ending points of the lines
must be in the window.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`row1`** (input_control)  line.begin.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row index of the start.

Default:
32.0

Suggested values:
0.0, 64.0, 128.0, 256.0, 511.0

Value range:
`0
≤
row1
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

**`column1`** (input_control)  line.begin.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column index of the start.

Default:
32.0

Suggested values:
0.0, 64.0, 128.0, 256.0, 511.0

Value range:
`0
≤
column1
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

**`row2`** (input_control)  line.end.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row index of end.

Default:
64.0

Suggested values:
0.0, 64.0, 128.0, 256.0, 511.0

Value range:
`0
≤
row2
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

**`column2`** (input_control)  line.end.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column index of end.

Default:
64.0

Suggested values:
0.0, 64.0, 128.0, 256.0, 511.0

Value range:
`0
≤
column2
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

## Example (HDevelop)

```
* Display contour of a rectangle
disp_line(WindowHandle,Row1,Column1,Row1,Column2)
disp_line(WindowHandle,Row1,Column2,Row2,Column2)
disp_line(WindowHandle,Row2,Column2,Row2,Column1)
disp_line(WindowHandle,Row2,Column1,Row1,Column1)
```

## Result

`DispLine` returns 2 (
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
`DispRegion`,
`GenRegionPolygon`,
`GenRegionPoints`

## See also

`OpenWindow`,
`SetColor`,
`SetRgb`,
`SetHsi`,
`SetLineWidth`

## Module

Foundation
