# DispRectangle2 (Operator)

## Name

`DispRectangle2` — Displays arbitrarily oriented rectangles.

## Signature

`static void HOperatorSet.DispRectangle2(HTuple windowHandle, HTuple centerRow, HTuple centerCol, HTuple phi, HTuple length1, HTuple length2)`

`void HWindow.DispRectangle2(HTuple centerRow, HTuple centerCol, HTuple phi, HTuple length1, HTuple length2)`

`void HWindow.DispRectangle2(double centerRow, double centerCol, double phi, double length1, double length2)`

## Description

`DispRectangle2` draws one or several arbitrarily oriented
rectangles in the output window. A rectangle is described by the
center (*`centerRow`*,*`centerCol`*), the orientation
*`phi`* (in radians) and half the lengths of the edges
*`length1`* and *`length2`*. The operators used to control
the display of regions (e.g., [`SetDraw`](set_draw.md), [`SetGray`](set_gray.md),
[`SetDraw`](set_draw.md)) can also be used with rectangles. Several
rectangles can be displayed with one call by using tuple
parameters. For the use of colors with several rectangles, see
[`SetColor`](set_color.md).

## Attention

The center must lie within the window boundaries.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`centerRow`** (input_control)  rectangle2.center.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row index of the center.

Default:
48

Suggested values:
0, 64, 128, 256, 511

Value range:
`0
≤
centerRow
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

**`centerCol`** (input_control)  rectangle2.center.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column index of the center.

Default:
64

Suggested values:
0, 64, 128, 256, 511

Value range:
`0
≤
centerCol
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

**`phi`** (input_control)  rectangle2.angle.rad(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Orientation of rectangle in radians.

Default:
0.0

Suggested values:
0.0, 0.785398, 1.570796, 3.1415926, 6.283185

Value range:
`0.0
≤
phi
≤
6.283185` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`length1`** (input_control)  rectangle2.hwidth(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Half of the length of the longer side.

Default:
48

Suggested values:
0, 64, 128, 256, 511

Value range:
`0
≤
length1
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

**`length2`** (input_control)  rectangle2.hheight(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Half of the length of the shorter side.

Default:
32

Suggested values:
0, 64, 128, 256, 511

Value range:
`0
≤
length2
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

Restriction:
`Length2 < Length1`

## Example (HDevelop)

```
set_color(WindowHandle,'green')
draw_region(MyRegion,WindowHandle)
elliptic_axis(MyRegion,Ra,Rb,Phi)
area_center(MyRegion,_,Row,Column)
disp_rectangle2(WindowHandle,Row,Column,Phi,Ra,Rb)
```

## Result

`DispRectangle2` returns 2 (
H_MSG_TRUE)
, if the
parameters are correct. Otherwise an exception is raised.

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

`DispRegion`,
`GenRectangle2`,
`DispRectangle1`,
`SetShape`

## See also

`OpenWindow`,
`DispRegion`,
`SetColor`,
`SetDraw`,
`SetLineWidth`

## Module

Foundation
