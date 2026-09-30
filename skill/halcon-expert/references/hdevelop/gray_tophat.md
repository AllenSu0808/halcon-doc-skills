# gray_tophat (Operator)

## Name

`gray_tophat` — Perform a gray value top hat transformation on an image.

## Signature

`gray_tophat(Image, SE : ImageTopHat : : )`

## Description

`gray_tophat` applies a gray value top hat transformation to
the input image *`Image`* with the structuring element
*`SE`*. The image type of the structuring element *`SE`*
must match the image type of the input image *`Image`*. The
gray value top hat transformation of an image i with a structuring
element s is defined as
$$\textit{tophat}(i,s)=i-(i\circ s),$$
i.e., the difference of the image and its opening with s (see
[`gray_opening`](gray_opening.md)). For the generation of structuring elements,
see [`read_gray_se`](read_gray_se.md).

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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / uint2 / real)

Input image.

**`SE`** (input_object)  singlechannelimage `→` object (byte / uint2 / real)

Structuring element.

**`ImageTopHat`** (output_object)  (multichannel-)image(-array) `→` object (byte / uint2 / real)

Top hat image.

## Result

`gray_tophat` returns 2 (
H_MSG_TRUE)
if the structuring element is not
the empty region. Otherwise, an exception is raised.

## Possible Predecessors

`read_gray_se`,
`gen_disc_se`,
`read_image`

## Possible Successors

`threshold`

## Alternatives

`gray_opening`

## See also

`gray_bothat`,
`top_hat`,
`gray_erosion_rect`,
`sub_image`

## Module

Foundation
