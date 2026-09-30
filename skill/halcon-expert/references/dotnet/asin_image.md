# AsinImage (Operator)

## Name

`AsinImage` — Calculate the arcsine of an image.

## Signature

`static void HOperatorSet.AsinImage(HObject image, out HObject arcsinImage)`

`HImage HImage.AsinImage()`

## Description

`AsinImage` calculates the arcsine of an input image
*`image`* and stores the result in the image
*`arcsinImage`*. The angles in *`arcsinImage`* are
represented in radians. If *`image`* contains gray values
outside the valid domain [-1,1] of the arcsine function, the
corresponding gray values in *`arcsinImage`* are set to 0.

## Attention

`AsinImage` can be executed on OpenCL devices.

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

**`arcsinImage`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (real)

Output image.

## See also

`AcosImage`,
`AtanImage`,
`Atan2Image`,
`TanImage`,
`SinImage`,
`CosImage`

## Module

Foundation
