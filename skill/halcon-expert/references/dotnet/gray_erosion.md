# GrayErosion (Operator)

## Name

`GrayErosion` — Perform a gray value erosion on an image.

## Signature

`static void HOperatorSet.GrayErosion(HObject image, HObject SE, out HObject imageErosion)`

`HImage HImage.GrayErosion(HImage SE)`

## Description

`GrayErosion` applies a gray value erosion to the input image
*`image`* with the structuring element *`SE`*. The image
type of the structuring element *`SE`* must match the image
type of the input image *`image`*. The gray value erosion of
an image i with a structuring element s at the pixel position
x is defined as:
$$(i \oplus s)(x) = \min{f(x + z) - s(z)\,|\,z \in S}$$ ![figure](../assets/939864be17b34d54.svg)
Here, S is the domain of the structuring element s (see
[`ReadGraySe`](read_gray_se.md)).

The gray value erosion is particularly fast for flat structuring
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

**`imageErosion`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Gray-eroded image.

## Result

`GrayErosion` returns 2 (
H_MSG_TRUE)
if the structuring element is not
the empty region. Otherwise, an exception is raised.

## Possible Predecessors

`ReadGraySe`,
`GenDiscSe`,
`ReadImage`

## Possible Successors

`GrayDilation`,
`SubImage`

## Alternatives

`GrayErosionRect`,
`GrayErosionShape`

## See also

`GrayOpening`,
`GrayClosing`,
`Erosion1`,
`GraySkeleton`

## Module

Foundation
