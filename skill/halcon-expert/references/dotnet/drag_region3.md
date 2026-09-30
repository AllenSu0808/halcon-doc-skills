# DragRegion3 (Operator)

## Name

`DragRegion3` — Interactive movement of a region with restriction of positions.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`static void HOperatorSet.DragRegion3(HObject sourceRegion, HObject maskRegion, out HObject destinationRegion, HTuple windowHandle, HTuple row, HTuple column)`

`HRegion HRegion.DragRegion3(HRegion maskRegion, HWindow windowHandle, int row, int column)`

`HRegion HWindow.DragRegion3(HRegion sourceRegion, HRegion maskRegion, int row, int column)`

## Description

You use `DragRegion3` to move a region on the display by mouse.
It corresponds to the operator [`DragRegion2`](drag_region2.md) with the
enhancement, that all points are specified which can be entered by mouse.
If you move the mouse outside of this area (*`maskRegion`*), the
region on the point with the smallest distance inside *`maskRegion`*
will be displayed.

## Attention

The region's gray values are not moved.
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

**`maskRegion`** (input_object)  region-array `→` [HRegion](HRegion.md)

Points on which it is allowed for a region to move.

**`destinationRegion`** (output_object)  region-array `→` [HRegion](HRegion.md)

Moved regions.

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`row`** (input_control)  point.y `→` [HTuple](HTuple.md) (*int* / long)

Row index of the reference point.

Default:
100

Suggested values:
0, 64, 128, 256, 512

Value range:
`0
≤
row
≤
1024`

**`column`** (input_control)  point.x `→` [HTuple](HTuple.md) (*int* / long)

Column index of the reference point.

Default:
100

Suggested values:
0, 64, 128, 256, 512

Value range:
`0
≤
column
≤
1024`

## Result

`DragRegion3` returns 2 (
H_MSG_TRUE)
if a region is entered and if the window
is valid.
If necessary, an exception is raised.
You may determine the behavior after an empty input with
`set_system(::'no_object_result',<Result>:)`.

## Possible Predecessors

`OpenWindow`,
`GetMposition`

## Possible Successors

`ReduceDomain`,
`DispRegion`,
`SetColored`,
`SetLineWidth`,
`SetDraw`,
`AffineTransImage`

## Alternatives

`GetMposition`,
`MoveRegion`,
`DragRegion1`,
`DragRegion2`

## See also

`SetDraw`,
`AffineTransImage`

## Module

Foundation
