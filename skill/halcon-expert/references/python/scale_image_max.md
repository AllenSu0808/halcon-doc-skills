# scale_image_max (Operator)

## Name

`scale_image_max` — Maximum gray value spreading in the value range
*0* to *255*.

## Signature

`def scale_image_max(image: HObject) -> HObject`

## Description

The operator `scale_image_max` calculates the minimum and
maximum and scales the image to the maximum value range of a byte image.
This way the dynamics (value range) is fully exploited.
The number of different gray scales does not change,
but in general the visual impression is enhanced.
The gray values of images of the *"real"*, *"int2"*,
*"uint2"*, *"int4"*, and *"int8"* type
are scaled to the range *0* to *255*
and returned as *"byte"* images.

## Attention

The output always is an image of the type *"byte"*.

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / int2 / uint2 / int4 / int8 / real)

Image to be scaled.

**`image_scale_max`** (output_object)  image(-array) `→` HObject (byte)

contrast enhanced image.

## Possible Successors

`disp_image`

## Alternatives

`equ_histo_image`,
`equ_histo_image_rect`,
`scale_image`,
`illuminate`,
`convert_image_type`

## See also

`min_max_gray`,
`gray_histo`

## Module

Foundation
