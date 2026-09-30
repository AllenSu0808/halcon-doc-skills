# atan_image (Operator)

## Name

`atan_image` — Calculate the arctangent of an image.

## Signature

`def atan_image(image: HObject) -> HObject`

## Description

`atan_image` calculates the arctangent of an input image
*`image`* and stores the result in the image
*`arctan_image`*. The angles in *`arctan_image`* are
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

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (real*) **allowed for compute devices*

Input image.

**`arctan_image`** (output_object)  (multichannel-)image(-array) `→` HObject (real)

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
