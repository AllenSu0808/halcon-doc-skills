# CosImage (Operator)

## Name

`CosImage` — Calculate the cosine of an image.

## Signature

`static void HOperatorSet.CosImage(HObject image, out HObject cosImage)`

`HImage HImage.CosImage()`

## Description

`CosImage` calculates the cosine of an input image
*`image`* and stores the result in the image *`cosImage`*
of type real. If *`image`* is of type direction or cyclic, the
angles in *`image`* are converted to radians internally. If
*`image`* is of type real, the angles in *`image`* are
assumed to be represented in radians. For direction images, the
value of 255 will result in a value of 0 in the output image.

## Attention

`CosImage` can be executed on OpenCL devices.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (direction* / cyclic* / real*) **allowed for compute devices*

Input image.

**`cosImage`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (real)

Output image.

## See also

`SinImage`,
`TanImage`,
`AsinImage`,
`AcosImage`,
`AtanImage`,
`Atan2Image`

## Module

Foundation
