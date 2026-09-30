# DrawCircle (Operator)

## Name

`DrawCircle` — Interactive drawing of a circle.

## Signature

`static void HOperatorSet.DrawCircle(HTuple windowHandle, out HTuple row, out HTuple column, out HTuple radius)`

`void HWindow.DrawCircle(out double row, out double column, out double radius)`

## Description

`DrawCircle` produces the parameter for a circle created interactive by
the user in the window.

To create a circle you have to press the mouse button at the location which is used
as the center of that circle. While keeping the mouse button pressed, the
*`radius`*'s length can be modified through moving the mouse.
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

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`row`** (output_control)  circle.center.y `→` [HTuple](HTuple.md) (*double*)

Barycenter's row index.

**`column`** (output_control)  circle.center.x `→` [HTuple](HTuple.md) (*double*)

Barycenter's column index.

**`radius`** (output_control)  circle.radius `→` [HTuple](HTuple.md) (*double*)

Circle's radius.

## Example (HDevelop)

```
read_image(Image,'monkey')
draw_circle(WindowHandle,Row,Column,Radius)
gen_circle(Circle,Row,Column,Radius)
reduce_domain(Image,Circle,ImageReduced)
invert_image (ImageReduced, ImageInvert)
dev_display (ImageInvert)
```

## Result

`DrawCircle` returns 2 (
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

`DrawCircleMod`,
`DrawEllipse`,
`DrawRegion`

## See also

`GenCircle`,
`DrawRectangle1`,
`DrawRectangle2`,
`DrawPolygon`

## Module

Foundation
