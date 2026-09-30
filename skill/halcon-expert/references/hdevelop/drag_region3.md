# drag_region3 (Operator)

## Name

`drag_region3` — Interactive movement of a region with restriction of positions.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`drag_region3(SourceRegion, MaskRegion : DestinationRegion : WindowHandle, Row, Column : )`

## Description

You use `drag_region3` to move a region on the display by mouse.
It corresponds to the operator [`drag_region2`](drag_region2.md) with the
enhancement, that all points are specified which can be entered by mouse.
If you move the mouse outside of this area (*`MaskRegion`*), the
region on the point with the smallest distance inside *`MaskRegion`*
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

**`SourceRegion`** (input_object)  region-array `→` object

Regions to move.

**`MaskRegion`** (input_object)  region-array `→` object

Points on which it is allowed for a region to move.

**`DestinationRegion`** (output_object)  region-array `→` object

Moved regions.

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Row`** (input_control)  point.y `→`  (integer)

Row index of the reference point.

Default:
100

Suggested values:
0, 64, 128, 256, 512

Value range:
`0
≤
Row
≤
1024`

**`Column`** (input_control)  point.x `→`  (integer)

Column index of the reference point.

Default:
100

Suggested values:
0, 64, 128, 256, 512

Value range:
`0
≤
Column
≤
1024`

## Result

`drag_region3` returns 2 (
H_MSG_TRUE)
if a region is entered and if the window
is valid.
If necessary, an exception is raised.
You may determine the behavior after an empty input with
`set_system(::'no_object_result',<Result>:)`.

## Possible Predecessors

`open_window`,
`get_mposition`

## Possible Successors

`reduce_domain`,
`disp_region`,
`set_colored`,
`set_line_width`,
`set_draw`,
`affine_trans_image`

## Alternatives

`get_mposition`,
`move_region`,
`drag_region1`,
`drag_region2`

## See also

`set_draw`,
`affine_trans_image`

## Module

Foundation
