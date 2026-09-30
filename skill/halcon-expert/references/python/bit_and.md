# bit_and (Operator)

## Name

`bit_and` — Bit-by-bit AND of all pixels of the input images.

## Signature

`def bit_and(image_1: HObject, image_2: HObject) -> HObject`

## Description

The operator `bit_and` calculates the “and”
of all pixels of the input images bit by bit.
The semantics of the “and” operation corresponds to that of C for the
respective types (signed char, unsigned char, short, unsigned short, int/long).
The images must have the same size and pixel type.
The pixels within the definition range of the image in the first
parameter are processed.

Several images can be processed in one call. In this case
both input parameters contain the same number of images
which are then processed in pairs.
An output image is generated for every pair.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image_1`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4)

Input image(s) 1.

**`image_2`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4)

Input image(s) 2.

**`image_and`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4)

Result image(s) by AND-operation.

## Result

If the images are correct (type and number) the operator `bit_and`
returns the value 2 (
H_MSG_TRUE)
.
The behavior in case of empty input (no input images available) is
set via the operator
`set_system(::'no_object_result',<Result>:)`
If necessary an exception is raised.

## Alternatives

`bit_mask`,
`add_image`,
`max_image`

## See also

`bit_mask`,
`add_image`,
`max_image`

## Module

Foundation
