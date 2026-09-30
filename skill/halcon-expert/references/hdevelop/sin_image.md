# sin_image (Operator)

## Name

`sin_image` — Calculate the sine of an image.

## Signature

`sin_image(Image : SinImage : : )`

## Description

`sin_image` calculates the sine of an input image
*`Image`* and stores the result in the image *`SinImage`*
of type real. If *`Image`* is of type direction or cyclic, the
angles in *`Image`* are converted to radians internally. If
*`Image`* is of type real, the angles in *`Image`* are
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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (direction* / cyclic* / real*) **allowed for compute devices*

Input image.

**`SinImage`** (output_object)  (multichannel-)image(-array) `→` object (real)

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
