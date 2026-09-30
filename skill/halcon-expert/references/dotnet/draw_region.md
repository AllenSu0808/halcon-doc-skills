# DrawRegion (Operator)

## Name

`DrawRegion` — Interactive drawing of a closed region.

## Signature

`static void HOperatorSet.DrawRegion(out HObject region, HTuple windowHandle)`

`void HRegion.DrawRegion(HWindow windowHandle)`

`HRegion HWindow.DrawRegion()`

## Description

`DrawRegion` produces an image. The region of that image spans
exactly the image region entered interactively by mouse clicks (gray values
remain undefined).
Painting happens in the output window while keeping the left mouse button
pressed. The left mouse button even operates by clicking in the output window;
through this a line between the previous clicked points is drawn.
Clicking the right mouse button terminates input and closes the outline.
Subsequently the image is “filled up”. Also it contains the whole image area
enclosed by the mouse.

Painting uses that color which has been set by [`SetColor`](set_color.md),
[`SetRgb`](set_rgb.md), etc. .

Pressing the right mouse button terminates the procedure.

## Attention

The output object's gray values are not defined.

If used in a buffer window, mouse events have to be supplied by the
application, while the draw operator must be run in another thread.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (output_object)  region `→` [HRegion](HRegion.md)

Interactive created region.

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

## Example (HDevelop)

```
read_image(Image,'fabrik')
dev_display (Image)
draw_region(Region,WindowHandle)
reduce_domain(Image,Region,ImageReduced)
invert_image (ImageReduced, ImageInvert)
dev_display (ImageInvert)
```

## Result

If the window is valid, `DrawRegion` returns 2 (
H_MSG_TRUE)
.
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

`DrawCircle`,
`DrawEllipse`,
`DrawRectangle1`,
`DrawRectangle2`

## See also

`DrawPolygon`,
`ReduceDomain`,
`FillUp`,
`SetColor`

## Module

Foundation
