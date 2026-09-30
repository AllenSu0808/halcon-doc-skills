# bit_slice (Operator)

## Name

`bit_slice` — Extract a bit from the pixels.

## Signature

`def bit_slice(image: HObject, bit: int) -> HObject`

## Description

The operator `bit_slice` extracts a bit level from the input image.
The semantics of the “and” operation corresponds to that of C for the
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

**`image_slice`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4)

Result image(s) by extraction.

**`bit`** (input_control)  integer `→` int

Bit to be selected.

Default:
8

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 24, 30, 32

Minimum increment:
1

Recommended increment:
1

## Result

If the images are correct (type) and
*`bit`* has a valid value, the operator `bit_slice`
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

`bit_mask`

## See also

`bit_and`,
`bit_lshift`

## Module

Foundation
