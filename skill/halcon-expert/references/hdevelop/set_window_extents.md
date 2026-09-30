# set_window_extents (Operator)

## Name

`set_window_extents` — Modify position and size of a window.

## Signature

`set_window_extents( : : WindowHandle, Row, Column, Width, Height : )`

## Description

`set_window_extents` positions the upper left corner of the
output window at (*`Row`*,*`Column`*) and changes the size of the
window to *`Width`* and *`Height`* at the same time. Negative
values for *`Width`* and *`Height`* are ignored.

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

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Row`** (input_control)  rectangle.origin.y `→`  (integer)

Row index of upper left corner in target position.

Default:
0

Value range:
`Row` (lin)

Minimum increment:
1

Recommended increment:
1

**`Column`** (input_control)  rectangle.origin.x `→`  (integer)

Column index of upper left corner in target position.

Default:
0

Value range:
`Column` (lin)

Minimum increment:
1

Recommended increment:
1

**`Width`** (input_control)  rectangle.extent.x `→`  (integer)

Width of the window.

Default:
512

Value range:
`Width` (lin)

Minimum increment:
1

Recommended increment:
1

**`Height`** (input_control)  rectangle.extent.y `→`  (integer)

Height of the window.

Default:
512

Value range:
`Height` (lin)

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
