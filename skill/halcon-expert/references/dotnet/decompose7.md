# Decompose7 (Operator)

## Name

`Decompose7` — Convert a seven-channel image into seven images.

## Signature

`static void HOperatorSet.Decompose7(HObject multiChannelImage, out HObject image1, out HObject image2, out HObject image3, out HObject image4, out HObject image5, out HObject image6, out HObject image7)`

`HImage HImage.Decompose7(out HImage image2, out HImage image3, out HImage image4, out HImage image5, out HImage image6, out HImage image7)`

## Description

The operator `Decompose7` converts a 7-channel image into
seven one-channel images with the same definition domain.
No new storage is allocated for the output images.
Instead, the created images contain references to the existing
input image channels.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`multiChannelImage`** (input_object)  multichannel-image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Multi-channel image.

**`image1`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Output image 1.

**`image2`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Output image 2.

**`image3`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Output image 3.

**`image4`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Output image 4.

**`image5`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Output image 5.

**`image6`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Output image 6.

**`image7`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Output image 7.

## Possible Predecessors

`CountChannels`

## Possible Successors

`DispImage`

## Alternatives

`AccessChannel`,
`ImageToChannels`

## See also

`Compose7`

## Module

Foundation
