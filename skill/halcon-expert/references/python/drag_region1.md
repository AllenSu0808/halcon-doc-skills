# drag_region1 (Operator)

## Name

`drag_region1` — Interactive moving of a region.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`def drag_region1(source_region: HObject, window_handle: HHandle) -> HObject`

## Description

`drag_region1` is used to move a region on the display by mouse.
Calling `drag_region1` turns the region visible as soon as the left
mouse button is pressed. Therefore the region's edges are displayed only.
As representation mode the mode 'not' (see [`set_draw`](set_draw.md)) is used
during procedure's permanence.
During the movement the cursor resides in the region's barycenter.
If you move the mouse with pressed left mouse button, the depicted region
follows - delayed - this movement. If you press the right mouse button you
terminate `drag_region1`. The depicted region disappears from the
display. Output is a region which corresponds to the last position on the display.
You may pass even several regions at once.
The operator [`affine_trans_image`](affine_trans_image.md) moves the gray values.

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

**`source_region`** (input_object)  region-array `→` HObject

Regions to move.

**`destination_region`** (output_object)  region-array `→` HObject

Moved Regions.

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

## Result

`drag_region1` returns 2 (
H_MSG_TRUE)
if a region is entered and the window
is valid.
If necessary, an exception is raised.
You may determine the behavior after an empty input with
`set_system(::'no_object_result',<Result>:)`.

## Possible Predecessors

`open_window`

## Possible Successors

`reduce_domain`,
`disp_region`,
`set_colored`,
`set_line_width`,
`set_draw`

## Alternatives

`get_mposition`,
`move_region`

## See also

`set_draw`,
`affine_trans_image`

## Module

Foundation
