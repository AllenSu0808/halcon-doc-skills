# gray_opening (Operator)

## Name

`gray_opening` — Perform a gray value opening on an image.

## Signature

`def gray_opening(image: HObject, se: HObject) -> HObject`

## Description

`gray_opening` applies a gray value opening to the input image
*`image`* with the structuring element *`se`*. The image
type of the structuring element *`se`* must match the image
type of the input image *`image`*. The gray value opening of
an image i with a structuring element s is defined as
$$i \odot s = (i \odot s) \oplus \tilde{s}$$ ![figure](../assets/4f0608759837c826.svg)
i.e., an erosion of the image with s followed by a dilation with
the transposed structuring element (see [`gray_erosion`](gray_erosion.md) and
[`gray_dilation`](gray_dilation.md)). For the generation of structuring elements,
see [`read_gray_se`](read_gray_se.md).

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

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / uint2 / real)

Input image.

**`se`** (input_object)  singlechannelimage `→` HObject (byte / uint2 / real)

Structuring element.

**`image_opening`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / uint2 / real)

Gray-opened image.

## Result

`gray_opening` returns 2 (
H_MSG_TRUE)
if the structuring element is not
the empty region. Otherwise, an exception is raised.

## Possible Predecessors

`read_gray_se`,
`gen_disc_se`,
`read_image`

## Alternatives

`dual_rank`,
`gray_opening_rect`,
`gray_opening_shape`

## See also

`opening`,
`gray_dilation`,
`gray_erosion`

## Module

Foundation
