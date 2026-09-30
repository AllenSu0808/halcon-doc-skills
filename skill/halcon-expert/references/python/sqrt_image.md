# sqrt_image (Operator)

## Name

`sqrt_image` — Calculate the square root of an image.

## Signature

`def sqrt_image(image: HObject) -> HObject`

## Description

`sqrt_image` calculates the square root of an input image
*`image`* and stores the result in the image *`sqrt_image`*
of the same pixel type. In case the picture *`image`* is of a
signed pixel type, negative pixel values will be mapped to zero in
*`sqrt_image`*.

`sqrt_image` can be executed on an OpenCL device for byte, int1, int2,
uint2, int4, and real images.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte* / int1* / int2* / uint2* / int4* / int8 / real*) **allowed for compute devices*

Input image

**`sqrt_image`** (output_object)  (multichannel-)image(-array) `→` HObject (byte* / int1* / int2* / uint2* / int4* / int8 / real*) **allowed for compute devices*

Output image

## See also

`pow_image`

## Module

Foundation
