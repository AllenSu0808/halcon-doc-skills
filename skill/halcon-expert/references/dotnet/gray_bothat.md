# GrayBothat (Operator)

## Name

`GrayBothat` — Perform a gray value bottom hat transformation on an image.

## Signature

`static void HOperatorSet.GrayBothat(HObject image, HObject SE, out HObject imageBotHat)`

`HImage HImage.GrayBothat(HImage SE)`

## Description

`GrayBothat` applies a gray value bottom hat transformation
to the input image *`image`* with the structuring element
*`SE`*. The image type of the structuring element *`SE`*
must match the image type of the input image *`image`*. The
gray value bottom hat transformation of an image i with a
structuring element s is defined as
$$\textit{bothat}(i,s)=(i\bullet s)-i,$$
i.e., the difference of the closing of the image with s and the
image (see [`GrayClosing`](gray_closing.md)). For the generation of structuring
elements, see [`ReadGraySe`](read_gray_se.md).

The gray value erosion is particularly fast for flat structuring
elements, i.e. structuring elements with a constant gray level
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

**`imageBotHat`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Bottom hat image.

## Result

`GrayBothat` returns 2 (
H_MSG_TRUE)
if the structuring element is not
the empty region. Otherwise, an exception is raised.

## Possible Predecessors

`ReadGraySe`,
`GenDiscSe`,
`ReadImage`

## Possible Successors

`Threshold`

## Alternatives

`GrayClosing`

## See also

`GrayTophat`,
`TopHat`,
`GrayErosionRect`,
`SubImage`

## Module

Foundation
