# disp_ellipse (Operator)

## Name

`disp_ellipse` — Displays ellipses.

## Signature

`disp_ellipse( : : WindowHandle, CenterRow, CenterCol, Phi, Radius1, Radius2 : )`

## Description

`disp_ellipse` displays one or several ellipses in the
output window. An ellipse is described by the center (*`CenterRow`*,
*`CenterCol`*), the orientation *`Phi`* (in radians) and the
radii of the major and the minor axis (*`Radius1`* and
*`Radius2`*).

The operators used to control the display of regions
(e.g., [`set_draw`](set_draw.md), [`set_gray`](set_gray.md), [`set_draw`](set_draw.md))
can also be used with ellipses. Several ellipses can be displayed
with one call by using tuple parameters. For the use of colors with
several ellipses, see [`set_color`](set_color.md).

## Attention

The center of the ellipse must be within the window.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`CenterRow`** (input_control)  ellipse.center.y(-array) `→`  (integer)

Row index of center.

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
10

**`CenterCol`** (input_control)  ellipse.center.x(-array) `→`  (integer)

Column index of center.

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
10

**`Phi`** (input_control)  ellipse.angle.rad(-array) `→`  (real / integer)

Orientation of the ellipse in radians

Default:
0.0

Suggested values:
0.0, 0.785398, 1.570796, 3.1415926, 6.283185

Value range:
`0.0
≤
Phi
≤
6.283185` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`Radius1`** (input_control)  ellipse.radius1(-array) `→`  (real / integer)

Radius of major axis.

Default:
24.0

Suggested values:
0.0, 64.0, 128.0, 256.0

Value range:
`0.0
≤
Radius1
≤
511.0` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`Radius2`** (input_control)  ellipse.radius2(-array) `→`  (real / integer)

Radius of minor axis.

Default:
14.0

Suggested values:
0.0, 64.0, 128.0, 256.0

Value range:
`0.0
≤
Radius2
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

`disp_ellipse` returns 2 (
H_MSG_TRUE)
, if the
parameters are correct. Otherwise an exception is raised.

## Possible Predecessors

`open_window`,
`set_draw`,
`set_color`,
`set_colored`,
`set_line_width`,
`set_rgb`,
`set_hsi`,
`elliptic_axis`,
`area_center`

## Alternatives

`disp_circle`,
`disp_region`,
`gen_ellipse`,
`gen_circle`

## See also

`open_window`,
`set_color`,
`set_rgb`,
`set_hsi`,
`set_draw`,
`set_line_width`

## Module

Foundation
