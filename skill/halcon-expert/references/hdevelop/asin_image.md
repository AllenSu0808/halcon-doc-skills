# asin_image (Operator)

## Name

`asin_image` — Calculate the arcsine of an image.

## Signature

`asin_image(Image : ArcsinImage : : )`

## Description

`asin_image` calculates the arcsine of an input image
*`Image`* and stores the result in the image
*`ArcsinImage`*. The angles in *`ArcsinImage`* are
represented in radians. If *`Image`* contains gray values
outside the valid domain [-1,1] of the arcsine function, the
corresponding gray values in *`ArcsinImage`* are set to 0.

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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (real*) **allowed for compute devices*

Input image.

**`ArcsinImage`** (output_object)  (multichannel-)image(-array) `→` object (real)

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
