# DrawPointMod (Operator)

## Name

`DrawPointMod` — Draw a point.

## Signature

`static void HOperatorSet.DrawPointMod(HTuple windowHandle, HTuple rowIn, HTuple columnIn, out HTuple row, out HTuple column)`

`void HWindow.DrawPointMod(double rowIn, double columnIn, out double row, out double column)`

## Description

`DrawPointMod` returns the parameter for a point, which has been
created interactively by the user in the window.

To create a point are expected the coordinates *`rowIn`* and
*`columnIn`*.
While keeping the button pressed you may “drag” the point in any direction.
Pressing the right mouse button terminates the procedure.

After terminating the procedure the point is not visible in the window any longer.

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

**`rowIn`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double*)

Row index of the point.

**`columnIn`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double*)

Column index of the point.

**`row`** (output_control)  point.y `→` [HTuple](HTuple.md) (*double*)

Row index of the point.

**`column`** (output_control)  point.x `→` [HTuple](HTuple.md) (*double*)

Column index of the point.

## Example (HDevelop)

```
draw_point_mod (WindowHandle, 100, 100, Row,Column)
gen_cross_contour_xld (Cross, Row, Column, 6, 0)
```

## Result

`DrawPointMod` returns 2 (
H_MSG_TRUE)
if the window is valid.
If necessary, an exception is raised.

## Possible Predecessors

`OpenWindow`

## Possible Successors

`ReduceDomain`,
`DispLine`,
`SetColored`,
`SetLineWidth`,
`SetDraw`

## See also

`DrawPoint`,
`DrawCircle`,
`DrawEllipse`

## Module

Foundation
