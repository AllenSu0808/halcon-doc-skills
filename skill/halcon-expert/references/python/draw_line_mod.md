# draw_line_mod (Operator)

## Name

`draw_line_mod` — Draw a line.

## Signature

`def draw_line_mod(window_handle: HHandle, row_1in: float, column_1in: float, row_2in: float, column_2in: float) -> Tuple[float, float, float, float]`

## Description

`draw_line_mod` returns the parameter for a line, which has been
created interactively by the user in the window.

To create a line are expected the coordinates of the start point
*`row_1in`*, *`column_1in`* and of the end point
*`row_2in`*,*`column_2in`*.
If you click on one end point of the created line, you may move this point.
After another mouse click in the middle of the created line
you can move it.

Pressing the right mouse button terminates the procedure.

After terminating the procedure the line is not visible in the window any longer.

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

**`row_1in`** (input_control)  line.begin.y `→` float

Row index of the first point of the line.

**`column_1in`** (input_control)  line.begin.x `→` float

Column index of the first point of the line.

**`row_2in`** (input_control)  line.end.y `→` float

Row index of the second point of the line.

**`column_2in`** (input_control)  line.end.x `→` float

Column index of the second point of the line.

**`row_1`** (output_control)  line.begin.y `→` float

Row index of the first point of the line.

**`column_1`** (output_control)  line.begin.x `→` float

Column index of the first point of the line.

**`row_2`** (output_control)  line.end.y `→` float

Row index of the second point of the line.

**`column_2`** (output_control)  line.end.x `→` float

Column index of the second point of the line.

## Result

`draw_line_mod` returns 2 (
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

## Alternatives

`draw_line`,
`draw_ellipse`,
`draw_region`

## See also

`gen_circle`,
`draw_rectangle1`,
`draw_rectangle2`

## Module

Foundation
