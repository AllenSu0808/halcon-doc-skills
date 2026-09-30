# draw_region (Operator)

## Name

`draw_region` — Interactive drawing of a closed region.

## Signature

`draw_region( : Region : WindowHandle : )`

## Description

`draw_region` produces an image. The region of that image spans
exactly the image region entered interactively by mouse clicks (gray values
remain undefined).
Painting happens in the output window while keeping the left mouse button
pressed. The left mouse button even operates by clicking in the output window;
through this a line between the previous clicked points is drawn.
Clicking the right mouse button terminates input and closes the outline.
Subsequently the image is “filled up”. Also it contains the whole image area
enclosed by the mouse.

Painting uses that color which has been set by [`set_color`](set_color.md),
[`set_rgb`](set_rgb.md), etc. .

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

**`Region`** (output_object)  region `→` object

Interactive created region.

**`WindowHandle`** (input_control)  window `→`  (handle)

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

If the window is valid, `draw_region` returns 2 (
H_MSG_TRUE)
.
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
`draw_rectangle1`,
`draw_rectangle2`

## See also

`draw_polygon`,
`reduce_domain`,
`fill_up`,
`set_color`

## Module

Foundation
