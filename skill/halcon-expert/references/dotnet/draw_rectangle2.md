# DrawRectangle2 (Operator)

## Name

`DrawRectangle2` — Interactive drawing of any orientated rectangle.

## Signature

`static void HOperatorSet.DrawRectangle2(HTuple windowHandle, out HTuple row, out HTuple column, out HTuple phi, out HTuple length1, out HTuple length2)`

`void HWindow.DrawRectangle2(out double row, out double column, out double phi, out double length1, out double length2)`

## Description

`DrawRectangle2` returns the parameter for any orientated rectangle,
which has been created interactively by the user in the window.

The created rectangle is described by its center, its two half axes and the angle
between the first half axis and the horizontal coordinate axis.

To create a rectangle you have to press the left mouse button for the center of the
rectangle. While keeping the button pressed you may dimension the length (*`length1`*)
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

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`row`** (output_control)  rectangle2.center.y `→` [HTuple](HTuple.md) (*double*)

Row index of the center.

**`column`** (output_control)  rectangle2.center.x `→` [HTuple](HTuple.md) (*double*)

Column index of the center.

**`phi`** (output_control)  rectangle2.angle.rad `→` [HTuple](HTuple.md) (*double*)

Orientation of the bigger half axis in radians.

**`length1`** (output_control)  rectangle2.hwidth `→` [HTuple](HTuple.md) (*double*)

Bigger half axis.

**`length2`** (output_control)  rectangle2.hheight `→` [HTuple](HTuple.md) (*double*)

Smaller half axis.

## Result

`DrawRectangle2` returns 2 (
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

`DrawRectangle2Mod`,
`DrawRectangle1`,
`DrawRegion`

## See also

`GenRectangle2`,
`DrawCircle`,
`DrawEllipse`

## Module

Foundation
