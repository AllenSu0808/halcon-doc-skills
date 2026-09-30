# Compose2 (Operator)

## Name

`Compose2` — Convert two images into a two-channel image.

## Signature

`static void HOperatorSet.Compose2(HObject image1, HObject image2, out HObject multiChannelImage)`

`HImage HImage.Compose2(HImage image2)`

## Description

The operator `Compose2` converts 2 one-channel images into
a 2-channel image. The definition domain is calculated as the
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

**`multiChannelImage`** (output_object)  multichannel-image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Multi-channel image.

## Possible Successors

`DispImage`

## Alternatives

`AppendChannel`

## See also

`Decompose2`

## Module

Foundation
