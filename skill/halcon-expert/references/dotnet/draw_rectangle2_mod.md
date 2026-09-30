# DrawRectangle2Mod (Operator)

## Name

`DrawRectangle2Mod` — Interactive drawing of any orientated rectangle.

## Signature

`static void HOperatorSet.DrawRectangle2Mod(HTuple windowHandle, HTuple rowIn, HTuple columnIn, HTuple phiIn, HTuple length1In, HTuple length2In, out HTuple row, out HTuple column, out HTuple phi, out HTuple length1, out HTuple length2)`

`void HWindow.DrawRectangle2Mod(double rowIn, double columnIn, double phiIn, double length1In, double length2In, out double row, out double column, out double phi, out double length1, out double length2)`

## Description

`DrawRectangle2Mod` returns the parameter for any orientated
rectangle, which has been created interactively by the user in the window.

The created rectangle is described by its center, its two half axes and the
angle between the first half axis and the horizontal coordinate axis.

To create a rectangle are expected the parameters *`rowIn`*,
*`columnIn`*,*`phiIn`*,*`length1In`*,*`length2In`*.
A click close to one side “grips” it to modify the rectangle's dimension
in perpendicular direction (*`length2`*) to this side. You only can
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

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`rowIn`** (input_control)  rectangle2.center.y `→` [HTuple](HTuple.md) (*double*)

Row index of the center.

**`columnIn`** (input_control)  rectangle2.center.x `→` [HTuple](HTuple.md) (*double*)

Column index of the center.

**`phiIn`** (input_control)  rectangle2.angle.rad `→` [HTuple](HTuple.md) (*double*)

Orientation of the bigger half axis in radians.

**`length1In`** (input_control)  rectangle2.hwidth `→` [HTuple](HTuple.md) (*double*)

Bigger half axis.

**`length2In`** (input_control)  rectangle2.hheight `→` [HTuple](HTuple.md) (*double*)

Smaller half axis.

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

`DrawRectangle2Mod` returns 2 (
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

`DrawRectangle2`,
`DrawRectangle1`,
`DrawRectangle2`,
`DrawRegion`

## See also

`GenRectangle2`,
`DrawCircle`,
`DrawEllipse`

## Module

Foundation
