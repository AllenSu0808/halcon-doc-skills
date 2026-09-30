# draw_point_mod (Operator)

## Name

`draw_point_mod` — Draw a point.

## Signature

`draw_point_mod( : : WindowHandle, RowIn, ColumnIn : Row, Column)`

## Description

`draw_point_mod` returns the parameter for a point, which has been
created interactively by the user in the window.

To create a point are expected the coordinates *`RowIn`* and
*`ColumnIn`*.
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

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`RowIn`** (input_control)  point.y `→`  (real)

Row index of the point.

**`ColumnIn`** (input_control)  point.x `→`  (real)

Column index of the point.

**`Row`** (output_control)  point.y `→`  (real)

Row index of the point.

**`Column`** (output_control)  point.x `→`  (real)

Column index of the point.

## Example (HDevelop)

```
draw_point_mod (WindowHandle, 100, 100, Row,Column)
gen_cross_contour_xld (Cross, Row, Column, 6, 0)
```

## Result

`draw_point_mod` returns 2 (
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

`draw_point`,
`draw_circle`,
`draw_ellipse`

## Module

Foundation
