# DragRegion1 (Operator)

## Name

`DragRegion1` — Interactive moving of a region.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`static void HOperatorSet.DragRegion1(HObject sourceRegion, out HObject destinationRegion, HTuple windowHandle)`

`HRegion HRegion.DragRegion1(HWindow windowHandle)`

`HRegion HWindow.DragRegion1(HRegion sourceRegion)`

## Description

`DragRegion1` is used to move a region on the display by mouse.
Calling `DragRegion1` turns the region visible as soon as the left
mouse button is pressed. Therefore the region's edges are displayed only.
As representation mode the mode 'not' (see [`SetDraw`](set_draw.md)) is used
during procedure's permanence.
During the movement the cursor resides in the region's barycenter.
If you move the mouse with pressed left mouse button, the depicted region
follows - delayed - this movement. If you press the right mouse button you
terminate `DragRegion1`. The depicted region disappears from the
display. Output is a region which corresponds to the last position on the display.
You may pass even several regions at once.
The operator [`AffineTransImage`](affine_trans_image.md) moves the gray values.

## Attention

Gray values of regions are not moved.
With moving the input region it is not sure whether the gray values of the
output regions are filled reasonable. This may occur if the gray values of the
input regions do not comprise the whole image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`sourceRegion`** (input_object)  region-array `→` [HRegion](HRegion.md)

Regions to move.

**`destinationRegion`** (output_object)  region-array `→` [HRegion](HRegion.md)

Moved Regions.

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

## Example (HDevelop)

```
draw_region(Obj,WindowHandle)
dev_set_color ('green')
drag_region1(Obj,New,WindowHandle)
dev_display(New)
get_region_runs (Obj, Rows1, ColumnBegins1, ColumnEnds1)
get_region_runs (New, Rows2, ColumnBegins2, ColumnEnds2)
Row1 := Rows1[0]
Column1 := ColumnBegins1[0]
Row2 := Rows2[0]
Column2 := ColumnBegins2[0]
dev_set_color ('white')
gen_arrow_contour_xld (Arrow, Row1,Column1,Row2,Column2, 5, 5)
dev_display (Arrow)
```

## Result

`DragRegion1` returns 2 (
H_MSG_TRUE)
if a region is entered and the window
is valid.
If necessary, an exception is raised.
You may determine the behavior after an empty input with
`set_system(::'no_object_result',<Result>:)`.

## Possible Predecessors

`OpenWindow`

## Possible Successors

`ReduceDomain`,
`DispRegion`,
`SetColored`,
`SetLineWidth`,
`SetDraw`

## Alternatives

`GetMposition`,
`MoveRegion`

## See also

`SetDraw`,
`AffineTransImage`

## Module

Foundation
