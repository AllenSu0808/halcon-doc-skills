# disp_ellipse (Operator)

## Name

`disp_ellipse` — Displays ellipses.

## Signature

`def disp_ellipse(window_handle: HHandle, center_row: MaybeSequence[int], center_col: MaybeSequence[int], phi: MaybeSequence[Union[int, float]], radius_1: MaybeSequence[Union[int, float]], radius_2: MaybeSequence[Union[int, float]]) -> None`

## Description

`disp_ellipse` displays one or several ellipses in the
output window. An ellipse is described by the center (*`center_row`*,
*`center_col`*), the orientation *`phi`* (in radians) and the
radii of the major and the minor axis (*`radius_1`* and
*`radius_2`*).

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

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`center_row`** (input_control)  ellipse.center.y(-array) `→` MaybeSequence[int]

Row index of center.

Default:
64

Suggested values:
0, 64, 128, 256

Value range:
`0
≤
center_row
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

**`center_col`** (input_control)  ellipse.center.x(-array) `→` MaybeSequence[int]

Column index of center.

Default:
64

Suggested values:
0, 64, 128, 256

Value range:
`0
≤
center_col
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

**`phi`** (input_control)  ellipse.angle.rad(-array) `→` MaybeSequence[Union[int, float]]

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

**`radius_1`** (input_control)  ellipse.radius1(-array) `→` MaybeSequence[Union[int, float]]

Radius of major axis.

Default:
24.0

Suggested values:
0.0, 64.0, 128.0, 256.0

Value range:
`0.0
≤
radius_1
≤
511.0` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`radius_2`** (input_control)  ellipse.radius2(-array) `→` MaybeSequence[Union[int, float]]

Radius of minor axis.

Default:
14.0

Suggested values:
0.0, 64.0, 128.0, 256.0

Value range:
`0.0
≤
radius_2
≤
511.0` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

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
