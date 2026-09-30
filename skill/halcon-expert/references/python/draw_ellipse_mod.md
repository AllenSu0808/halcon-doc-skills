# draw_ellipse_mod (Operator)

## Name

`draw_ellipse_mod` — Interactive drawing of an ellipse.

## Signature

`def draw_ellipse_mod(window_handle: HHandle, row_in: float, column_in: float, phi_in: float, radius_1in: float, radius_2in: float) -> Tuple[float, float, float, float, float]`

## Description

`draw_ellipse_mod` returns the parameter for any orientated ellipse, which
has been created interactively by the user in the window.

The created ellipse is described by its center, its two half axes and the angle
between the first half axis and the horizontal coordinate axis.

To create an ellipse are expected the parameters *`row_in`*,
*`column_in`*,*`phi_in`*,*`radius_1in`*,*`radius_2in`*.
Keeping the button pressed determines the length (*`radius_1`*)
and the orientation (*`phi`*) of the first half axis.
In doing so a temporary default length for the second half axis is assumed, which may be
modified afterwards on demand.
After another mouse click in the center of the created ellipse you can move it.
A mouse click close to a vertex “grips” it to modify the length of the appropriate
half axis. You may modify the orientation only, if a vertex of the first half axis is
gripped.

Pressing the right mouse button terminates the procedure.
After terminating the procedure the ellipse is not visible in the window any longer.

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

**`row_in`** (input_control)  ellipse.center.y `→` float

Row index of the center.

**`column_in`** (input_control)  ellipse.center.x `→` float

Column index of the center.

**`phi_in`** (input_control)  ellipse.angle.rad `→` float

Orientation of the bigger half axis in radians.

**`radius_1in`** (input_control)  ellipse.radius1 `→` float

Bigger half axis.

**`radius_2in`** (input_control)  ellipse.radius2 `→` float

Smaller half axis.

**`row`** (output_control)  ellipse.center.y `→` float

Row index of the center.

**`column`** (output_control)  ellipse.center.x `→` float

Column index of the center.

**`phi`** (output_control)  ellipse.angle.rad `→` float

Orientation of the first half axis in radians.

**`radius_1`** (output_control)  ellipse.radius1 `→` float

First half axis.

**`radius_2`** (output_control)  ellipse.radius2 `→` float

Second half axis.

## Result

`draw_ellipse_mod` returns 2 (
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

`draw_ellipse`,
`draw_circle`,
`draw_region`

## See also

`gen_ellipse`,
`draw_rectangle1`,
`draw_rectangle2`,
`draw_polygon`

## Module

Foundation
