# gray_opening_rect (Operator)

## Name

`gray_opening_rect` — Perform a gray value opening with a rectangular mask.

## Signature

`gray_opening_rect(Image : ImageOpening : MaskHeight, MaskWidth : )`

## Description

`gray_opening_rect` applies a gray value opening to the input
image *`Image`* with a rectangular mask of size
(*`MaskHeight`*, *`MaskWidth`*).
The resulting image is returned in *`ImageOpening`*. If the
parameters *`MaskHeight`* or *`MaskWidth`* are even,
they are changed to the next larger odd value. At the border of the
image the gray values are mirrored.

The gray value opening of an image i with a rectangular structuring
element s is defined as
$$i \circ s = (i \ominus s) \oplus s$$ ![figure](../assets/cb97c07392535186.svg)
i.e., an erosion of the image with s followed by a dilation with
s (see [`gray_erosion_rect`](gray_erosion_rect.md) and [`gray_dilation_rect`](gray_dilation_rect.md)).

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

Input image.

**`ImageOpening`** (output_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / uint2 / int2 / int4 / real)

Gray-opened image.

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
511`

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
511`

Minimum increment:
2

Recommended increment:
2

Restriction:
`odd(MaskWidth) && MaskWidth < width(Image) * 2`

## Result

`gray_opening_rect` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Alternatives

`gray_opening`,
`gray_opening_shape`

## See also

`opening_rectangle1`,
`gray_dilation_rect`,
`gray_erosion_rect`

## Module

Foundation
