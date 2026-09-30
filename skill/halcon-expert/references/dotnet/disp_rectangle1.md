# DispRectangle1 (Operator)

## Name

`DispRectangle1` — Display of rectangles aligned to the coordinate axes.

## Signature

`static void HOperatorSet.DispRectangle1(HTuple windowHandle, HTuple row1, HTuple column1, HTuple row2, HTuple column2)`

`void HWindow.DispRectangle1(HTuple row1, HTuple column1, HTuple row2, HTuple column2)`

`void HWindow.DispRectangle1(double row1, double column1, double row2, double column2)`

## Description

`DispRectangle1` displays one or several rectangles in the
output window. A rectangle is described by the upper left corner
(*`row1`*,*`column1`*) and the lower right corner
(*`row2`*,*`column2`*). If the given coordinates are not
within the boundary of the window the rectangle is clipped accordingly.
The operators used to control the display of regions
(e.g., [`SetColor`](set_color.md), [`SetGray`](set_gray.md), [`SetDraw`](set_draw.md),
[`SetLineWidth`](set_line_width.md)) can also be used with rectangles. Several
rectangles can be displayed with one call by using tuple parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`row1`** (input_control)  rectangle.origin.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row index of the upper left corner.

Default:
16

Suggested values:
0, 64, 128, 256, 511

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

**`column1`** (input_control)  rectangle.origin.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column index of the upper left corner.

Default:
16

Suggested values:
0, 64, 128, 256, 511

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

**`row2`** (input_control)  rectangle.corner.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row index of the lower right corner.

Default:
48

Suggested values:
0, 64, 128, 256, 511

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

Restriction:
`Row2 >= Row1`

**`column2`** (input_control)  rectangle.corner.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column index of the lower right corner.

Default:
80

Suggested values:
0, 64, 128, 256, 511

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

Restriction:
`Column2 >= Column1`

## Example (HDevelop)

```
set_color(WindowHandle,'green')
draw_region(MyRegion,WindowHandle)
smallest_rectangle1(MyRegion,R1,C1,R2,C2)
disp_rectangle1(WindowHandle,R1,C1,R2,C2)
```

## Result

`DispRectangle1` returns 2 (
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

`DispRectangle2`,
`GenRectangle1`,
`DispRegion`,
`DispLine`,
`SetShape`

## See also

`OpenWindow`,
`SetColor`,
`SetDraw`,
`SetLineWidth`

## Module

Foundation
