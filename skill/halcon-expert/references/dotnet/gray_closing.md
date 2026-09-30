# GrayClosing (Operator)

## Name

`GrayClosing` — Perform a gray value closing on an image.

## Signature

`static void HOperatorSet.GrayClosing(HObject image, HObject SE, out HObject imageClosing)`

`HImage HImage.GrayClosing(HImage SE)`

## Description

`GrayClosing` applies a gray value closing to the input image
*`image`* with the structuring element *`SE`*. The image
type of the structuring element *`SE`* must match the image
type of the input image *`image`*. The gray value closing of
an image i with a structuring element s is defined as
$$i \cdot s = (i \oplus s) \ominus \tilde{s}$$ ![figure](../assets/dae79b875c46d0a9.svg)
i.e., a dilation of the image with s followed by an erosion with
the transposed structuring element (see [`GrayDilation`](gray_dilation.md) and
[`GrayErosion`](gray_erosion.md)). For the generation of structuring elements,
see [`ReadGraySe`](read_gray_se.md).

The gray value closing is particularly fast for flat structuring
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

**`imageClosing`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Gray-closed image.

## Result

`GrayClosing` returns 2 (
H_MSG_TRUE)
if the structuring element is not
the empty region. Otherwise, an exception is raised.

## Possible Predecessors

`ReadGraySe`,
`GenDiscSe`,
`ReadImage`

## Alternatives

`DualRank`,
`GrayClosingRect`,
`GrayClosingShape`

## See also

`Closing`,
`GrayDilation`,
`GrayErosion`

## Module

Foundation
