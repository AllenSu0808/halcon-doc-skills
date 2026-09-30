# draw_circle_mod (Operator)

## Name

`draw_circle_mod` — Interactive drawing of a circle.

## Signature

`def draw_circle_mod(window_handle: HHandle, row_in: float, column_in: float, radius_in: float) -> Tuple[float, float, float]`

## Description

`draw_circle_mod` produces the parameter for a circle created interactive by
the user in the window.

To create a circle are expected the coordinates *`row_in`* and
*`column_in`* of the center of a circle with radius *`radius_in`*.
After another mouse click in the created circle center you can move it.
A clicking close to the circular arc you can modify the *`radius`* of
the circle.
Pressing the right mouse button terminates the procedure.
After terminating the procedure the circle is not visible in the window any longer.

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

**`row_in`** (input_control)  circle.center.y `→` float

Row index of the center.

**`column_in`** (input_control)  circle.center.x `→` float

Column index of the center.

**`radius_in`** (input_control)  circle.radius `→` float

Radius of the circle.

**`row`** (output_control)  circle.center.y `→` float

Row index of the center.

**`column`** (output_control)  circle.center.x `→` float

Column index of the center.

**`radius`** (output_control)  circle.radius `→` float

Circle's radius.

## Result

`draw_circle_mod` returns 2 (
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

`draw_circle`,
`draw_ellipse`,
`draw_region`

## See also

`gen_circle`,
`draw_rectangle1`,
`draw_rectangle2`,
`draw_polygon`

## Module

Foundation
