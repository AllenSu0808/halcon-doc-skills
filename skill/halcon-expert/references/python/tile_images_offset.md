# tile_images_offset (Operator)

## Name

`tile_images_offset` — Tile multiple image objects into a large image with explicit
positioning information.

## Signature

`def tile_images_offset(images: HObject, offset_row: MaybeSequence[int], offset_col: MaybeSequence[int], row_1: MaybeSequence[int], col_1: MaybeSequence[int], row_2: MaybeSequence[int], col_2: MaybeSequence[int], width: int, height: int) -> HObject`

## Description

`tile_images_offset` tiles multiple input image objects, which
must contain the same number of channels, into a large image. The
input image object *`images`* contains *Num* images,
which may be of different size. All channels of *`images`*
must be of the same type. The output image
*`tiled_image`* contains as many channels as the input images.
The size of the output image is determined by the parameters
*`width`* and *`height`*. The position of the upper left
corner of the input images in the output images is determined by the
parameters *`offset_row`* and *`offset_col`*. Both
parameters must contain exactly *Num* values. Optionally,
each input image can be cropped to an arbitrary rectangle that is
smaller than the input image. To do so, the parameters
*`row_1`*, *`col_1`*, *`row_2`*, and *`col_2`* must
be set accordingly. If any of these four parameters is set to
*-1*, the corresponding input image is not cropped. In any
case, all four parameters must contain *Num* values. If the
input images are cropped the position parameters *`offset_row`*
and *`offset_col`* refer to the upper left corner of the cropped
image. If the input images overlap each other in the output image
(while taking into account their respective domains), the image with
the higher index in *`images`* overwrites the image data of the
image with the lower index. The domain of *`tiled_image`* is
obtained by copying the domains of *`images`* to the
corresponding locations in the output image.

## Attention

If the input images all have the same size and tile the output image
exactly, the operator [`tile_images`](tile_images.md) usually will be slightly
faster.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`images`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Input images.

**`tiled_image`** (output_object)  (multichannel-)image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Tiled output image.

**`offset_row`** (input_control)  point.y(-array) `→` MaybeSequence[int]

Row coordinate of the upper left corner of the
input images in the output image.

Default:
0

Suggested values:
0, 50, 100, 150, 200, 250

**`offset_col`** (input_control)  point.x(-array) `→` MaybeSequence[int]

Column coordinate of the upper left corner of the
input images in the output image.

Default:
0

Suggested values:
0, 50, 100, 150, 200, 250

**`row_1`** (input_control)  rectangle.origin.y(-array) `→` MaybeSequence[int]

Row coordinate of the upper left corner of the
copied part of the respective input image.

Default:
-1

Suggested values:
-1, 0, 10, 20, 50, 100, 200, 300, 500

**`col_1`** (input_control)  rectangle.origin.x(-array) `→` MaybeSequence[int]

Column coordinate of the upper left corner of the
copied part of the respective input image.

Default:
-1

Suggested values:
-1, 0, 10, 20, 50, 100, 200, 300, 500

**`row_2`** (input_control)  rectangle.corner.y(-array) `→` MaybeSequence[int]

Row coordinate of the lower right corner of the
copied part of the respective input image.

Default:
-1

Suggested values:
-1, 0, 10, 20, 50, 100, 200, 300, 500

**`col_2`** (input_control)  rectangle.corner.x(-array) `→` MaybeSequence[int]

Column coordinate of the lower right corner of the
copied part of the respective input image.

Default:
-1

Suggested values:
-1, 0, 10, 20, 50, 100, 200, 300, 500

**`width`** (input_control)  extent.x `→` int

Width of the output image.

Default:
512

Suggested values:
32, 64, 128, 256, 512, 768, 1024, 2048, 4096

**`height`** (input_control)  extent.y `→` int

Height of the output image.

Default:
512

Suggested values:
32, 64, 128, 256, 512, 525, 1024, 2048, 4096

## Example (HDevelop)

```
* Example 1
* Grab 2 (multi-channel) NTSC images, crop the bottom 5 lines off
* of each image, the right 5 columns off of the first image, and
* the left five lines off of the second image, and put the cropped
* images side-by-side.
gen_empty_obj (Images)
for I := 1 to 2 by 1
    grab_image_async (ImageGrabbed, AcqHandle, -1)
    concat_obj (Images, ImageGrabbed, Images)
endfor
tile_images_offset (Images, TiledImage, [0,635], [0,0], [0,0], \
                    [0,5], [474,474], [634,639], 635, 950)

* Example 2
* Enlarge image by 15 rows and columns on all sides
EnlargeColsBy := 15
EnlargeRowsBy := 15
get_image_pointer1 (Image, Pointer, Type, WidthImage, HeightImage)
tile_images_offset (Image, EnlargedImage, EnlargeRowsBy, EnlargeColsBy, \
                    -1, -1, -1, -1, WidthImage + EnlargeColsBy*2, \
                    HeightImage + EnlargeRowsBy*2)
```

## Result

`tile_images_offset` returns 2 (
H_MSG_TRUE)
if all parameters are
correct and no error occurs during execution. If the input is empty
the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`append_channel`

## Alternatives

`tile_channels`,
`tile_images`

## See also

`change_format`,
`crop_part`,
`crop_rectangle1`

## Module

Foundation
