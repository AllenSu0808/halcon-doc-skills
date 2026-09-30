# disp_line (Operator)

## Name

`disp_line` — Draws lines in a window.

## Signature

`disp_line( : : WindowHandle, Row1, Column1, Row2, Column2 : )`

## Description

`disp_line` displays one or several lines in the output
window. A line is described by the coordinates of the start
(*`Row1`*,*`Column1`*) and the coordinates of the end
(*`Row2`*,*`Column2`*).
The operators used to control the display of regions
(e.g., [`set_color`](set_color.md), [`set_gray`](set_gray.md), [`set_draw`](set_draw.md),
[`set_line_width`](set_line_width.md)) can also be used with lines. Several lines can
be displayed with one call by using tuple parameters. For the use of colors
with several lines, see [`set_color`](set_color.md).

## Attention

The starting points and the ending points of the lines
must be in the window.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Row1`** (input_control)  line.begin.y(-array) `→`  (real)

Row index of the start.

Default:
32.0

Suggested values:
0.0, 64.0, 128.0, 256.0, 511.0

Value range:
`0
≤
Row1
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

**`Column1`** (input_control)  line.begin.x(-array) `→`  (real)

Column index of the start.

Default:
32.0

Suggested values:
0.0, 64.0, 128.0, 256.0, 511.0

Value range:
`0
≤
Column1
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

**`Row2`** (input_control)  line.end.y(-array) `→`  (real)

Row index of end.

Default:
64.0

Suggested values:
0.0, 64.0, 128.0, 256.0, 511.0

Value range:
`0
≤
Row2
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

**`Column2`** (input_control)  line.end.x(-array) `→`  (real)

Column index of end.

Default:
64.0

Suggested values:
0.0, 64.0, 128.0, 256.0, 511.0

Value range:
`0
≤
Column2
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

`disp_line` returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`open_window`,
`set_rgb`,
`set_lut`,
`set_hsi`,
`set_draw`,
`set_color`,
`set_colored`,
`set_line_width`

## Alternatives

`disp_arrow`,
`disp_rectangle1`,
`disp_rectangle2`,
`disp_region`,
`gen_region_polygon`,
`gen_region_points`

## See also

`open_window`,
`set_color`,
`set_rgb`,
`set_hsi`,
`set_line_width`

## Module

Foundation
