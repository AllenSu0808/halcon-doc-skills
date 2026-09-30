# DrawPolygon (Operator)

## Name

`DrawPolygon` — Interactive drawing of a polygon row.

## Signature

`static void HOperatorSet.DrawPolygon(out HObject polygonRegion, HTuple windowHandle)`

`void HRegion.DrawPolygon(HWindow windowHandle)`

`HRegion HWindow.DrawPolygon()`

## Description

`DrawPolygon` produces an image. The region of that image spans
exactly the image points entered interactively by mouse clicks (gray values
remain undefined).

Painting in the output window happens while pressing the left mouse button.
Releasing the left mouse button and repressing it at another position
effects drawing a line between these two points.
Pressing the right mouse button terminates the input.
Painting uses that color which has been set by [`SetColor`](set_color.md),
[`SetRgb`](set_rgb.md), etc. .

To put gray values on the created *`polygonRegion`* for further processing,
you may use the operator [`ReduceDomain`](reduce_domain.md).

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

**`polygonRegion`** (output_object)  region `→` [HRegion](HRegion.md)

Region, which encompasses all painted points.

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

## Example (HDevelop)

```
draw_polygon(Polygon,WindowHandle)
shape_trans(Polygon,Filled,'convex')
dev_display (Filled)
```

## Result

If the window is valid, `DrawPolygon` returns 2 (
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

`DrawRegion`,
`DrawCircle`,
`DrawRectangle1`,
`DrawRectangle2`,
`Boundary`

## See also

`ReduceDomain`,
`FillUp`,
`SetColor`

## Module

Foundation
