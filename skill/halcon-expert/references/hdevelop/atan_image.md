# atan_image (Operator)

## Name

`atan_image` — Calculate the arctangent of an image.

## Signature

`atan_image(Image : ArctanImage : : )`

## Description

`atan_image` calculates the arctangent of an input image
*`Image`* and stores the result in the image
*`ArctanImage`*. The angles in *`ArctanImage`* are
represented in radians.

## Attention

`atan_image` can be executed on OpenCL devices.

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

**`ArctanImage`** (output_object)  (multichannel-)image(-array) `→` object (real)

Output image.

## Alternatives

`atan2_image`

## See also

`acos_image`,
`asin_image`,
`tan_image`,
`sin_image`,
`cos_image`

## Module

Foundation
