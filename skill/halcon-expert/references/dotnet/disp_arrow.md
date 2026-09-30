# DispArrow (Operator)

## Name

`DispArrow` — Displays arrows in a window.

## Signature

`static void HOperatorSet.DispArrow(HTuple windowHandle, HTuple row1, HTuple column1, HTuple row2, HTuple column2, HTuple size)`

`void HWindow.DispArrow(HTuple row1, HTuple column1, HTuple row2, HTuple column2, HTuple size)`

`void HWindow.DispArrow(double row1, double column1, double row2, double column2, double size)`

## Description

`DispArrow` displays one or several arrows in the output
window. An arrow is described by the coordinates of the start
(*`row1`*,*`column1`*) and the end
(*`row2`*,*`column2`*). An arrowhead is displayed at the end
of the arrow. The size of the arrowhead is specified by the parameter
*`size`*. If the arrow consists of just one point (start = end)
nothing is displayed. The operators used to control the display of regions
(e.g., [`SetDraw`](set_draw.md), [`SetColor`](set_color.md),
[`SetLineWidth`](set_line_width.md)) can also be used with arrows. Several arrows
can be displayed with one call by using tuple parameters. For the use of
colors with several arcs, see [`SetColor`](set_color.md).

## Attention

The start and the end of the arrows must fall within the window.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`row1`** (input_control)  line.begin.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row index of the start.

Default:
10.0

Suggested values:
0.0, 64.0, 128.0, 256.0

Value range:
`0.0
≤
row1
≤
511.0` (lin)

Minimum increment:
1.0

Recommended increment:
1.0

**`column1`** (input_control)  line.begin.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column index of the start.

Default:
10.0

Suggested values:
0.0, 64.0, 128.0, 256.0

Value range:
`0.0
≤
column1
≤
511.0` (lin)

Minimum increment:
1.0

Recommended increment:
1.0

**`row2`** (input_control)  line.end.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row index of the end.

Default:
118.0

Suggested values:
0.0, 64.0, 128.0, 256.0

Value range:
`0.0
≤
row2
≤
511.0` (lin)

Minimum increment:
1.0

Recommended increment:
1.0

**`column2`** (input_control)  line.end.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column index of the end.

Default:
118.0

Suggested values:
0.0, 64.0, 128.0, 256.0

Value range:
`0.0
≤
column2
≤
511.0` (lin)

Minimum increment:
1.0

Recommended increment:
1.0

**`size`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Size of the arrowhead.

Default:
1.0

Suggested values:
1.0, 2.0, 3.0, 5.0

Value range:
`0.0
≤
size
≤
20.0` (lin)

Minimum increment:
1.0

Recommended increment:
1.0

Restriction:
`Size > 0.0`

## Example (HDevelop)

```
set_color(WindowHandle,['red','green'])
disp_arrow(WindowHandle,[10,10],[10,10],[118,110],[118,118],1.0)
```

## Result

`DispArrow` returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`OpenWindow`,
`SetDraw`,
`SetColor`,
`SetColored`,
`SetLineWidth`,
`SetRgb`,
`SetHsi`

## Alternatives

`DispLine`,
`GenRegionPolygon`,
`DispRegion`

## See also

`OpenWindow`,
`SetColor`,
`SetDraw`,
`SetLineWidth`

## Module

Foundation
