# bit_rshift (Operator)

## Name

`bit_rshift` — Right shift of all pixels of the image.

## Signature

`bit_rshift(Image : ImageRShift : Shift : )`

## Description

The operator `bit_rshift` calculates a “right shift”
of all pixels of the input image bit by bit.
The semantics of the “right shift” operation corresponds to that of C
(“>>”) for the
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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4)

Input image(s).

**`ImageRShift`** (output_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4)

Result image(s) by shift operation.

**`Shift`** (input_control)  integer `→`  (integer)

shift value

Default:
3

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 24, 30, 31

Minimum increment:
1

Recommended increment:
1

## Example (C)

```
bit_rshift(Int2Image,&ReducedInt2Image,8);
convert_image_type(ReducedInt2Image,&ByteImage,"byte");
```

## Result

If the images are correct (type) and
*`Shift`* has a valid value the operator `bit_rshift`
returns the value 2 (
H_MSG_TRUE)
.
The behavior in case of empty input (no input images available) is
set via the operator
`set_system(::'no_object_result',<Result>:)`
If necessary an exception is raised.

## Alternatives

`scale_image`

## See also

`bit_lshift`

## Module

Foundation
