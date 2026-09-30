# gray_skeleton (Operator)

## Name

`gray_skeleton` — Thinning of gray value images.

## Signature

`def gray_skeleton(image: HObject) -> HObject`

## Description

`gray_skeleton` applies a gray value thinning operation
to the input image *`image`*. Figuratively, the gray value
“mountain range” is reduced to its ridge lines by setting the gray
value of “hillsides” to the gray value at the corresponding valley
bottom. The resulting ridge lines are at most two pixels wide.
This operator is especially useful for thinning edge images, and is
thus an alternative to [`nonmax_suppression_amp`](nonmax_suppression_amp.md). In
contrast to [`nonmax_suppression_amp`](nonmax_suppression_amp.md),
`gray_skeleton` preserves contours, but is much slower.
In contrast to [`skeleton`](skeleton.md), this operator changes the gray
values of an image while leaving its region unchanged.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / uint2)

Image to be thinned.

**`gray_skeleton`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / uint2)

Thinned image.

## Result

`gray_skeleton` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Possible Successors

`mean_image`

## Alternatives

`nonmax_suppression_amp`,
`nonmax_suppression_dir`,
`local_max`

## See also

`skeleton`,
`gray_dilation_rect`

## Module

Foundation
