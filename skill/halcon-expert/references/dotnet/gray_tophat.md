# GrayTophat (Operator)

## Name

`GrayTophat` — Perform a gray value top hat transformation on an image.

## Signature

`static void HOperatorSet.GrayTophat(HObject image, HObject SE, out HObject imageTopHat)`

`HImage HImage.GrayTophat(HImage SE)`

## Description

`GrayTophat` applies a gray value top hat transformation to
the input image *`image`* with the structuring element
*`SE`*. The image type of the structuring element *`SE`*
must match the image type of the input image *`image`*. The
gray value top hat transformation of an image i with a structuring
element s is defined as
$$\textit{tophat}(i,s)=i-(i\circ s),$$
i.e., the difference of the image and its opening with s (see
[`GrayOpening`](gray_opening.md)). For the generation of structuring elements,
see [`ReadGraySe`](read_gray_se.md).

The top hat transformation is particularly fast for flat structuring
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

**`imageTopHat`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Top hat image.

## Result

`GrayTophat` returns 2 (
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

`GrayOpening`

## See also

`GrayBothat`,
`TopHat`,
`GrayErosionRect`,
`SubImage`

## Module

Foundation
