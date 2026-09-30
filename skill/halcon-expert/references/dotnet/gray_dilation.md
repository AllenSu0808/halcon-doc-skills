# GrayDilation (Operator)

## Name

`GrayDilation` — Perform a gray value dilation on an image.

## Signature

`static void HOperatorSet.GrayDilation(HObject image, HObject SE, out HObject imageDilation)`

`HImage HImage.GrayDilation(HImage SE)`

## Description

`GrayDilation` applies a gray value dilation to the input
image *`image`* with the structuring element *`SE`*. The
image type of the structuring element *`SE`* must match the
image type of the input image *`image`*. The gray value
dilation of an image i with a structuring element s at the pixel
position x is defined as:
$$(i \oplus s)(x) = \max\{f(x - z) + s(z) \mid z \in S\}$$ ![figure](../assets/d6d5dbca93d6726b.svg)
Here, S is the domain of the structuring element s (see
[`ReadGraySe`](read_gray_se.md)).

The gray value dilation is particularly fast for flat structuring
elements, i.e., structuring elements with a constant gray level
within their domain.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Input image.

**`SE`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2 / real)

Structuring element.

**`imageDilation`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Gray-dilated image.

## Result

`GrayDilation` returns 2 (
H_MSG_TRUE)
if the structuring element is not
the empty region. Otherwise, an exception is raised.

## Possible Predecessors

`ReadGraySe`,
`GenDiscSe`,
`ReadImage`

## Possible Successors

`SubImage`,
`GrayErosion`

## Alternatives

`GrayDilationRect`,
`GrayDilationShape`

## See also

`GrayOpening`,
`GrayClosing`,
`Dilation1`,
`GraySkeleton`

## Module

Foundation
