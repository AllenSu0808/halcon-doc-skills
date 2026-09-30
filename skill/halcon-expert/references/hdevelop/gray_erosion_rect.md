# gray_erosion_rect (Operator)

## Name

`gray_erosion_rect` — Determine the minimum gray value within a rectangle.

## Signature

`gray_erosion_rect(Image : ImageMin : MaskHeight, MaskWidth : )`

## Description

`gray_erosion_rect` calculates the minimum gray value of the input
image *`Image`* within a rectangular mask of size
(*`MaskHeight`*, *`MaskWidth`*) for each image point.
The resulting image is returned in *`ImageMin`*. If the
parameters *`MaskHeight`* or *`MaskWidth`* are even,
they are changed to the next larger odd value. At the border of the
image the gray values are mirrored.

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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / uint2 / int2 / int4 / real)

Image for which the minimum gray values are to
be calculated.

**`ImageMin`** (output_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / uint2 / int2 / int4 / real)

Image containing the minimum gray values.

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

`gray_erosion_rect` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## See also

`gray_dilation_rect`

## Module

Foundation
