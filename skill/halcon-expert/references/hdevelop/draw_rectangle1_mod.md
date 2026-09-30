# draw_rectangle1_mod (Operator)

## Name

`draw_rectangle1_mod` — Draw a rectangle parallel to the coordinate axis.

## Signature

`draw_rectangle1_mod( : : WindowHandle, Row1In, Column1In, Row2In, Column2In : Row1, Column1, Row2, Column2)`

## Description

`draw_rectangle1_mod` returns the parameter for a rectangle parallel
to the coordinate axes, which has been created interactively by the user
in the window.

To create a rectangle are expected the parameters *`Row1In`*,
*`Column1In`*,*`Row2In`* and *`Column2In`*.
After a mouse click in the middle of the created rectangle you can move it.
A click close to one side “grips” it to modify the rectangle's dimension in perpendicular
direction to this side. If you click on one corner of the created rectangle, you may
move this corner.
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

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Row1In`** (input_control)  rectangle.origin.y `→`  (real)

Row index of the left upper corner.

**`Column1In`** (input_control)  rectangle.origin.x `→`  (real)

Column index of the left upper corner.

**`Row2In`** (input_control)  rectangle.corner.y `→`  (real)

Row index of the right lower corner.

**`Column2In`** (input_control)  rectangle.corner.x `→`  (real)

Column index of the right lower corner.

**`Row1`** (output_control)  rectangle.origin.y `→`  (real)

Row index of the left upper corner.

**`Column1`** (output_control)  rectangle.origin.x `→`  (real)

Column index of the left upper corner.

**`Row2`** (output_control)  rectangle.corner.y `→`  (real)

Row index of the right lower corner.

**`Column2`** (output_control)  rectangle.corner.x `→`  (real)

Column index of the right lower corner.

## Example (HDevelop)

```
read_image(Image,'monkey')
get_image_size (Image, Width, Height)
dev_display (Image)
draw_rectangle1_mod(WindowHandle,100,100,200,300,\
                    Row1,Column1,Row2,Column2)
dev_set_part (Row1, Column1, Row2, Column2)
dev_display (Image)
```

## Result

`draw_rectangle1_mod` returns 2 (
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

`draw_rectangle1`,
`draw_rectangle2`,
`draw_region`

## See also

`gen_rectangle1`,
`draw_circle`,
`draw_ellipse`

## Module

Foundation
