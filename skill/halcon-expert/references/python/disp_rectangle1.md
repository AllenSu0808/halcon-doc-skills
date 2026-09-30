# disp_rectangle1 (Operator)

## Name

`disp_rectangle1` — Display of rectangles aligned to the coordinate axes.

## Signature

`def disp_rectangle1(window_handle: HHandle, row_1: MaybeSequence[Union[int, float]], column_1: MaybeSequence[Union[int, float]], row_2: MaybeSequence[Union[int, float]], column_2: MaybeSequence[Union[int, float]]) -> None`

## Description

`disp_rectangle1` displays one or several rectangles in the
output window. A rectangle is described by the upper left corner
(*`row_1`*,*`column_1`*) and the lower right corner
(*`row_2`*,*`column_2`*). If the given coordinates are not
within the boundary of the window the rectangle is clipped accordingly.
The operators used to control the display of regions
(e.g., [`set_color`](set_color.md), [`set_gray`](set_gray.md), [`set_draw`](set_draw.md),
[`set_line_width`](set_line_width.md)) can also be used with rectangles. Several
rectangles can be displayed with one call by using tuple parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`row_1`** (input_control)  rectangle.origin.y(-array) `→` MaybeSequence[Union[int, float]]

Row index of the upper left corner.

Default:
16

Suggested values:
0, 64, 128, 256, 511

Value range:
`0
≤
row_1
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

**`column_1`** (input_control)  rectangle.origin.x(-array) `→` MaybeSequence[Union[int, float]]

Column index of the upper left corner.

Default:
16

Suggested values:
0, 64, 128, 256, 511

Value range:
`0
≤
column_1
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

**`row_2`** (input_control)  rectangle.corner.y(-array) `→` MaybeSequence[Union[int, float]]

Row index of the lower right corner.

Default:
48

Suggested values:
0, 64, 128, 256, 511

Value range:
`0
≤
row_2
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

Restriction:
`Row2 >= Row1`

**`column_2`** (input_control)  rectangle.corner.x(-array) `→` MaybeSequence[Union[int, float]]

Column index of the lower right corner.

Default:
80

Suggested values:
0, 64, 128, 256, 511

Value range:
`0
≤
column_2
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

Restriction:
`Column2 >= Column1`

## Example (HDevelop)

```
set_color(WindowHandle,'green')
draw_region(MyRegion,WindowHandle)
smallest_rectangle1(MyRegion,R1,C1,R2,C2)
disp_rectangle1(WindowHandle,R1,C1,R2,C2)
```

## Result

`disp_rectangle1` returns 2 (
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

`disp_rectangle2`,
`gen_rectangle1`,
`disp_region`,
`disp_line`,
`set_shape`

## See also

`open_window`,
`set_color`,
`set_draw`,
`set_line_width`

## Module

Foundation
