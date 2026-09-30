# BitNot (Operator)

## Name

`BitNot` — Complement all bits of the pixels.

## Signature

`static void HOperatorSet.BitNot(HObject image, out HObject imageNot)`

`HImage HImage.BitNot()`

## Description

The operator `BitNot` calculates the “complement”
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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4)

Input image(s).

**`imageNot`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4)

Result image(s) by complement operation.

## Example (HDevelop)

```
read_image(Image,'monkey')
dev_display(Image)
bit_not(Image,ImageBitNot)
dev_display(ImageBitNot)
```

## Result

If the images are correct (type) the operator `BitNot`
returns the value 2 (
H_MSG_TRUE)
.
The behavior in case of empty input (no input images available) is
set via the operator
`set_system(::'no_object_result',<Result>:)`
If necessary an exception is raised.

## Alternatives

`BitOr`,
`BitAnd`,
`AddImage`

## See also

`BitSlice`,
`BitMask`

## Module

Foundation
