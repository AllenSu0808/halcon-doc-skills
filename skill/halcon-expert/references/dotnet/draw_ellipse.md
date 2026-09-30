# DrawEllipse (Operator)

## Name

`DrawEllipse` — Interactive drawing of an ellipse.

## Signature

`static void HOperatorSet.DrawEllipse(HTuple windowHandle, out HTuple row, out HTuple column, out HTuple phi, out HTuple radius1, out HTuple radius2)`

`void HWindow.DrawEllipse(out double row, out double column, out double phi, out double radius1, out double radius2)`

## Description

`DrawEllipse` returns the parameter for any orientated ellipse, which
has been created interactively by the user in the window.

The created ellipse is described by its center, *`row`* and
*`column`*, its orientation, *`phi`*, and its two half axes,
*`radius1`* and *`radius2`*.

To create an ellipse you have to determine the center of the ellipse with the
left mouse button. Keeping the button pressed determines the length (*`radius1`*)
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

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`row`** (output_control)  ellipse.center.y `→` [HTuple](HTuple.md) (*double*)

Row index of the center.

**`column`** (output_control)  ellipse.center.x `→` [HTuple](HTuple.md) (*double*)

Column index of the center.

**`phi`** (output_control)  ellipse.angle.rad `→` [HTuple](HTuple.md) (*double*)

Orientation of the first half axis in radians.

**`radius1`** (output_control)  ellipse.radius1 `→` [HTuple](HTuple.md) (*double*)

First half axis.

**`radius2`** (output_control)  ellipse.radius2 `→` [HTuple](HTuple.md) (*double*)

Second half axis.

## Example (HDevelop)

```
read_image(Image,'monkey')
draw_ellipse(WindowHandle,Row,Column,Phi,Radius1,Radius2)
gen_ellipse(Ellipse,Row,Column,Phi,Radius1,Radius2)
reduce_domain(Image,Ellipse,GrayEllipse)
sobel_amp(GrayEllipse,Sobel,'sum_abs',3)
dev_display(Sobel)
```

## Result

`DrawEllipse` returns 2 (
H_MSG_TRUE)
if the window is valid.
If necessary, an exception is raised.

## Possible Predecessors

`OpenWindow`

## Possible Successors

`ReduceDomain`,
`DispRegion`,
`SetColored`,
`SetLineWidth`,
`SetDraw`

## Alternatives

`DrawEllipseMod`,
`DrawCircle`,
`DrawRegion`

## See also

`GenEllipse`,
`DrawRectangle1`,
`DrawRectangle2`,
`DrawPolygon`

## Module

Foundation
