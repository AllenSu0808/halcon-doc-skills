# drag_region3 (Operator)

## Name

`drag_region3` — Interactive movement of a region with restriction of positions.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`def drag_region3(source_region: HObject, mask_region: HObject, window_handle: HHandle, row: int, column: int) -> HObject`

## Description

You use `drag_region3` to move a region on the display by mouse.
It corresponds to the operator [`drag_region2`](drag_region2.md) with the
enhancement, that all points are specified which can be entered by mouse.
If you move the mouse outside of this area (*`mask_region`*), the
region on the point with the smallest distance inside *`mask_region`*
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

**`source_region`** (input_object)  region-array `→` HObject

Regions to move.

**`mask_region`** (input_object)  region-array `→` HObject

Points on which it is allowed for a region to move.

**`destination_region`** (output_object)  region-array `→` HObject

Moved regions.

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`row`** (input_control)  point.y `→` int

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

**`column`** (input_control)  point.x `→` int

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
