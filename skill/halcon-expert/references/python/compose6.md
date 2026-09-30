# compose6 (Operator)

## Name

`compose6` — Convert 6 images into a six-channel image.

## Signature

`def compose6(image_1: HObject, image_2: HObject, image_3: HObject, image_4: HObject, image_5: HObject, image_6: HObject) -> HObject`

## Description

The operator `compose6` converts 6 one-channel images into
a 6-channel image. The definition domain is calculated as the
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

**`image_3`** (input_object)  singlechannelimage(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image 3.

**`image_4`** (input_object)  singlechannelimage(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image 4.

**`image_5`** (input_object)  singlechannelimage(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image 5.

**`image_6`** (input_object)  singlechannelimage(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image 6.

**`multi_channel_image`** (output_object)  multichannel-image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Multi-channel image.

## Possible Successors

`disp_image`

## Alternatives

`append_channel`

## See also

`decompose6`

## Module

Foundation
