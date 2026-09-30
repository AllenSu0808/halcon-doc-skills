# draw_polygon (Operator)

## Name

`draw_polygon` — Interactive drawing of a polygon row.

## Signature

`draw_polygon( : PolygonRegion : WindowHandle : )`

## Description

`draw_polygon` produces an image. The region of that image spans
exactly the image points entered interactively by mouse clicks (gray values
remain undefined).

Painting in the output window happens while pressing the left mouse button.
Releasing the left mouse button and repressing it at another position
effects drawing a line between these two points.
Pressing the right mouse button terminates the input.
Painting uses that color which has been set by [`set_color`](set_color.md),
[`set_rgb`](set_rgb.md), etc. .

To put gray values on the created *`PolygonRegion`* for further processing,
you may use the operator [`reduce_domain`](reduce_domain.md).

## Attention

The painted contour is not closed automatically, in particular it is not
“filled up” either.

Output object's gray values are not defined.

If used in a buffer window, mouse events have to be supplied by the
application, while the draw operator must be run in another thread.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`PolygonRegion`** (output_object)  region `→` object

Region, which encompasses all painted points.

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

## Example (HDevelop)

```
draw_polygon(Polygon,WindowHandle)
shape_trans(Polygon,Filled,'convex')
dev_display (Filled)
```

## Result

If the window is valid, `draw_polygon` returns 2 (
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

`draw_region`,
`draw_circle`,
`draw_rectangle1`,
`draw_rectangle2`,
`boundary`

## See also

`reduce_domain`,
`fill_up`,
`set_color`

## Module

Foundation
