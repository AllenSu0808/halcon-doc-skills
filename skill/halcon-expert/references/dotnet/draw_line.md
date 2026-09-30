# DrawLine (Operator)

## Name

`DrawLine` — Draw a line.

## Signature

`static void HOperatorSet.DrawLine(HTuple windowHandle, out HTuple row1, out HTuple column1, out HTuple row2, out HTuple column2)`

`void HWindow.DrawLine(out double row1, out double column1, out double row2, out double column2)`

## Description

`DrawLine` returns the parameter for a line, which has been
created interactively by the user in the window.

To create a line you have to press the left mouse button determining a start point
of the line. While keeping the button pressed you may “drag” the line in
any direction. After another mouse click in the middle of the created line
you can move it.
If you click on one end point of the created line, you may move this point.
Pressing the right mouse button terminates the procedure.

After terminating the procedure the line is not visible in the window any longer.

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

**`row1`** (output_control)  line.begin.y `→` [HTuple](HTuple.md) (*double*)

Row index of the first point of the line.

**`column1`** (output_control)  line.begin.x `→` [HTuple](HTuple.md) (*double*)

Column index of the first point of the line.

**`row2`** (output_control)  line.end.y `→` [HTuple](HTuple.md) (*double*)

Row index of the second point of the line.

**`column2`** (output_control)  line.end.x `→` [HTuple](HTuple.md) (*double*)

Column index of the second point of the line.

## Example (HDevelop)

```
draw_line(WindowHandle,Row1,Column1,Row2,Column2)
gen_contour_polygon_xld (Line, [Row1,Row2], [Column1,Column2])
dev_display (Line)
```

## Result

`DrawLine` returns 2 (
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

`DrawLineMod`,
`GenRectangle1`,
`DrawCircle`,
`DrawEllipse`

## Module

Foundation
