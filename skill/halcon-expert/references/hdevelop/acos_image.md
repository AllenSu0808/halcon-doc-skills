# acos_image (Operator)

## Name

`acos_image` — Calculate the arccosine of an image.

## Signature

`acos_image(Image : ArccosImage : : )`

## Description

`acos_image` calculates the arccosine of an input image
*`Image`* and stores the result in the image
*`ArccosImage`*. The angles in *`ArccosImage`* are
represented in radians. If *`Image`* contains gray values
outside the valid domain [-1,1] of the arccosine function, the
corresponding gray values in *`ArccosImage`* are set to 0.

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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (real*) **allowed for compute devices*

Input image.

**`ArccosImage`** (output_object)  (multichannel-)image(-array) `→` object (real)

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
