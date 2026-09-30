# Compose4 (Operator)

## Name

`Compose4` — Convert 4 images into a four-channel image.

## Signature

`static void HOperatorSet.Compose4(HObject image1, HObject image2, HObject image3, HObject image4, out HObject multiChannelImage)`

`HImage HImage.Compose4(HImage image2, HImage image3, HImage image4)`

## Description

The operator `Compose4` converts 4 one-channel images into
a 4-channel image. The definition domain is calculated as the
intersection of the definition domains of the input images.
No new storage is allocated for the multi-channel image.
Instead, the created multi-channel image contains references to the existing
input images.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image1`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image 1.

**`image2`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image 2.

**`image3`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image 3.

**`image4`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image 4.

**`multiChannelImage`** (output_object)  multichannel-image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Multi-channel image.

## Possible Successors

`DispImage`

## Alternatives

`AppendChannel`

## See also

`Decompose4`

## Module

Foundation
