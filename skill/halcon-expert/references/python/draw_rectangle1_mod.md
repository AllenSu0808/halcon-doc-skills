# draw_rectangle1_mod (Operator)

## Name

`draw_rectangle1_mod` — Draw a rectangle parallel to the coordinate axis.

## Signature

`def draw_rectangle1_mod(window_handle: HHandle, row_1in: float, column_1in: float, row_2in: float, column_2in: float) -> Tuple[float, float, float, float]`

## Description

`draw_rectangle1_mod` returns the parameter for a rectangle parallel
to the coordinate axes, which has been created interactively by the user
in the window.

To create a rectangle are expected the parameters *`row_1in`*,
*`column_1in`*,*`row_2in`* and *`column_2in`*.
After a mouse click in the middle of the created rectangle you can move it.
A click close to one side “grips” it to modify the rectangle's dimension in perpendicular
direction to this side. If you click on one corner of the created rectangle, you may
move this corner.
Pressing the right mouse button terminates the procedure.

After terminating the procedure the rectangle is not visible in the window any longer.

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

**`row_1in`** (input_control)  rectangle.origin.y `→` float

Row index of the left upper corner.

**`column_1in`** (input_control)  rectangle.origin.x `→` float

Column index of the left upper corner.

**`row_2in`** (input_control)  rectangle.corner.y `→` float

Row index of the right lower corner.

**`column_2in`** (input_control)  rectangle.corner.x `→` float

Column index of the right lower corner.

**`row_1`** (output_control)  rectangle.origin.y `→` float

Row index of the left upper corner.

**`column_1`** (output_control)  rectangle.origin.x `→` float

Column index of the left upper corner.

**`row_2`** (output_control)  rectangle.corner.y `→` float

Row index of the right lower corner.

**`column_2`** (output_control)  rectangle.corner.x `→` float

Column index of the right lower corner.

## Result

`draw_rectangle1_mod` returns 2 (
H_MSG_TRUE)
if the window is valid.
If necessary, an exception is raised.

## Possible Predecessors

`open_window`

## Possible Successors

`reduce_domain`,
`disp_region`,
`set_colored`,
`set_line_width`,
`set_draw`

## Alternatives

`draw_rectangle1`,
`draw_rectangle2`,
`draw_region`

## See also

`gen_rectangle1`,
`draw_circle`,
`draw_ellipse`

## Module

Foundation
