# GrayOpening (Operator)

## Name

`GrayOpening` — Perform a gray value opening on an image.

## Signature

`static void HOperatorSet.GrayOpening(HObject image, HObject SE, out HObject imageOpening)`

`HImage HImage.GrayOpening(HImage SE)`

## Description

`GrayOpening` applies a gray value opening to the input image
*`image`* with the structuring element *`SE`*. The image
type of the structuring element *`SE`* must match the image
type of the input image *`image`*. The gray value opening of
an image i with a structuring element s is defined as
$$i \odot s = (i \odot s) \oplus \tilde{s}$$ ![figure](../assets/4f0608759837c826.svg)
i.e., an erosion of the image with s followed by a dilation with
the transposed structuring element (see [`GrayErosion`](gray_erosion.md) and
[`GrayDilation`](gray_dilation.md)). For the generation of structuring elements,
see [`ReadGraySe`](read_gray_se.md).

The gray value opening is particularly fast for flat structuring
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

**`imageOpening`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Gray-opened image.

## Result

`GrayOpening` returns 2 (
H_MSG_TRUE)
if the structuring element is not
the empty region. Otherwise, an exception is raised.

## Possible Predecessors

`ReadGraySe`,
`GenDiscSe`,
`ReadImage`

## Alternatives

`DualRank`,
`GrayOpeningRect`,
`GrayOpeningShape`

## See also

`Opening`,
`GrayDilation`,
`GrayErosion`

## Module

Foundation
