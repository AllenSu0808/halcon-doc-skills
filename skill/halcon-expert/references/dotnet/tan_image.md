# TanImage (Operator)

## Name

`TanImage` — Calculate the tangent of an image.

## Signature

`static void HOperatorSet.TanImage(HObject image, out HObject tanImage)`

`HImage HImage.TanImage()`

## Description

`TanImage` calculates the tangent of an input image
*`image`* and stores the result in the image *`tanImage`*
of type real. If *`image`* is of type direction or cyclic, the
angles in *`image`* are converted to radians internally. If
*`image`* is of type real, the angles in *`image`* are
assumed to be represented in radians. For direction images, the
value of 255 will result in a value of 0 in the output image.

## Attention

`TanImage` can be executed on OpenCL devices.

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

**`tanImage`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (real)

Output image.

## See also

`SinImage`,
`CosImage`,
`AsinImage`,
`AcosImage`,
`AtanImage`,
`Atan2Image`

## Module

Foundation
