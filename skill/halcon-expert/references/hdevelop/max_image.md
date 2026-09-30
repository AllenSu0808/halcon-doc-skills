# max_image (Operator)

## Name

`max_image` — Calculate the maximum of two images pixel by pixel.

## Signature

`max_image(Image1, Image2 : ImageMax : : )`

## Description

`max_image` calculates the maximum of the images
*`Image1`* and *`Image2`* (pixel by pixel). The
result is stored in the image *`ImageMax`*. The resulting
image has the same pixel type as the input image. If several (pairs
of) images are processed in one call, every i-th image from
*`Image1`* is compared to the i-th image from
*`Image2`*. Thus the number of images in both input
parameters must be the same. An output image is generated for every
input pair.

`max_image` can be executed on an OpenCL device for byte, int1, int2,
uint2, int4, real, direction, and cyclic images.

## Attention

The two input images must be of the same type and size.

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

**`ImageMax`** (output_object)  (multichannel-)image(-array) `→` object (byte / int1 / int2 / uint2 / int4 / int8 / real / direction / cyclic)

Result image(s) by the maximization.

## Example (HDevelop)

```
read_image(Image1,'monkey')
read_image(Image2,'fabrik')
max_image(Image1,Image2,Max)
dev_display (Max)
```

## Result

If the parameter values are correct the operator `max_image`
returns the value 2 (
H_MSG_TRUE)
. The behavior in case of empty input (no
input images available) is set via the operator
`set_system(::'no_object_result',<Result>:)`.
If necessary an exception is raised.

## See also

`min_image`

## Module

Foundation
