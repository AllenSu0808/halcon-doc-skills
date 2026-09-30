# PowImage (Operator)

## Name

`PowImage` — Raise an image to a power.

## Signature

`static void HOperatorSet.PowImage(HObject image, out HObject powImage, HTuple exponent)`

`HImage HImage.PowImage(HTuple exponent)`

`HImage HImage.PowImage(double exponent)`

## Description

`PowImage` raises the gray values of the input image
*`image`* to the power *`exponent`* and stores the result
in the image *`powImage`*. If *`image`* contains gray
values that would overflow the range of *`powImage`*, e.g., >
7131.55017 for *`exponent`* = *10*, the corresponding
gray values in *`powImage`* are set to the largest value
representable in *`powImage`* (i.e., $3.4028235\times10^{38}$). If *`image`* contains gray
values that cannot be raised to the power *`exponent`*, i.e.,
if the gray values are negative and *`exponent`* is not an
integer, the corresponding gray values in *`powImage`* are set
to 0.

## Attention

`PowImage` can be executed on an OpenCL device for byte,
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

**`powImage`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (real)

Output image.

**`exponent`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Power to which the gray values are raised.

Default:
2

Suggested values:
0.25, 0.5, 2, 3, 4

## Alternatives

`GammaImage`

## See also

`SqrtImage`,
`ExpImage`,
`LogImage`

## Module

Foundation
