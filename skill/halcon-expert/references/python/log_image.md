# log_image (Operator)

## Name

`log_image` — Calculate the logarithm of an image.

## Signature

`def log_image(image: HObject, base: Union[int, float, str]) -> HObject`

## Description

`log_image` calculates the logarithm to the base *`base`*
of an input image *`image`* and stores the result in the image
*`log_image`*. If *`image`* contains gray values outside
the valid domain of the logarithm function, i.e., $\le0$,
the corresponding gray values in *`log_image`* are set to 0.

## Attention

`log_image` can be executed on an OpenCL device for byte,
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

**`log_image`** (output_object)  (multichannel-)image(-array) `→` HObject (real)

Output image.

**`base`** (input_control)  number `→` Union[int, float, str]

Base of the logarithm.

Default:
"e"

Suggested values:
"e", 2, 10

## See also

`pow_image`,
`exp_image`

## Module

Foundation
