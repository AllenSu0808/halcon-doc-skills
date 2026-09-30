# invert_image (Operator)

## Name

`invert_image` — Invert an image.

## Signature

`def invert_image(image: HObject) -> HObject`

## Description

The operator `invert_image` inverts the gray values of an image.
For images of the `byte` and `cyclic` type the result is
calculated
as:
g' = 255 - g
Images of the 'direction' type are transformed by
g' = (g + 90) modulo 180
In the case of signed types the values are negated. The resulting
image has the same pixel type as the input image.

Several images can be processed in one call.
An output image is generated for every input image.

`invert_image` can be executed on an OpenCL device for `byte`,
`direction`, `cyclic`, `int1`, `int2`,
`uint2`, `int4`, and `real` images.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte* / direction* / cyclic* / int1* / int2* / uint2* / int4* / int8 / real*) **allowed for compute devices*

Input image(s).

**`image_invert`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Image(s) with inverted gray values.

## Possible Successors

`watersheds`

## Alternatives

`scale_image`

## See also

`scale_image`,
`add_image`,
`sub_image`

## Module

Foundation
