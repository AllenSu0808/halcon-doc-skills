# draw_rectangle2_mod (Operator)

## Name

`draw_rectangle2_mod` — Interactive drawing of any orientated rectangle.

## Signature

`draw_rectangle2_mod( : : WindowHandle, RowIn, ColumnIn, PhiIn, Length1In, Length2In : Row, Column, Phi, Length1, Length2)`

## Description

`draw_rectangle2_mod` returns the parameter for any orientated
rectangle, which has been created interactively by the user in the window.

The created rectangle is described by its center, its two half axes and the
angle between the first half axis and the horizontal coordinate axis.

To create a rectangle are expected the parameters *`RowIn`*,
*`ColumnIn`*,*`PhiIn`*,*`Length1In`*,*`Length2In`*.
A click close to one side “grips” it to modify the rectangle's dimension
in perpendicular direction (*`Length2`*) to this side. You only can
modify the orientation (*`Phi`*), if you grip a side perpendicular to
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

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`RowIn`** (input_control)  rectangle2.center.y `→`  (real)

Row index of the center.

**`ColumnIn`** (input_control)  rectangle2.center.x `→`  (real)

Column index of the center.

**`PhiIn`** (input_control)  rectangle2.angle.rad `→`  (real)

Orientation of the bigger half axis in radians.

**`Length1In`** (input_control)  rectangle2.hwidth `→`  (real)

Bigger half axis.

**`Length2In`** (input_control)  rectangle2.hheight `→`  (real)

Smaller half axis.

**`Row`** (output_control)  rectangle2.center.y `→`  (real)

Row index of the center.

**`Column`** (output_control)  rectangle2.center.x `→`  (real)

Column index of the center.

**`Phi`** (output_control)  rectangle2.angle.rad `→`  (real)

Orientation of the bigger half axis in radians.

**`Length1`** (output_control)  rectangle2.hwidth `→`  (real)

Bigger half axis.

**`Length2`** (output_control)  rectangle2.hheight `→`  (real)

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
