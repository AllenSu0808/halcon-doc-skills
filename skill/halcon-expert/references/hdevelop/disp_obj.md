# disp_obj (Operator)

## Name

`disp_obj` — Displays image objects (image, region, XLD).

## Signature

`disp_obj(Object : : WindowHandle : )`

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

**`Object`** (input_object)  object(-array) `→` object

Image object to be displayed.

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

## Example (HDevelop)

```
* Output of a gray image:
read_image(Image1,'monkey')
disp_obj(Image1,WindowHandle)
threshold(Image,Region,0,128)
disp_obj(Region,WindowHandle)
```

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
