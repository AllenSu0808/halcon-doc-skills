# disp_circle (Operator)

## Name

`disp_circle` — Displays circles in a window.

## Signature

`disp_circle( : : WindowHandle, Row, Column, Radius : )`

## Description

`disp_circle` displays one or several circles in the
output window. A circle is described by the center (*`Row`*,
*`Column`*) and the radius *`Radius`*.
If the used coordinates are not within the window the circle is
clipped accordingly.

The operators used to control the display of regions
(e.g., [`set_draw`](set_draw.md), [`set_gray`](set_gray.md), [`set_draw`](set_draw.md))
can also be used with circles. Several circles can be displayed with
one call by using tuple parameters. For the use of colors with
several circles, see [`set_color`](set_color.md).

## Attention

The center of the circle must be within the window.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Row`** (input_control)  circle.center.y(-array) `→`  (real / integer)

Row index of the center.

Default:
64

Suggested values:
0, 64, 128, 256

Value range:
`0
≤
Row
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`Column`** (input_control)  circle.center.x(-array) `→`  (real / integer)

Column index of the center.

Default:
64

Suggested values:
0, 64, 128, 256

Value range:
`0
≤
Column
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`Radius`** (input_control)  circle.radius(-array) `→`  (real / integer)

Radius of the circle.

Default:
64

Suggested values:
0, 64, 128, 256

Value range:
`0
≤
Radius
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

Restriction:
`Radius > 0.0`

## Example (HDevelop)

```
open_window(0,0,-1,-1,'root','visible','',WindowHandle)
set_draw(WindowHandle,'fill')
set_color(WindowHandle,'white')
repeat
  get_mbutton(WindowHandle,Row,Column,Button)
  disp_circle(WindowHandle,Row,Column,(Row + Column) % 50)
until(Button == 1)
close_window(WindowHandle)
```

## Result

`disp_circle` returns 2 (
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
