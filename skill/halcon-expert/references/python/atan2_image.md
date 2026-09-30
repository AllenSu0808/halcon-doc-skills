# atan2_image (Operator)

## Name

`atan2_image` — Calculate the arctangent of two images.

## Signature

`def atan2_image(image_y: HObject, image_x: HObject) -> HObject`

## Description

`atan2_image` calculates the arctangent
*`image_y`*/*`image_x`* of the input images
*`image_y`* and *`image_x`*, using the signs of the gray
values of the two images to determine the quadrant of the result,
and stores the result in the image *`arctan_image`*. The angles
in *`arctan_image`* are represented in radians.

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

**`image_y`** (input_object)  (multichannel-)image(-array) `→` HObject (int1* / int2* / int4* / int8 / real*) **allowed for compute devices*

Input image 1.

**`image_x`** (input_object)  (multichannel-)image(-array) `→` HObject (int1 / int2 / int4 / int8 / real)

Input image 2.

**`arctan_image`** (output_object)  (multichannel-)image(-array) `→` HObject (real)

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
