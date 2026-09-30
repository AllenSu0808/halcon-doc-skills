# draw_ellipse_mod (Operator)

## Name

`draw_ellipse_mod` — Interactive drawing of an ellipse.

## Signature

`draw_ellipse_mod( : : WindowHandle, RowIn, ColumnIn, PhiIn, Radius1In, Radius2In : Row, Column, Phi, Radius1, Radius2)`

## Description

`draw_ellipse_mod` returns the parameter for any orientated ellipse, which
has been created interactively by the user in the window.

The created ellipse is described by its center, its two half axes and the angle
between the first half axis and the horizontal coordinate axis.

To create an ellipse are expected the parameters *`RowIn`*,
*`ColumnIn`*,*`PhiIn`*,*`Radius1In`*,*`Radius2In`*.
Keeping the button pressed determines the length (*`Radius1`*)
and the orientation (*`Phi`*) of the first half axis.
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

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`RowIn`** (input_control)  ellipse.center.y `→`  (real)

Row index of the center.

**`ColumnIn`** (input_control)  ellipse.center.x `→`  (real)

Column index of the center.

**`PhiIn`** (input_control)  ellipse.angle.rad `→`  (real)

Orientation of the bigger half axis in radians.

**`Radius1In`** (input_control)  ellipse.radius1 `→`  (real)

Bigger half axis.

**`Radius2In`** (input_control)  ellipse.radius2 `→`  (real)

Smaller half axis.

**`Row`** (output_control)  ellipse.center.y `→`  (real)

Row index of the center.

**`Column`** (output_control)  ellipse.center.x `→`  (real)

Column index of the center.

**`Phi`** (output_control)  ellipse.angle.rad `→`  (real)

Orientation of the first half axis in radians.

**`Radius1`** (output_control)  ellipse.radius1 `→`  (real)

First half axis.

**`Radius2`** (output_control)  ellipse.radius2 `→`  (real)

Second half axis.

## Example (HDevelop)

```
read_image(Image,'monkey')
draw_ellipse_mod(WindowHandle,RowIn,ColumnIn,PhiIn,Radius1In,Radius2In,\
                 Row,Column,Phi,Radius1,Radius2)
gen_ellipse(Ellipse,Row,Column,Phi,Radius1,Radius2)
reduce_domain(Image,Ellipse,GrayEllipse)
sobel_amp(GrayEllipse,Sobel,'sum_abs',3)
dev_display(Sobel)
```

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
