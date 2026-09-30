# append_channel (Operator)

## Name

`append_channel` — Append additional matrices (channels) to the image.

## Signature

`def append_channel(multi_channel_image: HObject, image: HObject) -> HObject`

## Description

The operator `append_channel` appends the matrices of the
image *`image`* to the matrices of
*`multi_channel_image`*. The result is an image containing as
many matrices (channels) as *`multi_channel_image`* and
*`image`* combined. The definition domain of the output
image is calculated as the intersection of the definition domains of both
input images.
*`multi_channel_image`* may be a region only that is then interpreted as
the definition domain of an image without channels.
No new storage is allocated for the multi-channel image.
Instead, the created multi-channel image contains references to the existing
input images.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`multi_channel_image`** (input_object)  (multichannel-)image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Multi-channel image.

**`image`** (input_object)  (multichannel-)image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Image to be appended.

**`image_extended`** (output_object)  multichannel-image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Image appended by *`image`*.

## Possible Successors

`disp_image`

## Alternatives

`compose2`,
`compose3`,
`compose4`,
`compose5`

## Module

Foundation
