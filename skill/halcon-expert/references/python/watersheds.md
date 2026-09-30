# watersheds (Operator)

## Name

`watersheds` — Extract watersheds and basins from an image.

## Signature

`def watersheds(image: HObject) -> Tuple[HObject, HObject]`

## Description

`watersheds` segments an image based on the topology of
the gray values. The image is interpreted as a “mountain range.”
Higher gray values correspond to “mountains,” while lower gray
values correspond to “valleys.” In the resulting mountain range
watersheds are extracted. These correspond to the bright ridges
between dark basins. On output, the parameter *`basins`*
contains these basins, while *`watersheds`* contains the
watersheds, which are at most one pixel wide.
*`watersheds`* always is a single
region per input image, while *`basins`* contains a separate
region for each basin.

It is advisable to apply a smoothing operator (e.g.,
[`binomial_filter`](binomial_filter.md) or [`gauss_filter`](gauss_filter.md)) to the input image
before calling `watersheds` in order to reduce the number of
output regions. A more sophisticated way to reduce the number of
output regions is to merge neighboring basins based on a threshold
criterion by using [`watersheds_threshold`](watersheds_threshold.md) instead (for more
details please refer to the documentation of
[`watersheds_threshold`](watersheds_threshold.md)).

## Attention

If the image contains many fine structures or is noisy, many output
regions result, and thus the runtime increases considerably.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` HObject (byte / uint2 / real)

Input image.

**`basins`** (output_object)  region-array `→` HObject

Segmented basins.

**`watersheds`** (output_object)  region(-array) `→` HObject

Watersheds between the basins.

## Result

`watersheds` always returns 2 (
H_MSG_TRUE)
. The behavior with
respect to the input images and output regions can be determined by
setting the values of the flags *"no_object_result"*,
*"empty_region_result"*, and *"store_empty_region"*
with [`set_system`](set_system.md). If necessary, an exception is raised.

## Possible Predecessors

`binomial_filter`,
`gauss_filter`,
`smooth_image`,
`invert_image`

## Possible Successors

`expand_region`,
`select_shape`,
`reduce_domain`,
`opening`

## Alternatives

`watersheds_threshold`,
`pouring`,
`watersheds_marker`

## References

L. Vincent, P. Soille: “Watersheds in Digital Space: An Efficient
Algorithm Based on Immersion Simulations”; IEEE Transactions on Pattern
Analysis and Machine Intelligence; vol. 13, no. 6; pp. 583-598; 1991.

## Module

Foundation
