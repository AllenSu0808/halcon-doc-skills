# compose2 (Operator)

## Name

`compose2` — Convert two images into a two-channel image.

## Signature

`def compose2(image_1: HObject, image_2: HObject) -> HObject`

## Description

The operator `compose2` converts 2 one-channel images into
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

**`image_1`** (input_object)  singlechannelimage(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image 1.

**`image_2`** (input_object)  singlechannelimage(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image 2.

**`multi_channel_image`** (output_object)  multichannel-image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Multi-channel image.

## Possible Successors

`disp_image`

## Alternatives

`append_channel`

## See also

`decompose2`

## Module

Foundation
