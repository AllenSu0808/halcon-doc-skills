# LogImage (Operator)

## Name

`LogImage` — Calculate the logarithm of an image.

## Signature

`static void HOperatorSet.LogImage(HObject image, out HObject logImage, HTuple baseVal)`

`HImage HImage.LogImage(HTuple baseVal)`

`HImage HImage.LogImage(string baseVal)`

## Description

`LogImage` calculates the logarithm to the base *`baseVal`*
of an input image *`image`* and stores the result in the image
*`logImage`*. If *`image`* contains gray values outside
the valid domain of the logarithm function, i.e., $\le0$,
the corresponding gray values in *`logImage`* are set to 0.

## Attention

`LogImage` can be executed on an OpenCL device for byte,
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

**`logImage`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (real)

Output image.

**`baseVal`** (input_control)  number `→` [HTuple](HTuple.md) (*string* / int / long / double)

Base of the logarithm.

Default:
"e"

Suggested values:
"e", 2, 10

## See also

`PowImage`,
`ExpImage`

## Module

Foundation
