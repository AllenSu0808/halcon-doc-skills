# DispEllipse (Operator)

## Name

`DispEllipse` — Displays ellipses.

## Signature

`static void HOperatorSet.DispEllipse(HTuple windowHandle, HTuple centerRow, HTuple centerCol, HTuple phi, HTuple radius1, HTuple radius2)`

`void HWindow.DispEllipse(HTuple centerRow, HTuple centerCol, HTuple phi, HTuple radius1, HTuple radius2)`

`void HWindow.DispEllipse(int centerRow, int centerCol, double phi, double radius1, double radius2)`

## Description

`DispEllipse` displays one or several ellipses in the
output window. An ellipse is described by the center (*`centerRow`*,
*`centerCol`*), the orientation *`phi`* (in radians) and the
radii of the major and the minor axis (*`radius1`* and
*`radius2`*).

The operators used to control the display of regions
(e.g., [`SetDraw`](set_draw.md), [`SetGray`](set_gray.md), [`SetDraw`](set_draw.md))
can also be used with ellipses. Several ellipses can be displayed
with one call by using tuple parameters. For the use of colors with
several ellipses, see [`SetColor`](set_color.md).

## Attention

The center of the ellipse must be within the window.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`centerRow`** (input_control)  ellipse.center.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Row index of center.

Default:
64

Suggested values:
0, 64, 128, 256

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

**`centerCol`** (input_control)  ellipse.center.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Column index of center.

Default:
64

Suggested values:
0, 64, 128, 256

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

**`phi`** (input_control)  ellipse.angle.rad(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Orientation of the ellipse in radians

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

**`radius1`** (input_control)  ellipse.radius1(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Radius of major axis.

Default:
24.0

Suggested values:
0.0, 64.0, 128.0, 256.0

Value range:
`0.0
≤
radius1
≤
511.0` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`radius2`** (input_control)  ellipse.radius2(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Radius of minor axis.

Default:
14.0

Suggested values:
0.0, 64.0, 128.0, 256.0

Value range:
`0.0
≤
radius2
≤
511.0` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

## Example (HDevelop)

```
set_color(WindowHandle,'red')
draw_region(MyRegion,WindowHandle)
elliptic_axis(MyRegion,Ra,Rb,Phi)
area_center(MyRegion,_,Row,Column)
disp_ellipse(WindowHandle,Row,Column,Phi,Ra,Rb)
```

## Result

`DispEllipse` returns 2 (
H_MSG_TRUE)
, if the
parameters are correct. Otherwise an exception is raised.

## Possible Predecessors

`OpenWindow`,
`SetDraw`,
`SetColor`,
`SetColored`,
`SetLineWidth`,
`SetRgb`,
`SetHsi`,
`EllipticAxis`,
`AreaCenter`

## Alternatives

`DispCircle`,
`DispRegion`,
`GenEllipse`,
`GenCircle`

## See also

`OpenWindow`,
`SetColor`,
`SetRgb`,
`SetHsi`,
`SetDraw`,
`SetLineWidth`

## Module

Foundation
