# draw_point_mod (Operator)

## Name

`draw_point_mod` — Draw a point.

## Signature

`def draw_point_mod(window_handle: HHandle, row_in: float, column_in: float) -> Tuple[float, float]`

## Description

`draw_point_mod` returns the parameter for a point, which has been
created interactively by the user in the window.

To create a point are expected the coordinates *`row_in`* and
*`column_in`*.
While keeping the button pressed you may “drag” the point in any direction.
Pressing the right mouse button terminates the procedure.

After terminating the procedure the point is not visible in the window any longer.

## Attention

If used in a buffer window, mouse events have to be supplied by the
application, while the draw operator must be run in another thread.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`row_in`** (input_control)  point.y `→` float

Row index of the point.

**`column_in`** (input_control)  point.x `→` float

Column index of the point.

**`row`** (output_control)  point.y `→` float

Row index of the point.

**`column`** (output_control)  point.x `→` float

Column index of the point.

## Result

`draw_point_mod` returns 2 (
H_MSG_TRUE)
if the window is valid.
If necessary, an exception is raised.

## Possible Predecessors

`open_window`

## Possible Successors

`reduce_domain`,
`disp_line`,
`set_colored`,
`set_line_width`,
`set_draw`

## See also

`draw_point`,
`draw_circle`,
`draw_ellipse`

## Module

Foundation
