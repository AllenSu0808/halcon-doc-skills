# draw_line_mod (Operator)

## Name

`draw_line_mod` — Draw a line.

## Signature

`draw_line_mod( : : WindowHandle, Row1In, Column1In, Row2In, Column2In : Row1, Column1, Row2, Column2)`

## Description

`draw_line_mod` returns the parameter for a line, which has been
created interactively by the user in the window.

To create a line are expected the coordinates of the start point
*`Row1In`*, *`Column1In`* and of the end point
*`Row2In`*,*`Column2In`*.
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

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Row1In`** (input_control)  line.begin.y `→`  (real)

Row index of the first point of the line.

**`Column1In`** (input_control)  line.begin.x `→`  (real)

Column index of the first point of the line.

**`Row2In`** (input_control)  line.end.y `→`  (real)

Row index of the second point of the line.

**`Column2In`** (input_control)  line.end.x `→`  (real)

Column index of the second point of the line.

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
draw_line_mod(WindowHandle,10,20,55,124,Row1,Column1,Row2,Column2)
gen_contour_polygon_xld (Line, [Row1,Row2], [Column1,Column2])
dev_display (Line)
```

## Result

`draw_line_mod` returns 2 (
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

## Alternatives

`draw_line`,
`draw_ellipse`,
`draw_region`

## See also

`gen_circle`,
`draw_rectangle1`,
`draw_rectangle2`

## Module

Foundation
