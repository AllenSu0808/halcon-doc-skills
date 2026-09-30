# atan2_image (Operator)

## Name

`atan2_image` — Calculate the arctangent of two images.

## Signature

`atan2_image(ImageY, ImageX : ArctanImage : : )`

## Description

`atan2_image` calculates the arctangent
*`ImageY`*/*`ImageX`* of the input images
*`ImageY`* and *`ImageX`*, using the signs of the gray
values of the two images to determine the quadrant of the result,
and stores the result in the image *`ArctanImage`*. The angles
in *`ArctanImage`* are represented in radians.

## Attention

`atan2_image` can be executed on an OpenCL device for int1,
int2, int4, and real images. Note that the results of the OpenCL
code may vary from the results produced by the CPU.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`ImageY`** (input_object)  (multichannel-)image(-array) `→` object (int1* / int2* / int4* / int8 / real*) **allowed for compute devices*

Input image 1.

**`ImageX`** (input_object)  (multichannel-)image(-array) `→` object (int1 / int2 / int4 / int8 / real)

Input image 2.

**`ArctanImage`** (output_object)  (multichannel-)image(-array) `→` object (real)

Output image.

## Alternatives

`atan_image`

## See also

`acos_image`,
`asin_image`,
`tan_image`,
`sin_image`,
`cos_image`

## Module

Foundation
