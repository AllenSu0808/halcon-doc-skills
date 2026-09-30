# CropDomain (Operator)

## Name

`CropDomain` — Cut out of defined gray values.

## Signature

`static void HOperatorSet.CropDomain(HObject image, out HObject imagePart)`

`HImage HImage.CropDomain()`

## Description

The operator `CropDomain` cuts a rectangular area from the
input images.
This rectangle is the smallest surrounding rectangle of the
domain of the input image.
The new image matrix has the size of the rectangle.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / direction* / cyclic* / int1* / int2* / uint2* / int4* / int8 / real*) **allowed for compute devices*

Input image.

**`imagePart`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / direction* / cyclic* / int1* / int2* / uint2* / int4* / int8 / real*) **allowed for compute devices*

Image area.

## Possible Successors

`DispImage`

## Alternatives

`CropPart`,
`CropRectangle1`,
`ChangeFormat`,
`ReduceDomain`

## See also

`ZoomImageSize`,
`ZoomImageFactor`

## Module

Foundation
