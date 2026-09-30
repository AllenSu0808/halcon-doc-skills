# compose4 (Operator)

## Name

`compose4` — Convert 4 images into a four-channel image.

## Signature

`compose4(Image1, Image2, Image3, Image4 : MultiChannelImage : : )`

## Description

The operator `compose4` converts 4 one-channel images into
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

**`Image1`** (input_object)  singlechannelimage(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image 1.

**`Image2`** (input_object)  singlechannelimage(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image 2.

**`Image3`** (input_object)  singlechannelimage(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image 3.

**`Image4`** (input_object)  singlechannelimage(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image 4.

**`MultiChannelImage`** (output_object)  multichannel-image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Multi-channel image.

## Possible Successors

`disp_image`

## Alternatives

`append_channel`

## See also

`decompose4`

## Module

Foundation
