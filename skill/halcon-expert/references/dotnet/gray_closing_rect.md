# GrayClosingRect (Operator)

## Name

`GrayClosingRect` — Perform a gray value closing with a rectangular mask.

## Signature

`static void HOperatorSet.GrayClosingRect(HObject image, out HObject imageClosing, HTuple maskHeight, HTuple maskWidth)`

`HImage HImage.GrayClosingRect(int maskHeight, int maskWidth)`

## Description

`GrayClosingRect` applies a gray value closing to the input
image *`image`* with a rectangular mask of size
(*`maskHeight`*, *`maskWidth`*).
The resulting image is returned in *`imageClosing`*. If the
parameters *`maskHeight`* or *`maskWidth`* are even,
they are changed to the next larger odd value. At the border of the
image the gray values are mirrored.

The gray value closing of an image i with a rectangular structuring
element s is defined as
$$i \circ s = \left(i \oplus s\right) \ominus s,$$ ![figure](../assets/661128449be14554.svg)
i.e., a dilation of the image with s followed by an erosion with
s (see [`GrayDilationRect`](gray_dilation_rect.md) and [`GrayErosionRect`](gray_erosion_rect.md)).

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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / uint2 / int2 / int4 / real)

Input image.

**`imageClosing`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / uint2 / int2 / int4 / real)

Gray-closed image.

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
511`

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
511`

Minimum increment:
2

Recommended increment:
2

Restriction:
`odd(MaskWidth) && MaskWidth < width(Image) * 2`

## Result

`GrayClosingRect` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Alternatives

`GrayClosing`,
`GrayClosingShape`

## See also

`ClosingRectangle1`,
`GrayDilationRect`,
`GrayErosionRect`

## Module

Foundation
