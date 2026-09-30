# gray_closing_rect (Operator)

## Name

`gray_closing_rect` — Perform a gray value closing with a rectangular mask.

## Signature

`def gray_closing_rect(image: HObject, mask_height: int, mask_width: int) -> HObject`

## Description

`gray_closing_rect` applies a gray value closing to the input
image *`image`* with a rectangular mask of size
(*`mask_height`*, *`mask_width`*).
The resulting image is returned in *`image_closing`*. If the
parameters *`mask_height`* or *`mask_width`* are even,
they are changed to the next larger odd value. At the border of the
image the gray values are mirrored.

The gray value closing of an image i with a rectangular structuring
element s is defined as
$$i \circ s = \left(i \oplus s\right) \ominus s,$$ ![figure](../assets/661128449be14554.svg)
i.e., a dilation of the image with s followed by an erosion with
s (see [`gray_dilation_rect`](gray_dilation_rect.md) and [`gray_erosion_rect`](gray_erosion_rect.md)).

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

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / uint2 / int2 / int4 / real)

Input image.

**`image_closing`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / uint2 / int2 / int4 / real)

Gray-closed image.

**`mask_height`** (input_control)  extent.y `→` int

Height of the filter mask.

Default:
11

Suggested values:
3, 5, 7, 9, 11, 13, 15

Value range:
`3
≤
mask_height
≤
511`

Minimum increment:
2

Recommended increment:
2

Restriction:
`odd(MaskHeight) && MaskHeight < height(Image) * 2`

**`mask_width`** (input_control)  extent.x `→` int

Width of the filter mask.

Default:
11

Suggested values:
3, 5, 7, 9, 11, 13, 15

Value range:
`3
≤
mask_width
≤
511`

Minimum increment:
2

Recommended increment:
2

Restriction:
`odd(MaskWidth) && MaskWidth < width(Image) * 2`

## Result

`gray_closing_rect` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Alternatives

`gray_closing`,
`gray_closing_shape`

## See also

`closing_rectangle1`,
`gray_dilation_rect`,
`gray_erosion_rect`

## Module

Foundation
