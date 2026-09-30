# pow_image (Operator)

## Name

`pow_image` — Raise an image to a power.

## Signature

`def pow_image(image: HObject, exponent: Union[int, float]) -> HObject`

## Description

`pow_image` raises the gray values of the input image
*`image`* to the power *`exponent`* and stores the result
in the image *`pow_image`*. If *`image`* contains gray
values that would overflow the range of *`pow_image`*, e.g., >
7131.55017 for *`exponent`* = *10*, the corresponding
gray values in *`pow_image`* are set to the largest value
representable in *`pow_image`* (i.e., $3.4028235\times10^{38}$). If *`image`* contains gray
values that cannot be raised to the power *`exponent`*, i.e.,
if the gray values are negative and *`exponent`* is not an
integer, the corresponding gray values in *`pow_image`* are set
to 0.

## Attention

`pow_image` can be executed on an OpenCL device for byte,
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

**`pow_image`** (output_object)  (multichannel-)image(-array) `→` HObject (real)

Output image.

**`exponent`** (input_control)  number `→` Union[int, float]

Power to which the gray values are raised.

Default:
2

Suggested values:
0.25, 0.5, 2, 3, 4

## Alternatives

`gamma_image`

## See also

`sqrt_image`,
`exp_image`,
`log_image`

## Module

Foundation
