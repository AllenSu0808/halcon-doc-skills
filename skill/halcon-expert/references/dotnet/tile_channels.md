# TileChannels (Operator)

## Name

`TileChannels` — Tile multiple images into a large image.

## Signature

`static void HOperatorSet.TileChannels(HObject image, out HObject tiledImage, HTuple numColumns, HTuple tileOrder)`

`HImage HImage.TileChannels(int numColumns, string tileOrder)`

## Description

`TileChannels` tiles an image consisting of multiple channels
into a large single-channel image. The input image *`image`*
contains *Num* images of the same size, which are stored in
the individual channels. All channels of *`image`*
must be of the same type. The output image *`tiledImage`*
contains a single channel image, where the *Num* input
channels have been tiled into *`numColumns`* columns. In
particular, this means that `TileChannels` cannot tile color
images. For this purpose, [`TileImages`](tile_images.md) can be used. The
parameter *`tileOrder`* determines the order in which the
images are copied into the output in the cases in which this is not
already determined by *`numColumns`* (i.e., if
*`numColumns`* != 1 and *`numColumns`* != *Num*).
If *`tileOrder`* = *"horizontal"* the images are copied
in the horizontal direction, i.e., the second channel of
*`image`* will be to the right of the first channel. If
*`tileOrder`* = *"vertical"* the images are copied in
the vertical direction, i.e., the second channel of *`image`*
will be below the first channel. The domain of *`tiledImage`*
is obtained by copying the domain of *`image`* to the
corresponding locations in the output image. If *Num* is not
a multiple of *`numColumns`* the output image will have
undefined gray values in the lower right corner of the image. The
output domain will reflect this.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Input image.

**`tiledImage`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Tiled output image.

**`numColumns`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of columns to use for the output image.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7

Restriction:
`NumColumns >= 1`

**`tileOrder`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

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

`TileChannels` returns 2 (
H_MSG_TRUE)
if all parameters are correct
and no error occurs during execution. If the input is empty the
behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`AppendChannel`

## Alternatives

`TileImages`,
`TileImagesOffset`

## See also

`ChangeFormat`,
`CropPart`,
`CropRectangle1`

## Module

Foundation
