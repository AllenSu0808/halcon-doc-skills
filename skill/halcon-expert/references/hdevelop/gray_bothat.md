# gray_bothat (Operator)

## Name

`gray_bothat` — Perform a gray value bottom hat transformation on an image.

## Signature

`gray_bothat(Image, SE : ImageBotHat : : )`

## Description

`gray_bothat` applies a gray value bottom hat transformation
to the input image *`Image`* with the structuring element
*`SE`*. The image type of the structuring element *`SE`*
must match the image type of the input image *`Image`*. The
gray value bottom hat transformation of an image i with a
structuring element s is defined as
$$\textit{bothat}(i,s)=(i\bullet s)-i,$$
i.e., the difference of the closing of the image with s and the
image (see [`gray_closing`](gray_closing.md)). For the generation of structuring
elements, see [`read_gray_se`](read_gray_se.md).

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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / uint2 / real)

Input image.

**`SE`** (input_object)  singlechannelimage `→` object (byte / uint2 / real)

Structuring element.

**`ImageBotHat`** (output_object)  (multichannel-)image(-array) `→` object (byte / uint2 / real)

Bottom hat image.

## Result

`gray_bothat` returns 2 (
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

`gray_closing`

## See also

`gray_tophat`,
`top_hat`,
`gray_erosion_rect`,
`sub_image`

## Module

Foundation
