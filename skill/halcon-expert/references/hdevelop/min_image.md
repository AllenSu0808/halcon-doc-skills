# min_image (Operator)

## Name

`min_image` — Calculate the minimum of two images pixel by pixel.

## Signature

`min_image(Image1, Image2 : ImageMin : : )`

## Description

The operator `min_image` determines the minimum (pixel by
pixel) of the images *`Image1`* and *`Image2`*. The
result is stored in the image *`ImageMin`*. The resulting
image has the same pixel type as the input image. If several (pairs
of) images are processed in one call, every i-th image from
*`Image1`* is compared to the i-th image from
*`Image2`*. Thus the number of images in both input
parameters must be the same. An output image is generated for every
input pair.

`min_image` can be executed on an OpenCL device for byte, int1, int2,
uint2, int4, real, direction, and cyclic images.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`Image1`** (input_object)  (multichannel-)image(-array) `→` object (byte* / int1* / int2* / uint2* / int4* / int8 / real* / direction* / cyclic*) **allowed for compute devices*

Image(s) 1.

**`Image2`** (input_object)  (multichannel-)image(-array) `→` object (byte* / int1* / int2* / uint2* / int4* / int8 / real* / direction* / cyclic*) **allowed for compute devices*

Image(s) 2.

**`ImageMin`** (output_object)  (multichannel-)image(-array) `→` object (byte / int1 / int2 / uint2 / int4 / int8 / real / direction / cyclic)

Result image(s) by the minimization.

## Result

If the parameter values are correct the operator `min_image`
returns the value 2 (
H_MSG_TRUE)
. The behavior in case of empty input (no
input images available) is set via the operator
`set_system(::'no_object_result',<Result>:)`
If necessary an exception is raised.

## Alternatives

`gray_erosion`

## See also

`max_image`

## Module

Foundation
