# DispArc (Operator)

## Name

`DispArc` — Displays circular arcs in a window.

## Signature

`static void HOperatorSet.DispArc(HTuple windowHandle, HTuple centerRow, HTuple centerCol, HTuple angle, HTuple beginRow, HTuple beginCol)`

`void HWindow.DispArc(HTuple centerRow, HTuple centerCol, HTuple angle, HTuple beginRow, HTuple beginCol)`

`void HWindow.DispArc(double centerRow, double centerCol, double angle, int beginRow, int beginCol)`

## Description

`DispArc` displays one or several circular arcs in the
output window. An arc is described by its center point
(*`centerRow`*,*`centerCol`*), the angle between start and end
of the arc (*`angle`* in radians) and the first point of the arc
(*`beginRow`*,*`beginCol`*). The arc is displayed in clockwise
direction. The parameters for output can be determined - as with the output
of regions - with the operators [`SetColor`](set_color.md), [`SetGray`](set_gray.md),
[`SetDraw`](set_draw.md), etc. It is possible to draw several arcs with
one call by using tuple parameters. For the use of colors with
several arcs, see [`SetColor`](set_color.md).

## Attention

The center point has to be within the window. The radius of the arc has be
at least 2 pixel.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`centerRow`** (input_control)  arc.center.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of center point.

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
1

**`centerCol`** (input_control)  arc.center.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of center point.

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
1

**`angle`** (input_control)  arc.angle.rad `→` [HTuple](HTuple.md) (*double* / int / long)

Angle between start and end of the arc (in radians).

Default:
3.1415926

Suggested values:
0.0, 0.785398, 1.570796, 3.1415926, 6.283185

Value range:
`0.0
≤
angle
≤
6.283185` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

Restriction:
`Angle > 0.0`

**`beginRow`** (input_control)  arc.begin.y(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

Row coordinate of the start of the arc.

Default:
32

Suggested values:
0, 64, 128, 256

Value range:
`0
≤
beginRow
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`beginCol`** (input_control)  arc.begin.x(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

Column coordinate of the start of the arc.

Default:
32

Suggested values:
0, 64, 128, 256

Value range:
`0
≤
beginCol
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

## Example (HDevelop)

```
open_window(0,0,-1,-1,'root','visible','',WindowHandle)
set_draw(WindowHandle,'fill')
set_color(WindowHandle,'white')
Row := 100
Column := 100
disp_arc(WindowHandle,Row,Column,3.14,Row+10,Column+10)
close_window(WindowHandle)
```

## Result

`DispArc` returns 2 (
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

`DispCircle`,
`DispEllipse`,
`DispRegion`,
`GenCircle`,
`GenEllipse`

## See also

`OpenWindow`,
`SetColor`,
`SetDraw`,
`SetRgb`,
`SetHsi`

## Module

Foundation
