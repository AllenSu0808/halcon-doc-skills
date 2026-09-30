# BitMask (Operator)

## Name

`BitMask` — Logical “AND” of each pixel using a bit mask.

## Signature

`static void HOperatorSet.BitMask(HObject image, out HObject imageMask, HTuple bitMask)`

`HImage HImage.BitMask(int bitMask)`

## Description

The operator `BitMask` carries out an “and” operation
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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4)

Input image(s).

**`imageMask`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4)

Result image(s) by combination with mask.

**`bitMask`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Bit field

Default:
128

Suggested values:
1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096

## Result

If the images are correct (type) the operator `BitMask`
returns the value 2 (
H_MSG_TRUE)
.
The behavior in case of empty input (no input images available) is
set via the operator
`set_system(::'no_object_result',<Result>:)`
If necessary an exception is raised.

## Possible Successors

`Threshold`,
`BitOr`

## Alternatives

`BitSlice`

## See also

`BitAnd`,
`BitLshift`

## Module

Foundation
