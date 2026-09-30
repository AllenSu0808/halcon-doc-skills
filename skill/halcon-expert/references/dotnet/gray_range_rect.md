# GrayRangeRect (Operator)

## Name

`GrayRangeRect` — Determine the gray value range within a rectangle.

## Signature

`static void HOperatorSet.GrayRangeRect(HObject image, out HObject imageResult, HTuple maskHeight, HTuple maskWidth)`

`HImage HImage.GrayRangeRect(int maskHeight, int maskWidth)`

## Description

`GrayRangeRect` calculates the gray value range, i.e., the
difference (max - min) of the maximum and
minimum gray values, of the input image *`image`* within a
rectangular mask of size (*`maskHeight`*,
*`maskWidth`*) for each image point. The resulting image is
returned in *`imageResult`*. If the parameters
*`maskHeight`* or *`maskWidth`* are even, they are
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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / cyclic / uint2 / int2 / int4 / real)

Image for which the gray value range is to
be calculated.

**`imageResult`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / cyclic / uint2 / int2 / int4 / real)

Image containing the gray value range.

**`maskHeight`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the filter mask.

Default:
11

Suggested values:
3, 5, 7, 9, 11, 13, 15

Value range:
`3
≤
maskHeight
≤
511` (lin)

Minimum increment:
2

Recommended increment:
2

Restriction:
`odd(MaskHeight) && MaskHeight < height(Image) * 2`

**`maskWidth`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the filter mask.

Default:
11

Suggested values:
3, 5, 7, 9, 11, 13, 15

Value range:
`3
≤
maskWidth
≤
511` (lin)

Minimum increment:
2

Recommended increment:
2

Restriction:
`odd(MaskWidth) && MaskWidth < width(Image) * 2`

## Result

`GrayRangeRect` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Alternatives

`GrayDilationRect`,
`GrayErosionRect`,
`SubImage`

## Module

Foundation
