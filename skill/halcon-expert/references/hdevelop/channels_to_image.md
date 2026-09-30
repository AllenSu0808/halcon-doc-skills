# channels_to_image (Operator)

## Name

`channels_to_image` — Convert one-channel images into a multi-channel image

## Signature

`channels_to_image(Images : MultiChannelImage : : )`

## Description

The operator `channels_to_image` converts several
one-channel images into a multi-channel image. The new definition
domain is the intersection of the definition domains of the input
images.
No new storage is allocated for the multi-channel images, unless images
of different dimensions are combined. In that case, new storage is allocated
for all images that do not have both maximum width and height among all
input images.
For all images with maximum dimensions, the created multi-channel image
contains references to the existing input images.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Images`** (input_object)  singlechannelimage-array `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

One-channel images to be combined into a
one-channel image.

**`MultiChannelImage`** (output_object)  multichannel-image `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Multi-channel image.

## Possible Successors

`count_channels`,
`disp_image`

## See also

`image_to_channels`

## Module

Foundation
