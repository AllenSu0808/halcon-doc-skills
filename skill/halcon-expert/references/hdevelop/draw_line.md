# draw_line (Operator)

## Name

`draw_line` — Draw a line.

## Signature

`draw_line( : : WindowHandle : Row1, Column1, Row2, Column2)`

## Description

`draw_line` returns the parameter for a line, which has been
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

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Row1`** (output_control)  line.begin.y `→`  (real)

Row index of the first point of the line.

**`Column1`** (output_control)  line.begin.x `→`  (real)

Column index of the first point of the line.

**`Row2`** (output_control)  line.end.y `→`  (real)

Row index of the second point of the line.

**`Column2`** (output_control)  line.end.x `→`  (real)

Column index of the second point of the line.

## Example (HDevelop)

```
draw_line(WindowHandle,Row1,Column1,Row2,Column2)
gen_contour_polygon_xld (Line, [Row1,Row2], [Column1,Column2])
dev_display (Line)
```

## Result

`draw_line` returns 2 (
H_MSG_TRUE)
if the window is valid.
If necessary, an exception is raised.

## Possible Predecessors

`open_window`

## Possible Successors

`reduce_domain`,
`disp_line`,
`set_colored`,
`set_line_width`,
`set_draw`

## See also

`draw_line_mod`,
`gen_rectangle1`,
`draw_circle`,
`draw_ellipse`

## Module

Foundation
