# bit_not (Operator)

## Name

`bit_not` — Complement all bits of the pixels.

## Signature

`def bit_not(image: HObject) -> HObject`

## Description

The operator `bit_not` calculates the “complement”
of all pixels of the input image bit by bit.
The semantics of the “complement” operation corresponds to that of C
(“~”) for the
respective types (signed char, unsigned char, short, unsigned short, int/long).
Only the pixels within the definition range of the image
are processed.

Several images can be processed in one call.
An output image is generated for every input image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4)

Input image(s).

**`image_not`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4)

Result image(s) by complement operation.

## Result

If the images are correct (type) the operator `bit_not`
returns the value 2 (
H_MSG_TRUE)
.
The behavior in case of empty input (no input images available) is
set via the operator
`set_system(::'no_object_result',<Result>:)`
If necessary an exception is raised.

## Alternatives

`bit_or`,
`bit_and`,
`add_image`

## See also

`bit_slice`,
`bit_mask`

## Module

Foundation
