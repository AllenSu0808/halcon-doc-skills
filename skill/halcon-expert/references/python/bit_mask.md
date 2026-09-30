# bit_mask (Operator)

## Name

`bit_mask` — Logical “AND” of each pixel using a bit mask.

## Signature

`def bit_mask(image: HObject, bit_mask: int) -> HObject`

## Description

The operator `bit_mask` carries out an “and” operation
of each pixel with a fixed mask.
The semantics of the “and” operation corresponds to that of C for the
respective types (signed char, unsigned char, unsigned short, short, int/long).
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

**`image_mask`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4)

Result image(s) by combination with mask.

**`bit_mask`** (input_control)  integer `→` int

Bit field

Default:
128

Suggested values:
1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096

## Result

If the images are correct (type) the operator `bit_mask`
returns the value 2 (
H_MSG_TRUE)
.
The behavior in case of empty input (no input images available) is
set via the operator
`set_system(::'no_object_result',<Result>:)`
If necessary an exception is raised.

## Possible Successors

`threshold`,
`bit_or`

## Alternatives

`bit_slice`

## See also

`bit_and`,
`bit_lshift`

## Module

Foundation
