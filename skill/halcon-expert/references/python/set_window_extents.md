# set_window_extents (Operator)

## Name

`set_window_extents` — Modify position and size of a window.

## Signature

`def set_window_extents(window_handle: HHandle, row: int, column: int, width: int, height: int) -> None`

## Description

`set_window_extents` positions the upper left corner of the
output window at (*`row`*,*`column`*) and changes the size of the
window to *`width`* and *`height`* at the same time. Negative
values for *`width`* and *`height`* are ignored.

Adapting the size of the window to the size of the image part to be
displayed will prevent slowing down the display due to necessary
interpolations.
Thus, the window preferably has the same size as the image part to be
displayed, or otherwise half its size, quarter its size, etc.

## Attention

Modifying the size of the window does not automatically redraw the window
contents. This has to be done by the program by redisplaying the desired
data.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`row`** (input_control)  rectangle.origin.y `→` int

Row index of upper left corner in target position.

Default:
0

Value range:
`row` (lin)

Minimum increment:
1

Recommended increment:
1

**`column`** (input_control)  rectangle.origin.x `→` int

Column index of upper left corner in target position.

Default:
0

Value range:
`column` (lin)

Minimum increment:
1

Recommended increment:
1

**`width`** (input_control)  rectangle.extent.x `→` int

Width of the window.

Default:
512

Value range:
`width` (lin)

Minimum increment:
1

Recommended increment:
1

**`height`** (input_control)  rectangle.extent.y `→` int

Height of the window.

Default:
512

Value range:
`height` (lin)

Minimum increment:
1

Recommended increment:
1

## Result

If the window is valid and the parameters are correct
`set_window_extents` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`open_window`

## See also

`get_window_extents`,
`open_window`

## Module

Foundation
