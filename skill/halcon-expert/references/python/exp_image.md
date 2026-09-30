# exp_image (Operator)

## Name

`exp_image` — Calculate the exponentiation of an image.

## Signature

`def exp_image(image: HObject, base: Union[int, float, str]) -> HObject`

## Description

`exp_image` calculates the exponentiation to the base
*`base`* of an input image *`image`* and stores the result
in the image *`exp_image`*. If *`image`* contains gray
values that would overflow the range of *`exp_image`*, e.g., >
88.722839 for *`base`* = *"e"*, the corresponding
gray values in *`exp_image`* are set to the largest value
representable in *`exp_image`* (i.e., $3.4028235\times10^{38}$).

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

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte* / int1* / uint2* / int2* / int4* / int8 / real*) **allowed for compute devices*

Input image.

**`exp_image`** (output_object)  (multichannel-)image(-array) `→` HObject (real)

Output image.

**`base`** (input_control)  number `→` Union[int, float, str]

Base of the exponentiation.

Default:
"e"

Suggested values:
"e", 2, 10

## See also

`pow_image`,
`log_image`

## Module

Foundation
