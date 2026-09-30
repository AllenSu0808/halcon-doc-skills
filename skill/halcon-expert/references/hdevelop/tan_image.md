# tan_image (Operator)

## Name

`tan_image` — Calculate the tangent of an image.

## Signature

`tan_image(Image : TanImage : : )`

## Description

`tan_image` calculates the tangent of an input image
*`Image`* and stores the result in the image *`TanImage`*
of type real. If *`Image`* is of type direction or cyclic, the
angles in *`Image`* are converted to radians internally. If
*`Image`* is of type real, the angles in *`Image`* are
assumed to be represented in radians. For direction images, the
value of 255 will result in a value of 0 in the output image.

## Attention

`tan_image` can be executed on OpenCL devices.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (direction* / cyclic* / real*) **allowed for compute devices*

Input image.

**`TanImage`** (output_object)  (multichannel-)image(-array) `→` object (real)

Output image.

## See also

`sin_image`,
`cos_image`,
`asin_image`,
`acos_image`,
`atan_image`,
`atan2_image`

## Module

Foundation
