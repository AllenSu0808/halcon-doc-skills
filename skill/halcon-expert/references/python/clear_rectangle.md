# clear_rectangle (Operator)

## Name

`clear_rectangle` — Delete a rectangle on the output window.

## Warning

**`clear_rectangle` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def clear_rectangle(window_handle: HHandle, row_1: MaybeSequence[int], column_1: MaybeSequence[int], row_2: MaybeSequence[int], column_2: MaybeSequence[int]) -> None`

## Description

`clear_rectangle` deletes all entries in the rectangle which
is defined through the upper left corner
(*`row_1`*,*`column_1`*) and the lower right corner
(*`row_2`*,*`column_2`*). Deletion means that the
specified rectangle is set to the background color (see
[`open_window`](open_window.md)).

If you want to delete more than one rectangle, you may pass several
rectangles, i.e., the parameters *`row_1`*, *`column_1`*,
*`row_2`* and *`column_2`* are tuples.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`row_1`** (input_control)  rectangle.origin.y(-array) `→` MaybeSequence[int]

Line index of upper left corner.

Default:
10

Value range:
`0
≤
row_1
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`column_1`** (input_control)  rectangle.origin.x(-array) `→` MaybeSequence[int]

Column index of upper left corner.

Default:
10

Value range:
`0
≤
column_1
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`row_2`** (input_control)  rectangle.corner.y(-array) `→` MaybeSequence[int]

Row index of lower right corner.

Default:
118

Value range:
`0
≤
row_2
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

Restriction:
`Row2 > Row1`

**`column_2`** (input_control)  rectangle.corner.x(-array) `→` MaybeSequence[int]

Column index of lower right corner.

Default:
118

Value range:
`0
≤
column_2
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

Restriction:
`Column2 >= Column1`

## Result

If an output window exists and the specified parameters are correct
`clear_rectangle` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`open_window`,
`set_draw`,
`set_color`,
`set_colored`,
`set_line_width`,
`set_rgb`,
`set_hsi`,
`draw_rectangle1`

## Alternatives

`clear_window`,
`disp_rectangle1`

## See also

`open_window`

## Module

Foundation
