# DrawLineMod (Operator)

## Name

`DrawLineMod` — Draw a line.

## Signature

`static void HOperatorSet.DrawLineMod(HTuple windowHandle, HTuple row1In, HTuple column1In, HTuple row2In, HTuple column2In, out HTuple row1, out HTuple column1, out HTuple row2, out HTuple column2)`

`void HWindow.DrawLineMod(double row1In, double column1In, double row2In, double column2In, out double row1, out double column1, out double row2, out double column2)`

## Description

`DrawLineMod` returns the parameter for a line, which has been
created interactively by the user in the window.

To create a line are expected the coordinates of the start point
*`row1In`*, *`column1In`* and of the end point
*`row2In`*,*`column2In`*.
If you click on one end point of the created line, you may move this point.
After another mouse click in the middle of the created line
you can move it.

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

**`row1In`** (input_control)  line.begin.y `→` [HTuple](HTuple.md) (*double*)

Row index of the first point of the line.

**`column1In`** (input_control)  line.begin.x `→` [HTuple](HTuple.md) (*double*)

Column index of the first point of the line.

**`row2In`** (input_control)  line.end.y `→` [HTuple](HTuple.md) (*double*)

Row index of the second point of the line.

**`column2In`** (input_control)  line.end.x `→` [HTuple](HTuple.md) (*double*)

Column index of the second point of the line.

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
draw_line_mod(WindowHandle,10,20,55,124,Row1,Column1,Row2,Column2)
gen_contour_polygon_xld (Line, [Row1,Row2], [Column1,Column2])
dev_display (Line)
```

## Result

`DrawLineMod` returns 2 (
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

## Alternatives

`DrawLine`,
`DrawEllipse`,
`DrawRegion`

## See also

`GenCircle`,
`DrawRectangle1`,
`DrawRectangle2`

## Module

Foundation
