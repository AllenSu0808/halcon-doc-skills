# disp_arc (Operator)

## Name

`disp_arc` — Displays circular arcs in a window.

## Signature

`disp_arc( : : WindowHandle, CenterRow, CenterCol, Angle, BeginRow, BeginCol : )`

## Description

`disp_arc` displays one or several circular arcs in the
output window. An arc is described by its center point
(*`CenterRow`*,*`CenterCol`*), the angle between start and end
of the arc (*`Angle`* in radians) and the first point of the arc
(*`BeginRow`*,*`BeginCol`*). The arc is displayed in clockwise
direction. The parameters for output can be determined - as with the output
of regions - with the operators [`set_color`](set_color.md), [`set_gray`](set_gray.md),
[`set_draw`](set_draw.md), etc. It is possible to draw several arcs with
one call by using tuple parameters. For the use of colors with
several arcs, see [`set_color`](set_color.md).

## Attention

The center point has to be within the window. The radius of the arc has be
at least 2 pixel.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`CenterRow`** (input_control)  arc.center.y `→`  (real / integer)

Row coordinate of center point.

Default:
64

Suggested values:
0, 64, 128, 256

Value range:
`0
≤
CenterRow
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`CenterCol`** (input_control)  arc.center.x `→`  (real / integer)

Column coordinate of center point.

Default:
64

Suggested values:
0, 64, 128, 256

Value range:
`0
≤
CenterCol
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`Angle`** (input_control)  arc.angle.rad `→`  (real / integer)

Angle between start and end of the arc (in radians).

Default:
3.1415926

Suggested values:
0.0, 0.785398, 1.570796, 3.1415926, 6.283185

Value range:
`0.0
≤
Angle
≤
6.283185` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

Restriction:
`Angle > 0.0`

**`BeginRow`** (input_control)  arc.begin.y(-array) `→`  (integer / real)

Row coordinate of the start of the arc.

Default:
32

Suggested values:
0, 64, 128, 256

Value range:
`0
≤
BeginRow
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`BeginCol`** (input_control)  arc.begin.x(-array) `→`  (integer / real)

Column coordinate of the start of the arc.

Default:
32

Suggested values:
0, 64, 128, 256

Value range:
`0
≤
BeginCol
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

`disp_arc` returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`open_window`,
`set_draw`,
`set_color`,
`set_colored`,
`set_line_width`,
`set_rgb`,
`set_hsi`

## Alternatives

`disp_circle`,
`disp_ellipse`,
`disp_region`,
`gen_circle`,
`gen_ellipse`

## See also

`open_window`,
`set_color`,
`set_draw`,
`set_rgb`,
`set_hsi`

## Module

Foundation
