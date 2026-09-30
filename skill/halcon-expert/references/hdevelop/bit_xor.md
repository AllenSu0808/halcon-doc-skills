# bit_xor (Operator)

## Name

`bit_xor` — Bit-by-bit XOR of all pixels of the input images.

## Signature

`bit_xor(Image1, Image2 : ImageXor : : )`

## Description

The operator `bit_xor` calculates the “xor”
of all pixels of the input images bit by bit.
The semantics of the “xor” operation corresponds to that of C for the
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

**`Image1`** (input_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4)

Input image(s) 1.

**`Image2`** (input_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4)

Input image(s) 2.

**`ImageXor`** (output_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4)

Result image(s) by XOR-operation.

## Example (HDevelop)

```
read_image(Image1,'fabrik')
dev_display (Image1)
read_image(Image2,'monkey')
dev_display (Image2)
bit_xor(Image1,Image2,ImageBitXor)
dev_display (ImageBitXor)
```

## Result

If the parameter values are correct the operator `bit_xor`
returns the value 2 (
H_MSG_TRUE)
.
The behavior in case of empty input (no input images available) can be
determined by the operator
`set_system(::'no_object_result',<Result>:)`
If necessary an exception is raised.

## Alternatives

`bit_or`,
`bit_and`,
`add_image`

## See also

`bit_or`,
`bit_and`

## Module

Foundation
