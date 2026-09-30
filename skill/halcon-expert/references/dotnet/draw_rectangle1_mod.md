# DrawRectangle1Mod (Operator)

## Name

`DrawRectangle1Mod` — Draw a rectangle parallel to the coordinate axis.

## Signature

`static void HOperatorSet.DrawRectangle1Mod(HTuple windowHandle, HTuple row1In, HTuple column1In, HTuple row2In, HTuple column2In, out HTuple row1, out HTuple column1, out HTuple row2, out HTuple column2)`

`void HWindow.DrawRectangle1Mod(double row1In, double column1In, double row2In, double column2In, out double row1, out double column1, out double row2, out double column2)`

## Description

`DrawRectangle1Mod` returns the parameter for a rectangle parallel
to the coordinate axes, which has been created interactively by the user
in the window.

To create a rectangle are expected the parameters *`row1In`*,
*`column1In`*,*`row2In`* and *`column2In`*.
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

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`row1In`** (input_control)  rectangle.origin.y `→` [HTuple](HTuple.md) (*double*)

Row index of the left upper corner.

**`column1In`** (input_control)  rectangle.origin.x `→` [HTuple](HTuple.md) (*double*)

Column index of the left upper corner.

**`row2In`** (input_control)  rectangle.corner.y `→` [HTuple](HTuple.md) (*double*)

Row index of the right lower corner.

**`column2In`** (input_control)  rectangle.corner.x `→` [HTuple](HTuple.md) (*double*)

Column index of the right lower corner.

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
draw_rectangle1_mod(WindowHandle,100,100,200,300,\
                    Row1,Column1,Row2,Column2)
dev_set_part (Row1, Column1, Row2, Column2)
dev_display (Image)
```

## Result

`DrawRectangle1Mod` returns 2 (
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

`DrawRectangle1`,
`DrawRectangle2`,
`DrawRegion`

## See also

`GenRectangle1`,
`DrawCircle`,
`DrawEllipse`

## Module

Foundation
