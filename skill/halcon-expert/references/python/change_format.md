# change_format (Operator)

## Name

`change_format` — Change image size.

## Signature

`def change_format(image: HObject, width: int, height: int) -> HObject`

## Description

The operator `change_format` increases or decreases the size of the
input images to the indicated height or width, respectively. If the image is
reduced, parts are cut off at the “right” or “lower” edge of the image,
respectively. If the image is enlarged, the additional areas are set to 0.
The definition domain of the new image is equal to the domain of the input
image, clipped to the size of the new image. No zooming is carried out.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image.

**`image_part`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Image with new format.

**`width`** (input_control)  extent.x `→` int

Width of new image.

Default:
512

Suggested values:
32, 64, 128, 256, 512, 768, 1024

**`height`** (input_control)  extent.y `→` int

Height of new image.

Default:
512

Suggested values:
32, 64, 128, 256, 512, 525, 1024

## Possible Successors

`disp_image`

## Alternatives

`crop_part`

## See also

`zoom_image_size`,
`zoom_image_factor`

## Module

Foundation
