# DispRegion (Operator)

## Name

`DispRegion` — Displays regions in a window.

## Signature

`static void HOperatorSet.DispRegion(HObject dispRegions, HTuple windowHandle)`

`void HRegion.DispRegion(HWindow windowHandle)`

`void HWindow.DispRegion(HRegion dispRegions)`

## Description

`DispRegion` displays the regions in *`dispRegions`*
in the output window. The parameters for output can be set
with the operators [`SetColor`](set_color.md), [`SetGray`](set_gray.md),
[`SetDraw`](set_draw.md), [`SetLineWidth`](set_line_width.md), etc.

The color(s) for the display of the regions are determined with
[`SetColor`](set_color.md), [`SetRgb`](set_rgb.md), [`SetGray`](set_gray.md) or
[`SetColored`](set_colored.md). If more than one region is displayed and more than
one color is set, the colors are assigned in a cyclic way to the
regions.

The form of the region for output can be modified by [`SetPaint`](set_paint.md)
(e.g., encompassing circle, convex hull). The command [`SetDraw`](set_draw.md)
determines if the region is filled or only the boundary is drawn. If only
the boundary is drawn, the thickness of the boundary will be determined by
[`SetLineWidth`](set_line_width.md) and the style by [`SetLineStyle`](set_line_style.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dispRegions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to display.

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

## Example (HDevelop)

```
* Output with 12 colors:
set_colored(WindowHandle,12)
disp_region(SomeSegments,WindowHandle)

* Symbolic representation:
set_draw(WindowHandle,'margin')
set_color(WindowHandle,'red')
set_shape(WindowHandle,'ellipse')
disp_region(SomeSegments,WindowHandle)

* Representation of a margin with pattern:
set_draw(WindowHandle,'margin')
set_color(WindowHandle,'blue')
set_line_style(WindowHandle,[12,3])
disp_region(Segments,WindowHandle)
```

## Result

`DispRegion` returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`OpenWindow`,
`SetRgb`,
`SetLut`,
`SetHsi`,
`SetShape`,
`SetLineStyle`,
`SetDraw`,
`SetColor`,
`SetColored`,
`SetLineWidth`

## Alternatives

`DispObj`,
`DispArrow`,
`DispLine`,
`DispCircle`,
`DispRectangle1`,
`DispRectangle2`,
`DispEllipse`

## See also

`OpenWindow`,
`SetColor`,
`SetColored`,
`SetDraw`,
`SetShape`,
`SetPaint`,
`SetGray`,
`SetRgb`,
`SetHsi`,
`SetLineWidth`,
`SetLineStyle`,
`PaintRegion`,
`DumpWindow`

## Module

Foundation
