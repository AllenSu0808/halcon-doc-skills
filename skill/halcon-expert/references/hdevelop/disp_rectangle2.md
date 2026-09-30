# disp_rectangle2 (Operator)

## Name

`disp_rectangle2` — Displays arbitrarily oriented rectangles.

## Signature

`disp_rectangle2( : : WindowHandle, CenterRow, CenterCol, Phi, Length1, Length2 : )`

## Description

`disp_rectangle2` draws one or several arbitrarily oriented
rectangles in the output window. A rectangle is described by the
center (*`CenterRow`*,*`CenterCol`*), the orientation
*`Phi`* (in radians) and half the lengths of the edges
*`Length1`* and *`Length2`*. The operators used to control
the display of regions (e.g., [`set_draw`](set_draw.md), [`set_gray`](set_gray.md),
[`set_draw`](set_draw.md)) can also be used with rectangles. Several
rectangles can be displayed with one call by using tuple
parameters. For the use of colors with several rectangles, see
[`set_color`](set_color.md).

## Attention

The center must lie within the window boundaries.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`CenterRow`** (input_control)  rectangle2.center.y(-array) `→`  (real / integer)

Row index of the center.

Default:
48

Suggested values:
0, 64, 128, 256, 511

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

**`CenterCol`** (input_control)  rectangle2.center.x(-array) `→`  (real / integer)

Column index of the center.

Default:
64

Suggested values:
0, 64, 128, 256, 511

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

**`Phi`** (input_control)  rectangle2.angle.rad(-array) `→`  (real / integer)

Orientation of rectangle in radians.

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

**`Length1`** (input_control)  rectangle2.hwidth(-array) `→`  (real / integer)

Half of the length of the longer side.

Default:
48

Suggested values:
0, 64, 128, 256, 511

Value range:
`0
≤
Length1
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

**`Length2`** (input_control)  rectangle2.hheight(-array) `→`  (real / integer)

Half of the length of the shorter side.

Default:
32

Suggested values:
0, 64, 128, 256, 511

Value range:
`0
≤
Length2
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

`disp_rectangle2` returns 2 (
H_MSG_TRUE)
, if the
parameters are correct. Otherwise an exception is raised.

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

`disp_region`,
`gen_rectangle2`,
`disp_rectangle1`,
`set_shape`

## See also

`open_window`,
`disp_region`,
`set_color`,
`set_draw`,
`set_line_width`

## Module

Foundation
