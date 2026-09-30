# gray_range_rect (Operator)

## Name

`gray_range_rect` — Determine the gray value range within a rectangle.

## Signature

`gray_range_rect(Image : ImageResult : MaskHeight, MaskWidth : )`

## Description

`gray_range_rect` calculates the gray value range, i.e., the
difference (max - min) of the maximum and
minimum gray values, of the input image *`Image`* within a
rectangular mask of size (*`MaskHeight`*,
*`MaskWidth`*) for each image point. The resulting image is
returned in *`ImageResult`*. If the parameters
*`MaskHeight`* or *`MaskWidth`* are even, they are
changed to the next smaller odd value. At the border of the image
the gray values are mirrored.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / cyclic / uint2 / int2 / int4 / real)

Image for which the gray value range is to
be calculated.

**`ImageResult`** (output_object)  (multichannel-)image(-array) `→` object (byte / cyclic / uint2 / int2 / int4 / real)

Image containing the gray value range.

**`MaskHeight`** (input_control)  extent.y `→`  (integer)

Height of the filter mask.

Default:
11

Suggested values:
3, 5, 7, 9, 11, 13, 15

Value range:
`3
≤
MaskHeight
≤
511` (lin)

Minimum increment:
2

Recommended increment:
2

Restriction:
`odd(MaskHeight) && MaskHeight < height(Image) * 2`

**`MaskWidth`** (input_control)  extent.x `→`  (integer)

Width of the filter mask.

Default:
11

Suggested values:
3, 5, 7, 9, 11, 13, 15

Value range:
`3
≤
MaskWidth
≤
511` (lin)

Minimum increment:
2

Recommended increment:
2

Restriction:
`odd(MaskWidth) && MaskWidth < width(Image) * 2`

## Result

`gray_range_rect` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Alternatives

`gray_dilation_rect`,
`gray_erosion_rect`,
`sub_image`

## Module

Foundation
