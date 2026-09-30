# ExpImage (Operator)

## Name

`ExpImage` — Calculate the exponentiation of an image.

## Signature

`static void HOperatorSet.ExpImage(HObject image, out HObject expImage, HTuple baseVal)`

`HImage HImage.ExpImage(HTuple baseVal)`

`HImage HImage.ExpImage(string baseVal)`

## Description

`ExpImage` calculates the exponentiation to the base
*`baseVal`* of an input image *`image`* and stores the result
in the image *`expImage`*. If *`image`* contains gray
values that would overflow the range of *`expImage`*, e.g., >
88.722839 for *`baseVal`* = *"e"*, the corresponding
gray values in *`expImage`* are set to the largest value
representable in *`expImage`* (i.e., $3.4028235\times10^{38}$).

## Attention

`ExpImage` can be executed on an OpenCL device for byte,
int1, int2, uint2, int4, and real images. Note that the results of
the OpenCL code may vary from the results produced by the CPU.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / int1* / uint2* / int2* / int4* / int8 / real*) **allowed for compute devices*

Input image.

**`expImage`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (real)

Output image.

**`baseVal`** (input_control)  number `→` [HTuple](HTuple.md) (*string* / int / long / double)

Base of the exponentiation.

Default:
"e"

Suggested values:
"e", 2, 10

## See also

`PowImage`,
`LogImage`

## Module

Foundation
