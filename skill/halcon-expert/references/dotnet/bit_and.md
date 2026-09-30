# BitAnd (Operator)

## Name

`BitAnd` — Bit-by-bit AND of all pixels of the input images.

## Signature

`static void HOperatorSet.BitAnd(HObject image1, HObject image2, out HObject imageAnd)`

`HImage HImage.BitAnd(HImage image2)`

## Description

The operator `BitAnd` calculates the “and”
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

**`image1`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4)

Input image(s) 1.

**`image2`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4)

Input image(s) 2.

**`imageAnd`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4)

Result image(s) by AND-operation.

## Example (HDevelop)

```
read_image(Image1,'fabrik')
dev_display (Image1)
read_image(Image2,'monkey')
dev_display (Image2)
bit_and(Image1,Image2,ImageBitAnd)
dev_display (ImageBitAnd)
```

## Result

If the images are correct (type and number) the operator `BitAnd`
returns the value 2 (
H_MSG_TRUE)
.
The behavior in case of empty input (no input images available) is
set via the operator
`set_system(::'no_object_result',<Result>:)`
If necessary an exception is raised.

## Alternatives

`BitMask`,
`AddImage`,
`MaxImage`

## See also

`BitMask`,
`AddImage`,
`MaxImage`

## Module

Foundation
