# BitLshift (Operator)

## Name

`BitLshift` — Left shift of all pixels of the image.

## Signature

`static void HOperatorSet.BitLshift(HObject image, out HObject imageLShift, HTuple shift)`

`HImage HImage.BitLshift(int shift)`

## Description

The operator `BitLshift` calculates a “left shift”
of all pixels of the input image bit by bit.
The semantics of the “left shift” operation corresponds to that of C
(“<<“) for the
respective types (signed char, unsigned char, short, unsigned short, int/long).
If an overflow occurs the result is limited to the maximum
value of the respective pixel type.
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

**`imageLShift`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4)

Result image(s) by shift operation.

**`shift`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Shift value.

Default:
3

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 24, 30, 31

Minimum increment:
1

Recommended increment:
1

## Example (C)

```
read_image(&ByteImage,"fabrik");
convert_image_type(ByteImage,&Int2Image,"int2");
bit_lshift(Int2Image,&FullInt2Image,8);
```

## Result

If the images are correct (type) and if
*`shift`* has a valid value the operator `BitLshift`
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

`BitRshift`

## Module

Foundation
