# acos_image (Operator)

## Name

`acos_image` — Calculate the arccosine of an image.

## Signature

`def acos_image(image: HObject) -> HObject`

## Description

`acos_image` calculates the arccosine of an input image
*`image`* and stores the result in the image
*`arccos_image`*. The angles in *`arccos_image`* are
represented in radians. If *`image`* contains gray values
outside the valid domain [-1,1] of the arccosine function, the
corresponding gray values in *`arccos_image`* are set to 0.

## Attention

`acos_image` can be executed on OpenCL devices.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (real*) **allowed for compute devices*

Input image.

**`arccos_image`** (output_object)  (multichannel-)image(-array) `→` HObject (real)

Output image.

## See also

`asin_image`,
`atan_image`,
`atan2_image`,
`tan_image`,
`sin_image`,
`cos_image`

## Module

Foundation
