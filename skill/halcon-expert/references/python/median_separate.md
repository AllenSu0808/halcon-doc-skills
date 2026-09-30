# median_separate (Operator)

## Name

`median_separate` — Separated median filtering with rectangle masks.

## Signature

`def median_separate(image: HObject, mask_width: int, mask_height: int, margin: Union[int, float, str]) -> HObject`

## Description

The operator `median_separate` carries out a variation of
the median filtering: First two auxiliary images are created. The
first one originates from a median filtering with a horizontal mask
having a height of one pixel and the width *`mask_width`*
followed by filtering with a vertical mask having the height
*`mask_height`* and width of one pixel.
The second auxiliary image is created by
filtering with the same masks, but with a reversed sequence of the
operation: first the vertical, then the horizontal mask. The output
image results from averaging the two auxiliary images pixel by
pixel.

The operator `median_separate` is clearly faster than the
normal operator [`median_image`](median_image.md) because both masks are one pixel
wide, facilitating a very efficient processing. The runtime is
practically *independent* of the size of the mask. For example, the
operator `median_separate` can be well used after texture
filters, where large masks are needed.

The filter can also be used several times in a row in order to
enhance the smoothing.

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

Due to performance reasons, the input *`image`* is not checked whether
it contains NaNs. Using an input image with NaNs crashes HALCON.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / int2 / uint2 / int4 / real)

Image to be filtered.

**`image_smedian`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / int2 / uint2 / int4 / real)

Median filtered image.

**`mask_width`** (input_control)  extent.x `→` int

Width of rank mask.

Default:
25

Suggested values:
1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 27, 43, 51, 67, 91, 121, 151

Value range:
`1
≤
mask_width
≤
401`

Minimum increment:
2

Recommended increment:
2

**`mask_height`** (input_control)  extent.y `→` int

Height of rank mask.

Default:
25

Suggested values:
1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 27, 43, 51, 67, 91, 121, 151

Value range:
`1
≤
mask_height
≤
401`

Minimum increment:
2

Recommended increment:
2

**`margin`** (input_control)  string `→` Union[int, float, str]

Border treatment.

Default:
"mirrored"

Suggested values:
"mirrored", "cyclic", "continued", 0, 30, 60, 90, 120, 150, 180, 210, 240, 255

## Complexity

For each pixel: O(40).

## Possible Predecessors

`texture_laws`,
`sobel_amp`,
`deviation_image`

## Possible Successors

`learn_ndim_norm`,
`regiongrowing`,
`auto_threshold`

## Alternatives

`median_image`

## See also

`rank_image`

## References

R. Haralick, L. Shapiro; “Computer and Robot Vision”;
Addison-Wesley, 1992, Seite 319

## Module

Foundation
