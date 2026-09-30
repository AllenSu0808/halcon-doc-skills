# ImageToChannels (Operator)

## Name

`ImageToChannels` — Convert a multi-channel image into One-channel images

## Signature

`static void HOperatorSet.ImageToChannels(HObject multiChannelImage, out HObject images)`

`HImage HImage.ImageToChannels()`

## Description

The operator `ImageToChannels` generates a one-channel
image for each channel of the multi-channel image in
*`multiChannelImage`*. The definition domains are adopted
from the input image. As many images are created as
*`multiChannelImage`* has channels.
No new storage is allocated for the output images.
Instead, the created images contain references to the existing
input image channels.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`multiChannelImage`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Multi-channel image to be decomposed.

**`images`** (output_object)  singlechannelimage-array `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Generated one-channel images.

## Possible Predecessors

`CountChannels`

## Possible Successors

`DispImage`

## Alternatives

`AccessChannel`,
`Decompose2`,
`Decompose3`,
`Decompose4`,
`Decompose5`

## See also

`ChannelsToImage`

## Module

Foundation
