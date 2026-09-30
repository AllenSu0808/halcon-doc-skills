# disp_cross (Operator)

## Name

`disp_cross` — Displays crosses in a window.

## Signature

`def disp_cross(window_handle: HHandle, row: MaybeSequence[float], column: MaybeSequence[float], size: float, angle: float) -> None`

## Description

`disp_cross` displays one or several crosses in the output
window. A cross is described by the coordinates of the center point
(*`row`*,*`column`*), the length of its bars *`size`* and the
orientation *`angle`*.
The operators used to control the display of regions
(e.g., [`set_color`](set_color.md), [`set_gray`](set_gray.md), [`set_draw`](set_draw.md),
[`set_line_width`](set_line_width.md)) can also be used with crosses. Several crosses can
be displayed with one call by using tuple parameters. For the use of colors
with several crosses, see [`set_color`](set_color.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`row`** (input_control)  coordinates.y(-array) `→` MaybeSequence[float]

Row coordinate of the center.

Default:
32.0

Suggested values:
0.0, 64.0, 128.0, 256.0, 511.0

**`column`** (input_control)  coordinates.x(-array) `→` MaybeSequence[float]

Column coordinate of the center.

Default:
32.0

Suggested values:
0.0, 64.0, 128.0, 256.0, 511.0

**`size`** (input_control)  number `→` float

Length of the bars.

Default:
6.0

Suggested values:
4.0, 6.0, 8.0, 10.0

Value range:
`0.0
≤
size`

**`angle`** (input_control)  angle.rad `→` float

Orientation.

Default:
0.0

Suggested values:
0.0, 0.78539816339744830961566084581988

## Result

`disp_cross` returns 2 (
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
`disp_circle`

## See also

`open_window`,
`set_color`,
`set_rgb`,
`set_hsi`,
`set_line_width`

## Module

Foundation
