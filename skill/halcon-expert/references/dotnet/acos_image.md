# AcosImage (Operator)

## Name

`AcosImage` — Calculate the arccosine of an image.

## Signature

`static void HOperatorSet.AcosImage(HObject image, out HObject arccosImage)`

`HImage HImage.AcosImage()`

## Description

`AcosImage` calculates the arccosine of an input image
*`image`* and stores the result in the image
*`arccosImage`*. The angles in *`arccosImage`* are
represented in radians. If *`image`* contains gray values
outside the valid domain [-1,1] of the arccosine function, the
corresponding gray values in *`arccosImage`* are set to 0.

## Attention

`AcosImage` can be executed on OpenCL devices.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (real*) **allowed for compute devices*

Input image.

**`arccosImage`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (real)

Output image.

## See also

`AsinImage`,
`AtanImage`,
`Atan2Image`,
`TanImage`,
`SinImage`,
`CosImage`

## Module

Foundation
