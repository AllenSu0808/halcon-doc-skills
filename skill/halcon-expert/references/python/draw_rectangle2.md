# draw_rectangle2 (Operator)

## Name

`draw_rectangle2` — Interactive drawing of any orientated rectangle.

## Signature

`def draw_rectangle2(window_handle: HHandle) -> Tuple[float, float, float, float, float]`

## Description

`draw_rectangle2` returns the parameter for any orientated rectangle,
which has been created interactively by the user in the window.

The created rectangle is described by its center, its two half axes and the angle
between the first half axis and the horizontal coordinate axis.

To create a rectangle you have to press the left mouse button for the center of the
rectangle. While keeping the button pressed you may dimension the length (*`length_1`*)
and the orientation (*`phi`*) of the first half axis.
In doing so a temporary default length for the second half axis is assumed, which may be
modified afterwards on demand.
After another mouse click in the middle of the created rectangle, you can move it.
A click close to one side “grips” it to modify the rectangle's dimension in perpendicular
direction to this side. You only can modify the orientation, if you grip a side perpendicular
to the first half axis.
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

`draw_rectangle2` returns 2 (
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

`draw_rectangle2_mod`,
`draw_rectangle1`,
`draw_region`

## See also

`gen_rectangle2`,
`draw_circle`,
`draw_ellipse`

## Module

Foundation
