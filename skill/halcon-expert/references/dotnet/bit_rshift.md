# BitRshift (Operator)

## Name

`BitRshift` — Right shift of all pixels of the image.

## Signature

`static void HOperatorSet.BitRshift(HObject image, out HObject imageRShift, HTuple shift)`

`HImage HImage.BitRshift(int shift)`

## Description

The operator `BitRshift` calculates a “right shift”
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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4)

Input image(s).

**`imageRShift`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4)

Result image(s) by shift operation.

**`shift`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

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
*`shift`* has a valid value the operator `BitRshift`
returns the value 2 (
H_MSG_TRUE)
.
The behavior in case of empty input (no input images available) is
set via the operator
`set_system(::'no_object_result',<Result>:)`
If necessary an exception is raised.

## Alternatives

`ScaleImage`

## See also

`BitLshift`

## Module

Foundation
