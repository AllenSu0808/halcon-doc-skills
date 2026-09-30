# GrayOpeningRect (Operator)

## Name

`GrayOpeningRect` — Perform a gray value opening with a rectangular mask.

## Signature

`static void HOperatorSet.GrayOpeningRect(HObject image, out HObject imageOpening, HTuple maskHeight, HTuple maskWidth)`

`HImage HImage.GrayOpeningRect(int maskHeight, int maskWidth)`

## Description

`GrayOpeningRect` applies a gray value opening to the input
image *`image`* with a rectangular mask of size
(*`maskHeight`*, *`maskWidth`*).
The resulting image is returned in *`imageOpening`*. If the
parameters *`maskHeight`* or *`maskWidth`* are even,
they are changed to the next larger odd value. At the border of the
image the gray values are mirrored.

The gray value opening of an image i with a rectangular structuring
element s is defined as
$$i \circ s = (i \ominus s) \oplus s$$ ![figure](../assets/cb97c07392535186.svg)
i.e., an erosion of the image with s followed by a dilation with
s (see [`GrayErosionRect`](gray_erosion_rect.md) and [`GrayDilationRect`](gray_dilation_rect.md)).

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

**`imageOpening`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / uint2 / int2 / int4 / real)

Gray-opened image.

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

`GrayOpeningRect` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Alternatives

`GrayOpening`,
`GrayOpeningShape`

## See also

`OpeningRectangle1`,
`GrayDilationRect`,
`GrayErosionRect`

## Module

Foundation
