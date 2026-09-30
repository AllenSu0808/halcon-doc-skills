# tile_images (Operator)

## Name

`tile_images` — Tile multiple image objects into a large image.

## Signature

`tile_images(Images : TiledImage : NumColumns, TileOrder : )`

## Description

`tile_images` tiles multiple input image objects, which must
contain the same number of channels, into a large image. The input
image object *`Images`* contains *Num* images, which may
be of different size. All channels of *`Images`* must be of the
same type. The output image *`TiledImage`* contains
as many channels as the input images. In the output image the
*Num* input images have been tiled into *`NumColumns`*
columns. Each tile has the same size, which is determined by the
maximum width and height of all input images. If an input image is
smaller than the tile size it is copied to the center of the
respective tile. The parameter *`TileOrder`* determines the
order in which the images are copied into the output in the cases in
which this is not already determined by *`NumColumns`* (i.e.,
if *`NumColumns`* != 1 and *`NumColumns`* !=
*Num*). If *`TileOrder`* = *'horizontal'* the
images are copied in the horizontal direction, i.e., the second
image of *`Images`* will be to the right of the first image.
If *`TileOrder`* = *'vertical'* the images are copied in
the vertical direction, i.e., the second image of *`Images`*
will be below the first image. The domain of *`TiledImage`*
is obtained by copying the domains of *`Images`* to the
corresponding locations in the output image. If *Num* is not
a multiple of *`NumColumns`* the output image will have
undefined gray values in the lower right corner of the image. The
output domain will reflect this.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Images`** (input_object)  (multichannel-)image-array `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Input images.

**`TiledImage`** (output_object)  (multichannel-)image `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Tiled output image.

**`NumColumns`** (input_control)  integer `→`  (integer)

Number of columns to use for the output image.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7

Restriction:
`NumColumns >= 1`

**`TileOrder`** (input_control)  string `→`  (string)

Order of the input images in the output image.

Default:
'vertical'

List of values:
'horizontal', 'vertical'

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
