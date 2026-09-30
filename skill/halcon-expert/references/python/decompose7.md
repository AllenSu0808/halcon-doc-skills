# decompose7 (Operator)

## Name

`decompose7` — Convert a seven-channel image into seven images.

## Signature

`def decompose7(multi_channel_image: HObject) -> Tuple[HObject, HObject, HObject, HObject, HObject, HObject, HObject]`

## Description

The operator `decompose7` converts a 7-channel image into
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

**`multi_channel_image`** (input_object)  multichannel-image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Multi-channel image.

**`image_1`** (output_object)  singlechannelimage(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Output image 1.

**`image_2`** (output_object)  singlechannelimage(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Output image 2.

**`image_3`** (output_object)  singlechannelimage(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Output image 3.

**`image_4`** (output_object)  singlechannelimage(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Output image 4.

**`image_5`** (output_object)  singlechannelimage(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Output image 5.

**`image_6`** (output_object)  singlechannelimage(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Output image 6.

**`image_7`** (output_object)  singlechannelimage(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Output image 7.

## Possible Predecessors

`count_channels`

## Possible Successors

`disp_image`

## Alternatives

`access_channel`,
`image_to_channels`

## See also

`compose7`

## Module

Foundation
