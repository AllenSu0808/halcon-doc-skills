# copy_rectangle (Operator)

## Name

`copy_rectangle` — Copy all pixels within rectangles between output windows.

## Signature

`def copy_rectangle(window_handle_source: HHandle, window_handle_destination: HHandle, row_1: MaybeSequence[int], column_1: MaybeSequence[int], row_2: MaybeSequence[int], column_2: MaybeSequence[int], dest_row: MaybeSequence[int], dest_column: MaybeSequence[int]) -> None`

## Description

`copy_rectangle` copies all pixels from the window
*`window_handle_source`* in the
window
*`window_handle_destination`*. It copies pixels which reside
inside a rectangle which is specified by parameters *`row_1`*,
*`column_1`*, *`row_2`* and *`column_2`*. The target
position is specified through the upper left corner of the rectangle
(*`dest_row`*, *`dest_column`*).

If you want to move more than one rectangle, you may pass them at
once (in form of the tuple mode).

You may use `copy_rectangle` to copy edited graphics from an
“invisible” window in a visible window. Therefore a window with
the option 'buffer' is opened. The graphics is then displayed in
this window and is copied in a visible window afterwards. The
advantage of this strategy is, that `copy_rectangle` is much
more rapid than output operators as, e.g., [`disp_channel`](disp_channel.md). This
means a particular advantage while using demo programs. You could
even realize short “clips”: you have to create for every image of
a sequence a window of a 'buffer' type and pass the data into
it. Output is the image sequence whereat all buffers are copied one
after another in a visible window.

## Attention

Both windows have to reside on the same display.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle_source`** (input_control)  window `→` HHandle

Source window handle.

**`window_handle_destination`** (input_control)  window `→` HHandle

Destination window handle.

**`row_1`** (input_control)  rectangle.origin.y(-array) `→` MaybeSequence[int]

Row index of upper left corner in the source window.

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

Column index of upper left corner in the source window.

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

Row index of lower right corner in the source window.

Default:
128

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
`Row2 >= Row1`

**`column_2`** (input_control)  rectangle.corner.x(-array) `→` MaybeSequence[int]

Column index of lower right corner in the source window.

Default:
128

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

**`dest_row`** (input_control)  point.y(-array) `→` MaybeSequence[int]

Row index of upper left corner in the target window.

Default:
0

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

Column index of upper left corner in the target window.

Default:
0

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

If the output window is valid and if the specified parameters are correct
[`close_window`](close_window.md) returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`open_window`

## Possible Successors

`close_window`

## Alternatives

`move_rectangle`,
`slide_image`

## See also

`open_window`

## Module

Foundation
