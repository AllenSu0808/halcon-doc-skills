# AppendChannel (Operator)

## Name

`AppendChannel` — Append additional matrices (channels) to the image.

## Signature

`static void HOperatorSet.AppendChannel(HObject multiChannelImage, HObject image, out HObject imageExtended)`

`HImage HImage.AppendChannel(HImage image)`

## Description

The operator `AppendChannel` appends the matrices of the
image *`image`* to the matrices of
*`multiChannelImage`*. The result is an image containing as
many matrices (channels) as *`multiChannelImage`* and
*`image`* combined. The definition domain of the output
image is calculated as the intersection of the definition domains of both
input images.
*`multiChannelImage`* may be a region only that is then interpreted as
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

**`multiChannelImage`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Multi-channel image.

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Image to be appended.

**`imageExtended`** (output_object)  multichannel-image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Image appended by *`image`*.

## Possible Successors

`DispImage`

## Alternatives

`Compose2`,
`Compose3`,
`Compose4`,
`Compose5`

## Module

Foundation
