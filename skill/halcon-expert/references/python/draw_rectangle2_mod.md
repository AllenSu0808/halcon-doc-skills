# draw_rectangle2_mod (Operator)

## Name

`draw_rectangle2_mod` — Interactive drawing of any orientated rectangle.

## Signature

`def draw_rectangle2_mod(window_handle: HHandle, row_in: float, column_in: float, phi_in: float, length_1in: float, length_2in: float) -> Tuple[float, float, float, float, float]`

## Description

`draw_rectangle2_mod` returns the parameter for any orientated
rectangle, which has been created interactively by the user in the window.

The created rectangle is described by its center, its two half axes and the
angle between the first half axis and the horizontal coordinate axis.

To create a rectangle are expected the parameters *`row_in`*,
*`column_in`*,*`phi_in`*,*`length_1in`*,*`length_2in`*.
A click close to one side “grips” it to modify the rectangle's dimension
in perpendicular direction (*`length_2`*) to this side. You only can
modify the orientation (*`phi`*), if you grip a side perpendicular to
the first half axis. After another mouse click in the middle of the created
rectangle, you can move it. Pressing the right mouse button terminates the
procedure.

After terminating the procedure the rectangle is not visible in the window
any longer.

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

**`row_in`** (input_control)  rectangle2.center.y `→` float

Row index of the center.

**`column_in`** (input_control)  rectangle2.center.x `→` float

Column index of the center.

**`phi_in`** (input_control)  rectangle2.angle.rad `→` float

Orientation of the bigger half axis in radians.

**`length_1in`** (input_control)  rectangle2.hwidth `→` float

Bigger half axis.

**`length_2in`** (input_control)  rectangle2.hheight `→` float

Smaller half axis.

**`row`** (output_control)  rectangle2.center.y `→` float

Row index of the center.

**`column`** (output_control)  rectangle2.center.x `→` float

Column index of the center.

**`phi`** (output_control)  rectangle2.angle.rad `→` float

Orientation of the bigger half axis in radians.

**`length_1`** (output_control)  rectangle2.hwidth `→` float

Bigger half axis.

**`length_2`** (output_control)  rectangle2.hheight `→` float

Smaller half axis.

## Result

`draw_rectangle2_mod` returns 2 (
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

`draw_rectangle2`,
`draw_rectangle1`,
`draw_rectangle2`,
`draw_region`

## See also

`gen_rectangle2`,
`draw_circle`,
`draw_ellipse`

## Module

Foundation
