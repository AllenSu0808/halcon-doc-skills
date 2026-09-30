# gray_erosion (Operator)

## Name

`gray_erosion` — Perform a gray value erosion on an image.

## Signature

`def gray_erosion(image: HObject, se: HObject) -> HObject`

## Description

`gray_erosion` applies a gray value erosion to the input image
*`image`* with the structuring element *`se`*. The image
type of the structuring element *`se`* must match the image
type of the input image *`image`*. The gray value erosion of
an image i with a structuring element s at the pixel position
x is defined as:
$$(i \oplus s)(x) = \min{f(x + z) - s(z)\,|\,z \in S}$$ ![figure](../assets/939864be17b34d54.svg)
Here, S is the domain of the structuring element s (see
[`read_gray_se`](read_gray_se.md)).

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

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / uint2 / real)

Input image.

**`se`** (input_object)  singlechannelimage `→` HObject (byte / uint2 / real)

Structuring element.

**`image_erosion`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / uint2 / real)

Gray-eroded image.

## Result

`gray_erosion` returns 2 (
H_MSG_TRUE)
if the structuring element is not
the empty region. Otherwise, an exception is raised.

## Possible Predecessors

`read_gray_se`,
`gen_disc_se`,
`read_image`

## Possible Successors

`gray_dilation`,
`sub_image`

## Alternatives

`gray_erosion_rect`,
`gray_erosion_shape`

## See also

`gray_opening`,
`gray_closing`,
`erosion1`,
`gray_skeleton`

## Module

Foundation
