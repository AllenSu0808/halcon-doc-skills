# crop_domain (Operator)

## Name

`crop_domain` — Cut out of defined gray values.

## Signature

`def crop_domain(image: HObject) -> HObject`

## Description

The operator `crop_domain` cuts a rectangular area from the
input images.
This rectangle is the smallest surrounding rectangle of the
domain of the input image.
The new image matrix has the size of the rectangle.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte* / direction* / cyclic* / int1* / int2* / uint2* / int4* / int8 / real*) **allowed for compute devices*

Input image.

**`image_part`** (output_object)  (multichannel-)image(-array) `→` HObject (byte* / direction* / cyclic* / int1* / int2* / uint2* / int4* / int8 / real*) **allowed for compute devices*

Image area.

## Possible Successors

`disp_image`

## Alternatives

`crop_part`,
`crop_rectangle1`,
`change_format`,
`reduce_domain`

## See also

`zoom_image_size`,
`zoom_image_factor`

## Module

Foundation
