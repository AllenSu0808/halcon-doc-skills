# tile_channels (Operator)

## Name

`tile_channels` — Tile multiple images into a large image.

## Signature

`def tile_channels(image: HObject, num_columns: int, tile_order: str) -> HObject`

## Description

`tile_channels` tiles an image consisting of multiple channels
into a large single-channel image. The input image *`image`*
contains *Num* images of the same size, which are stored in
the individual channels. All channels of *`image`*
must be of the same type. The output image *`tiled_image`*
contains a single channel image, where the *Num* input
channels have been tiled into *`num_columns`* columns. In
particular, this means that `tile_channels` cannot tile color
images. For this purpose, [`tile_images`](tile_images.md) can be used. The
parameter *`tile_order`* determines the order in which the
images are copied into the output in the cases in which this is not
already determined by *`num_columns`* (i.e., if
*`num_columns`* != 1 and *`num_columns`* != *Num*).
If *`tile_order`* = *"horizontal"* the images are copied
in the horizontal direction, i.e., the second channel of
*`image`* will be to the right of the first channel. If
*`tile_order`* = *"vertical"* the images are copied in
the vertical direction, i.e., the second channel of *`image`*
will be below the first channel. The domain of *`tiled_image`*
is obtained by copying the domain of *`image`* to the
corresponding locations in the output image. If *Num* is not
a multiple of *`num_columns`* the output image will have
undefined gray values in the lower right corner of the image. The
output domain will reflect this.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Input image.

**`tiled_image`** (output_object)  singlechannelimage(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

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
* Grab 5 single-channel images and stack them vertically.
gen_rectangle1 (Image, 0, 0, Height-1, Width-1)
for I := 1 to 5 by 1
    grab_image_async (ImageGrabbed, AcqHandle, -1)
    append_channel (Image, ImageGrabbed, Image)
endfor
tile_channels (Image, TiledImage, 1, 'vertical')
```

## Result

`tile_channels` returns 2 (
H_MSG_TRUE)
if all parameters are correct
and no error occurs during execution. If the input is empty the
behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`append_channel`

## Alternatives

`tile_images`,
`tile_images_offset`

## See also

`change_format`,
`crop_part`,
`crop_rectangle1`

## Module

Foundation
