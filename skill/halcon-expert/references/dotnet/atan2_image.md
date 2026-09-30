# Atan2Image (Operator)

## Name

`Atan2Image` — Calculate the arctangent of two images.

## Signature

`static void HOperatorSet.Atan2Image(HObject imageY, HObject imageX, out HObject arctanImage)`

`HImage HImage.Atan2Image(HImage imageX)`

## Description

`Atan2Image` calculates the arctangent
*`imageY`*/*`imageX`* of the input images
*`imageY`* and *`imageX`*, using the signs of the gray
values of the two images to determine the quadrant of the result,
and stores the result in the image *`arctanImage`*. The angles
in *`arctanImage`* are represented in radians.

## Attention

`Atan2Image` can be executed on an OpenCL device for int1,
int2, int4, and real images. Note that the results of the OpenCL
code may vary from the results produced by the CPU.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`imageY`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (int1* / int2* / int4* / int8 / real*) **allowed for compute devices*

Input image 1.

**`imageX`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (int1 / int2 / int4 / int8 / real)

Input image 2.

**`arctanImage`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (real)

Output image.

## Alternatives

`AtanImage`

## See also

`AcosImage`,
`AsinImage`,
`TanImage`,
`SinImage`,
`CosImage`

## Module

Foundation
