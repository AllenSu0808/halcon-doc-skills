# image_to_channels (Operator)

## Name

`image_to_channels` — Convert a multi-channel image into One-channel images

## Signature

`image_to_channels(MultiChannelImage : Images : : )`

## Description

The operator `image_to_channels` generates a one-channel
image for each channel of the multi-channel image in
*`MultiChannelImage`*. The definition domains are adopted
from the input image. As many images are created as
*`MultiChannelImage`* has channels.
No new storage is allocated for the output images.
Instead, the created images contain references to the existing
input image channels.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MultiChannelImage`** (input_object)  (multichannel-)image `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Multi-channel image to be decomposed.

**`Images`** (output_object)  singlechannelimage-array `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Generated one-channel images.

## Possible Predecessors

`count_channels`

## Possible Successors

`disp_image`

## Alternatives

`access_channel`,
`decompose2`,
`decompose3`,
`decompose4`,
`decompose5`

## See also

`channels_to_image`

## Module

Foundation
