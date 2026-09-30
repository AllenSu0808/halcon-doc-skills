# exp_image (Operator)

## Name

`exp_image` — Calculate the exponentiation of an image.

## Signature

`exp_image(Image : ExpImage : Base : )`

## Description

`exp_image` calculates the exponentiation to the base
*`Base`* of an input image *`Image`* and stores the result
in the image *`ExpImage`*. If *`Image`* contains gray
values that would overflow the range of *`ExpImage`*, e.g., >
88.722839 for *`Base`* = *'e'*, the corresponding
gray values in *`ExpImage`* are set to the largest value
representable in *`ExpImage`* (i.e., $3.4028235\times10^{38}$).

## Attention

`exp_image` can be executed on an OpenCL device for byte,
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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte* / int1* / uint2* / int2* / int4* / int8 / real*) **allowed for compute devices*

Input image.

**`ExpImage`** (output_object)  (multichannel-)image(-array) `→` object (real)

Output image.

**`Base`** (input_control)  number `→`  (string / integer / real)

Base of the exponentiation.

Default:
'e'

Suggested values:
'e', 2, 10

## See also

`pow_image`,
`log_image`

## Module

Foundation
