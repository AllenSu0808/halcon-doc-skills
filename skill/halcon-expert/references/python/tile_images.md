# tile_images (Operator)

## Name

`tile_images` — Tile multiple image objects into a large image.

## Signature

`def tile_images(images: HObject, num_columns: int, tile_order: str) -> HObject`

## Description

`tile_images` tiles multiple input image objects, which must
contain the same number of channels, into a large image. The input
image object *`images`* contains *Num* images, which may
be of different size. All channels of *`images`* must be of the
same type. The output image *`tiled_image`* contains
as many channels as the input images. In the output image the
*Num* input images have been tiled into *`num_columns`*
columns. Each tile has the same size, which is determined by the
maximum width and height of all input images. If an input image is
smaller than the tile size it is copied to the center of the
respective tile. The parameter *`tile_order`* determines the
order in which the images are copied into the output in the cases in
which this is not already determined by *`num_columns`* (i.e.,
if *`num_columns`* != 1 and *`num_columns`* !=
*Num*). If *`tile_order`* = *"horizontal"* the
images are copied in the horizontal direction, i.e., the second
image of *`images`* will be to the right of the first image.
If *`tile_order`* = *"vertical"* the images are copied in
the vertical direction, i.e., the second image of *`images`*
will be below the first image. The domain of *`tiled_image`*
is obtained by copying the domains of *`images`* to the
corresponding locations in the output image. If *Num* is not
a multiple of *`num_columns`* the output image will have
undefined gray values in the lower right corner of the image. The
output domain will reflect this.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`images`** (input_object)  (multichannel-)image-array `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Input images.

**`tiled_image`** (output_object)  (multichannel-)image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Tiled output image.

**`num_columns`** (input_control)  integer `→` int

Number of columns to use for the output image.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7

Restriction:
`NumColumns >= 1`

**`tile_order`** (input_control)  string `→` str

Order of the input images in the output image.

Default:
"vertical"

List of values:
"horizontal", "vertical"

## Example (HDevelop)

```
* Grab 5 (multi-channel) images and stack them vertically.
gen_empty_obj (Images)
for I := 1 to 5 by 1
    grab_image_async (ImageGrabbed, AcqHandle, -1)
    concat_obj (Images, ImageGrabbed, Images)
endfor
tile_images (Images, TiledImage, 1, 'vertical')
```

## Result

`tile_images` returns 2 (
H_MSG_TRUE)
if all parameters are correct
and no error occurs during execution. If the input is empty the
behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`append_channel`

## Alternatives

`tile_channels`,
`tile_images_offset`

## See also

`change_format`,
`crop_part`,
`crop_rectangle1`

## Module

Foundation
