# disp_image (Operator)

## Name

`disp_image` — Displays gray value images.

## Signature

`def disp_image(image: HObject, window_handle: HHandle) -> None`

## Description

`disp_image` displays the gray values of an image in the
output window. The gray value pixels of the definition domain
(`set_comprise(::WindowHandle,'object':)`) or of the whole image
(`set_comprise(::WindowHandle,'image':)`) are used. Restriction to the
definition domain is the default.

For the display of gray value images the number of gray values is usually
reduced. This is due to the fact that colors have to be reserved for the
display of graphics (e.g., [`set_color`](set_color.md)) and the window manager.
Also depending on the number of bit planes on the used output device often
less than 256 colors (eight bit planes) are available. The number of
”colors” actually reserved for the display of gray values can be queried
by [`get_system`](get_system.md). Before opening the first window this value can be
modified by [`set_system`](set_system.md). For instance for 8 bit planes 200 real
gray values are the default.

The reduction of the number of gray values does not pose problems as long
as only gray value information is displayed, humans cannot distinguish
256 different shades of gray. If certain gray values are used for the
representation of region information (which is not the style commonly used
in HALCON), confusions might be the result, since different
numerical values are displayed on the screen with the same gray
value. The operator [`label_to_region`](label_to_region.md) should be used on
these images in order to transform the label data into HALCON objects.

If images of type `int2`, `int4`, `int8`, `real`
or `complex` are displayed, the smallest and largest gray value is
computed. For images of the type `complex` this computation is based
on the corresponding power spectrum.
Afterwards the pixel data is rescaled according to the
number of available gray values (depending on the output device, e.g., 200).
It is possible that some pixels have a very different value than
the other pixels. This might lead to the display of an (almost)
completely white or black image.
In order to decide if the current image is a binary image
[`min_max_gray`](min_max_gray.md) can be used. If necessary the image can be
transformed or converted by [`scale_image`](scale_image.md) and
[`convert_image_type`](convert_image_type.md) before it is displayed.

## Attention

If a wrong output mode was set by [`set_paint`](set_paint.md), the error will be
reported when `disp_image` is used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Gray value image to display.

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

## Result

If the used image contains valid values and a correct
output mode is set, `disp_image` returns 2 (
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

`disp_obj`,
`disp_color`

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
