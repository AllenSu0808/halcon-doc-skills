# cos_image (Operator)

## Name

`cos_image` — Calculate the cosine of an image.

## Signature

`def cos_image(image: HObject) -> HObject`

## Description

`cos_image` calculates the cosine of an input image
*`image`* and stores the result in the image *`cos_image`*
of type real. If *`image`* is of type direction or cyclic, the
angles in *`image`* are converted to radians internally. If
*`image`* is of type real, the angles in *`image`* are
assumed to be represented in radians. For direction images, the
value of 255 will result in a value of 0 in the output image.

## Attention

`cos_image` can be executed on OpenCL devices.

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

**`cos_image`** (output_object)  (multichannel-)image(-array) `→` HObject (real)

Output image.

## See also

`sin_image`,
`tan_image`,
`asin_image`,
`acos_image`,
`atan_image`,
`atan2_image`

## Module

Foundation
