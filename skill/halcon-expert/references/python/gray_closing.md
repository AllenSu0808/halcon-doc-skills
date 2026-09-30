# gray_closing (Operator)

## Name

`gray_closing` — Perform a gray value closing on an image.

## Signature

`def gray_closing(image: HObject, se: HObject) -> HObject`

## Description

`gray_closing` applies a gray value closing to the input image
*`image`* with the structuring element *`se`*. The image
type of the structuring element *`se`* must match the image
type of the input image *`image`*. The gray value closing of
an image i with a structuring element s is defined as
$$i \cdot s = (i \oplus s) \ominus \tilde{s}$$ ![figure](../assets/dae79b875c46d0a9.svg)
i.e., a dilation of the image with s followed by an erosion with
the transposed structuring element (see [`gray_dilation`](gray_dilation.md) and
[`gray_erosion`](gray_erosion.md)). For the generation of structuring elements,
see [`read_gray_se`](read_gray_se.md).

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

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / uint2 / real)

Input image.

**`se`** (input_object)  singlechannelimage `→` HObject (byte / uint2 / real)

Structuring element.

**`image_closing`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / uint2 / real)

Gray-closed image.

## Result

`gray_closing` returns 2 (
H_MSG_TRUE)
if the structuring element is not
the empty region. Otherwise, an exception is raised.

## Possible Predecessors

`read_gray_se`,
`gen_disc_se`,
`read_image`

## Alternatives

`dual_rank`,
`gray_closing_rect`,
`gray_closing_shape`

## See also

`closing`,
`gray_dilation`,
`gray_erosion`

## Module

Foundation
