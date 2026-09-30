# sin_image (Operator)

## Name

`sin_image` — Calculate the sine of an image.

## Signature

`def sin_image(image: HObject) -> HObject`

## Description

`sin_image` calculates the sine of an input image
*`image`* and stores the result in the image *`sin_image`*
of type real. If *`image`* is of type direction or cyclic, the
angles in *`image`* are converted to radians internally. If
*`image`* is of type real, the angles in *`image`* are
assumed to be represented in radians. For direction images, the
value of 255 will result in a value of 0 in the output image.

## Attention

`sin_image` can be executed on OpenCL devices.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (direction* / cyclic* / real*) **allowed for compute devices*

Input image.

**`sin_image`** (output_object)  (multichannel-)image(-array) `→` HObject (real)

Output image.

## See also

`cos_image`,
`tan_image`,
`asin_image`,
`acos_image`,
`atan_image`,
`atan2_image`

## Module

Foundation
