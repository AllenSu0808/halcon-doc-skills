# gray_dilation (Operator)

## Name

`gray_dilation` — Perform a gray value dilation on an image.

## Signature

`gray_dilation(Image, SE : ImageDilation : : )`

## Description

`gray_dilation` applies a gray value dilation to the input
image *`Image`* with the structuring element *`SE`*. The
image type of the structuring element *`SE`* must match the
image type of the input image *`Image`*. The gray value
dilation of an image i with a structuring element s at the pixel
position x is defined as:
$$(i \oplus s)(x) = \max\{f(x - z) + s(z) \mid z \in S\}$$ ![figure](../assets/d6d5dbca93d6726b.svg)
Here, S is the domain of the structuring element s (see
[`read_gray_se`](read_gray_se.md)).

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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / uint2 / real)

Input image.

**`SE`** (input_object)  singlechannelimage `→` object (byte / uint2 / real)

Structuring element.

**`ImageDilation`** (output_object)  (multichannel-)image(-array) `→` object (byte / uint2 / real)

Gray-dilated image.

## Result

`gray_dilation` returns 2 (
H_MSG_TRUE)
if the structuring element is not
the empty region. Otherwise, an exception is raised.

## Possible Predecessors

`read_gray_se`,
`gen_disc_se`,
`read_image`

## Possible Successors

`sub_image`,
`gray_erosion`

## Alternatives

`gray_dilation_rect`,
`gray_dilation_shape`

## See also

`gray_opening`,
`gray_closing`,
`dilation1`,
`gray_skeleton`

## Module

Foundation
