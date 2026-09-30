# AtanImage (Operator)

## Name

`AtanImage` — Calculate the arctangent of an image.

## Signature

`static void HOperatorSet.AtanImage(HObject image, out HObject arctanImage)`

`HImage HImage.AtanImage()`

## Description

`AtanImage` calculates the arctangent of an input image
*`image`* and stores the result in the image
*`arctanImage`*. The angles in *`arctanImage`* are
represented in radians.

## Attention

`AtanImage` can be executed on OpenCL devices.

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

**`arctanImage`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (real)

Output image.

## Alternatives

`Atan2Image`

## See also

`AcosImage`,
`AsinImage`,
`TanImage`,
`SinImage`,
`CosImage`

## Module

Foundation
