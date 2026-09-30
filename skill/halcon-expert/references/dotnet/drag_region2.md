# DragRegion2 (Operator)

## Name

`DragRegion2` — Interactive movement of a region with fixpoint specification.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`static void HOperatorSet.DragRegion2(HObject sourceRegion, out HObject destinationRegion, HTuple windowHandle, HTuple row, HTuple column)`

`HRegion HRegion.DragRegion2(HWindow windowHandle, int row, int column)`

`HRegion HWindow.DragRegion2(HRegion sourceRegion, int row, int column)`

## Description

You use `DragRegion2` to move a region on the display by mouse.
It corresponds to the operator [`DragRegion1`](drag_region1.md) with the
difference, that the position of the mouse cursor can be determined.

## Attention

Gray values of the regions are not moved.
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

`DragRegion2` returns 2 (
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
`SetDraw`,
`AffineTransImage`

## Alternatives

`GetMposition`,
`MoveRegion`,
`DragRegion1`,
`DragRegion3`

## See also

`SetDraw`,
`AffineTransImage`

## Module

Foundation
