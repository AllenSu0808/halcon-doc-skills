# disp_arrow (Operator)

## Name

`disp_arrow` — Displays arrows in a window.

## Signature

`def disp_arrow(window_handle: HHandle, row_1: MaybeSequence[Union[int, float]], column_1: MaybeSequence[Union[int, float]], row_2: MaybeSequence[Union[int, float]], column_2: MaybeSequence[Union[int, float]], size: Union[int, float]) -> None`

## Description

`disp_arrow` displays one or several arrows in the output
window. An arrow is described by the coordinates of the start
(*`row_1`*,*`column_1`*) and the end
(*`row_2`*,*`column_2`*). An arrowhead is displayed at the end
of the arrow. The size of the arrowhead is specified by the parameter
*`size`*. If the arrow consists of just one point (start = end)
nothing is displayed. The operators used to control the display of regions
(e.g., [`set_draw`](set_draw.md), [`set_color`](set_color.md),
[`set_line_width`](set_line_width.md)) can also be used with arrows. Several arrows
can be displayed with one call by using tuple parameters. For the use of
colors with several arcs, see [`set_color`](set_color.md).

## Attention

The start and the end of the arrows must fall within the window.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`row_1`** (input_control)  line.begin.y(-array) `→` MaybeSequence[Union[int, float]]

Row index of the start.

Default:
10.0

Suggested values:
0.0, 64.0, 128.0, 256.0

Value range:
`0.0
≤
row_1
≤
511.0` (lin)

Minimum increment:
1.0

Recommended increment:
1.0

**`column_1`** (input_control)  line.begin.x(-array) `→` MaybeSequence[Union[int, float]]

Column index of the start.

Default:
10.0

Suggested values:
0.0, 64.0, 128.0, 256.0

Value range:
`0.0
≤
column_1
≤
511.0` (lin)

Minimum increment:
1.0

Recommended increment:
1.0

**`row_2`** (input_control)  line.end.y(-array) `→` MaybeSequence[Union[int, float]]

Row index of the end.

Default:
118.0

Suggested values:
0.0, 64.0, 128.0, 256.0

Value range:
`0.0
≤
row_2
≤
511.0` (lin)

Minimum increment:
1.0

Recommended increment:
1.0

**`column_2`** (input_control)  line.end.x(-array) `→` MaybeSequence[Union[int, float]]

Column index of the end.

Default:
118.0

Suggested values:
0.0, 64.0, 128.0, 256.0

Value range:
`0.0
≤
column_2
≤
511.0` (lin)

Minimum increment:
1.0

Recommended increment:
1.0

**`size`** (input_control)  number `→` Union[int, float]

Size of the arrowhead.

Default:
1.0

Suggested values:
1.0, 2.0, 3.0, 5.0

Value range:
`0.0
≤
size
≤
20.0` (lin)

Minimum increment:
1.0

Recommended increment:
1.0

Restriction:
`Size > 0.0`

## Example (HDevelop)

```
set_color(WindowHandle,['red','green'])
disp_arrow(WindowHandle,[10,10],[10,10],[118,110],[118,118],1.0)
```

## Result

`disp_arrow` returns 2 (
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

`disp_line`,
`gen_region_polygon`,
`disp_region`

## See also

`open_window`,
`set_color`,
`set_draw`,
`set_line_width`

## Module

Foundation
