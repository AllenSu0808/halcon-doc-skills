# get_window_extents (Operator)

## Name

`get_window_extents` — Information about a window's size and position.

## Signature

`def get_window_extents(window_handle: HHandle) -> Tuple[int, int, int, int]`

## Description

`get_window_extents` returns the position of the upper left
corner, as well as width and height of the output window.

## Attention

Size and position of a window may be modified by the window manager, without
explicit instruction in the program. Therefore the values which are returned by
`get_window_extents` may change cause of side effects.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`row`** (output_control)  rectangle.origin.y `→` int

Row index of upper left corner of the window.

**`column`** (output_control)  rectangle.origin.x `→` int

Column index of upper left corner of the window.

**`width`** (output_control)  rectangle.extent.x `→` int

Window width.

**`height`** (output_control)  rectangle.extent.y `→` int

Window height.

## Result

If the window is valid `get_window_extents` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`open_window`,
`set_draw`,
`set_color`,
`set_colored`,
`set_line_width`

## See also

`set_window_extents`,
`open_window`

## Module

Foundation
