# decompose2 (Operator)

## Name

`decompose2` — Convert a two-channel image into two images.

## Signature

`decompose2(MultiChannelImage : Image1, Image2 : : )`

## Description

The operator `decompose2` converts a 2-channel image into
two one-channel images with the same definition domain.
No new storage is allocated for the output images.
Instead, the created images contain references to the existing
input image channels.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`MultiChannelImage`** (input_object)  multichannel-image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Multi-channel image.

**`Image1`** (output_object)  singlechannelimage(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Output image 1.

**`Image2`** (output_object)  singlechannelimage(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Output image 2.

## Possible Predecessors

`count_channels`

## Possible Successors

`disp_image`

## Alternatives

`access_channel`,
`image_to_channels`

## See also

`compose2`

## Module

Foundation
