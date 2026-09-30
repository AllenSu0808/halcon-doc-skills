# disp_region (Operator)

## Name

`disp_region` — Displays regions in a window.

## Signature

`disp_region(DispRegions : : WindowHandle : )`

## Description

`disp_region` displays the regions in *`DispRegions`*
in the output window. The parameters for output can be set
with the operators [`set_color`](set_color.md), [`set_gray`](set_gray.md),
[`set_draw`](set_draw.md), [`set_line_width`](set_line_width.md), etc.

The color(s) for the display of the regions are determined with
[`set_color`](set_color.md), [`set_rgb`](set_rgb.md), [`set_gray`](set_gray.md) or
[`set_colored`](set_colored.md). If more than one region is displayed and more than
one color is set, the colors are assigned in a cyclic way to the
regions.

The form of the region for output can be modified by [`set_paint`](set_paint.md)
(e.g., encompassing circle, convex hull). The command [`set_draw`](set_draw.md)
determines if the region is filled or only the boundary is drawn. If only
the boundary is drawn, the thickness of the boundary will be determined by
[`set_line_width`](set_line_width.md) and the style by [`set_line_style`](set_line_style.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DispRegions`** (input_object)  region(-array) `→` object

Regions to display.

**`WindowHandle`** (input_control)  window `→`  (handle)

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

`disp_region` returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`open_window`,
`set_rgb`,
`set_lut`,
`set_hsi`,
`set_shape`,
`set_line_style`,
`set_draw`,
`set_color`,
`set_colored`,
`set_line_width`

## Alternatives

`disp_obj`,
`disp_arrow`,
`disp_line`,
`disp_circle`,
`disp_rectangle1`,
`disp_rectangle2`,
`disp_ellipse`

## See also

`open_window`,
`set_color`,
`set_colored`,
`set_draw`,
`set_shape`,
`set_paint`,
`set_gray`,
`set_rgb`,
`set_hsi`,
`set_line_width`,
`set_line_style`,
`paint_region`,
`dump_window`

## Module

Foundation
