# draw_circle_mod (Operator)

## Name

`draw_circle_mod` — Interactive drawing of a circle.

## Signature

`draw_circle_mod( : : WindowHandle, RowIn, ColumnIn, RadiusIn : Row, Column, Radius)`

## Description

`draw_circle_mod` produces the parameter for a circle created interactive by
the user in the window.

To create a circle are expected the coordinates *`RowIn`* and
*`ColumnIn`* of the center of a circle with radius *`RadiusIn`*.
After another mouse click in the created circle center you can move it.
A clicking close to the circular arc you can modify the *`Radius`* of
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

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`RowIn`** (input_control)  circle.center.y `→`  (real)

Row index of the center.

**`ColumnIn`** (input_control)  circle.center.x `→`  (real)

Column index of the center.

**`RadiusIn`** (input_control)  circle.radius `→`  (real)

Radius of the circle.

**`Row`** (output_control)  circle.center.y `→`  (real)

Row index of the center.

**`Column`** (output_control)  circle.center.x `→`  (real)

Column index of the center.

**`Radius`** (output_control)  circle.radius `→`  (real)

Circle's radius.

## Example (HDevelop)

```
read_image(Image,'monkey')
draw_circle_mod(WindowHandle,20,20,15,Row,Column,Radius)
gen_circle(Circle,Row,Column,Radius)
reduce_domain(Image,Circle,ImageReduced)
invert_image (ImageReduced, ImageInvert)
dev_display (ImageInvert)
```

## Result

`draw_circle_mod` returns 2 (
H_MSG_TRUE)
if the window is valid.
If necessary, an exception is raised.

## Possible Predecessors

`open_window`

## Possible Successors

`reduce_domain`,
`disp_region`,
`set_colored`,
`set_line_width`,
`set_draw`

## Alternatives

`draw_circle`,
`draw_ellipse`,
`draw_region`

## See also

`gen_circle`,
`draw_rectangle1`,
`draw_rectangle2`,
`draw_polygon`

## Module

Foundation
