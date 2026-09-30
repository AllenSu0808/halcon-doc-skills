# rank_n (Operator)

## Name

`rank_n` — Return gray values with given rank from multiple channels.

## Signature

`rank_n(Image : RankImage : RankIndex : )`

## Description

The operator `rank_n` returns pixel-by-pixel the result of the
rank-function over all channels.

For every pixel in the input image the following is being done: The
gray values of all channels at this position are sorted in ascending
order. Then the pixel with index *`RankIndex`* is selected and
placed in the output image at the same position. The output image
has one channel.

In the special cases *`RankIndex`* = *1* and
*`RankIndex`* = *'(Number of channels)'* the minimum and
maximum are returned.
*`RankIndex`* = *'(Number of channels + 1) / 2'*
returns the median (here, / denotes integer division).
Hence, for a five-channel image, *3* returns the median.

The operator `rank_n` should not be confused with the operator
[`rank_image`](rank_image.md) which computes the rank within a certain mask.

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on domain level.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / int2 / uint2 / int4 / int8 / real)

Multichannel gray image.

**`RankImage`** (output_object)  singlechannelimage(-array) `→` object (byte / int2 / uint2 / int4 / int8 / real)

Result of the rank function.

**`RankIndex`** (input_control)  integer `→`  (integer)

Rank of the gray value images to return.

Default:
2

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20

## Example (HDevelop)

```
compose5 (Image1, Image2, Image3, Image4, Image5, MultiChannelImage)
rank_n (MultiChannelImage, ImageMin, 1)
rank_n (MultiChannelImage, ImageMax, 5)
rank_n (MultiChannelImage, ImageMedian, 3)
```

## Possible Predecessors

`compose2`,
`compose3`,
`compose4`,
`compose5`,
`add_channels`

## Alternatives

`mean_n`

## See also

`count_channels`,
`rank_image`

## Module

Foundation
