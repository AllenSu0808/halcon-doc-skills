# asin_image (Operator)

## Name

`asin_image` — Calculate the arcsine of an image.

## Signature

`def asin_image(image: HObject) -> HObject`

## Description

`asin_image` calculates the arcsine of an input image
*`image`* and stores the result in the image
*`arcsin_image`*. The angles in *`arcsin_image`* are
represented in radians. If *`image`* contains gray values
outside the valid domain [-1,1] of the arcsine function, the
corresponding gray values in *`arcsin_image`* are set to 0.

## Attention

`asin_image` can be executed on OpenCL devices.

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

**`arcsin_image`** (output_object)  (multichannel-)image(-array) `→` HObject (real)

Output image.

## See also

`acos_image`,
`atan_image`,
`atan2_image`,
`tan_image`,
`sin_image`,
`cos_image`

## Module

Foundation
