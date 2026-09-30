# DrawRectangle1 (Operator)

## Name

`DrawRectangle1` — Draw a rectangle parallel to the coordinate axis.

## Signature

`static void HOperatorSet.DrawRectangle1(HTuple windowHandle, out HTuple row1, out HTuple column1, out HTuple row2, out HTuple column2)`

`void HWindow.DrawRectangle1(out double row1, out double column1, out double row2, out double column2)`

## Description

`DrawRectangle1` returns the parameter for a rectangle parallel
to the coordinate axes, which has been created interactively by the user
in the window.

To create a rectangle you have to press the left mouse button determining a corner
of the rectangle. While keeping the button pressed you may “drag” the rectangle in
any direction. After another mouse click in the middle of the created rectangle
you can move it.
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

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`row1`** (output_control)  rectangle.origin.y `→` [HTuple](HTuple.md) (*double*)

Row index of the left upper corner.

**`column1`** (output_control)  rectangle.origin.x `→` [HTuple](HTuple.md) (*double*)

Column index of the left upper corner.

**`row2`** (output_control)  rectangle.corner.y `→` [HTuple](HTuple.md) (*double*)

Row index of the right lower corner.

**`column2`** (output_control)  rectangle.corner.x `→` [HTuple](HTuple.md) (*double*)

Column index of the right lower corner.

## Example (HDevelop)

```
read_image(Image,'monkey')
get_image_size (Image, Width, Height)
dev_display (Image)
draw_rectangle1(WindowHandle,Row1,Column1,Row2,Column2)
dev_set_part (Row1, Column1, Row2, Column2)
dev_display (Image)
```

## Result

`DrawRectangle1` returns 2 (
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

`DrawRectangle1Mod`,
`DrawRectangle2`,
`DrawRegion`

## See also

`GenRectangle1`,
`DrawCircle`,
`DrawEllipse`

## Module

Foundation
