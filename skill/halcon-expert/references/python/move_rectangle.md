# move_rectangle (Operator)

## Name

`move_rectangle` — Copy inside an output window.

## Warning

**`move_rectangle` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def move_rectangle(window_handle: HHandle, row_1: MaybeSequence[int], column_1: MaybeSequence[int], row_2: MaybeSequence[int], column_2: MaybeSequence[int], dest_row: MaybeSequence[int], dest_column: MaybeSequence[int]) -> None`

## Description

`move_rectangle` copies all entries in the rectangle
(*`row_1`*,*`column_1`*), (*`row_2`*,*`column_2`*)
of the output window to a new position inside the same window.
This position is determined by the upper left corner (*`dest_row`*,
*`dest_column`*).
Regions of the window, which are “uncovered” through moving the rectangle,
are set to the color of the background.

If you want to move several rectangles at once, you may pass parameters
in form of tuples.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`row_1`** (input_control)  rectangle.origin.y(-array) `→` MaybeSequence[int]

Row index of upper left corner of the source rectangle.

Default:
0

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

Column index of upper left corner of the source rectangle.

Default:
0

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

Row index of lower right corner of the source rectangle.

Default:
64

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

**`column_2`** (input_control)  rectangle.corner.x(-array) `→` MaybeSequence[int]

Column index of lower right corner of the source rectangle.

Default:
64

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

**`dest_row`** (input_control)  point.y(-array) `→` MaybeSequence[int]

Row index of upper left corner of the target position.

Default:
64

Value range:
`0
≤
dest_row
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`dest_column`** (input_control)  point.x(-array) `→` MaybeSequence[int]

Column index of upper left corner of the target position.

Default:
64

Value range:
`0
≤
dest_column
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

## Result

If the window is valid and the specified parameters are correct
`move_rectangle` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`open_window`

## Alternatives

`copy_rectangle`

## See also

`open_window`

## Module

Foundation
