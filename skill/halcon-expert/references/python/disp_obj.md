# disp_obj (Operator)

## Name

`disp_obj` — Displays image objects (image, region, XLD).

## Signature

`def disp_obj(object: HObject, window_handle: HHandle) -> None`

## Description

`disp_obj` displays objects depending of their kind.
`disp_obj` is equivalent to [`disp_image`](disp_image.md)
for one channel images, equivalent to [`disp_color`](disp_color.md)
for three channel images, equivalent to [`disp_region`](disp_region.md)
for regions and equivalent to [`disp_xld`](disp_xld.md) for XLDs.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`object`** (input_object)  object(-array) `→` HObject

Image object to be displayed.

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

## Result

If the used object is valid and a correct
output mode is set, `disp_obj` returns 2 (
H_MSG_TRUE)
. Otherwise an
exception is raised.

## Possible Predecessors

`open_window`,
`set_rgb`,
`set_lut`,
`set_hsi`,
`scale_image`,
`convert_image_type`,
`min_max_gray`

## Alternatives

`disp_color`,
`disp_image`,
`disp_xld`,
`disp_region`

## See also

`open_window`,
`reset_obj_db`,
`set_paint`,
`set_lut`,
`paint_gray`,
`scale_image`,
`convert_image_type`,
`dump_window`

## Module

Foundation
