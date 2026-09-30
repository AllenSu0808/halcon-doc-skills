# RankRect (Operator)

## Name

`RankRect` — Compute a rank filter with rectangular masks.

## Signature

`static void HOperatorSet.RankRect(HObject image, out HObject imageRank, HTuple maskWidth, HTuple maskHeight, HTuple rank)`

`HImage HImage.RankRect(int maskWidth, int maskHeight, int rank)`

## Description

`RankRect` performs a rank filter on the input image
*`image`* with a rectangular mask of size *`maskWidth`*
× *`maskHeight`* and returns the filtered image
in *`imageRank`*.

Conceptually, the rank filter sorts all gray values within the mask
in ascending order and then selects the gray value with rank
*`rank`*. The rank 1 corresponds to the smallest gray value
and the rank *`maskWidth`* * *`maskHeight`*
corresponds to the largest gray value within the mask. For
*`rank`* = (*`maskWidth`* *
*`maskHeight`* - 1) / 2 + 1, `RankRect` returns the
median gray value (see [`MedianRect`](median_rect.md)). For *`rank`* = 1, `RankRect` performs a gray value
erosion (see [`GrayErosionRect`](gray_erosion_rect.md), [`GrayErosionShape`](gray_erosion_shape.md),
and [`GrayErosion`](gray_erosion.md)), while for *`rank`* =
*`maskWidth`* * *`maskHeight`* `RankRect`
performs a gray value dilation (see [`GrayDilationRect`](gray_dilation_rect.md),
[`GrayDilationShape`](gray_dilation_shape.md), and [`GrayDilation`](gray_dilation.md)).

`RankRect` can be used, for example, to suppress noise or to
suppress unwanted objects that are smaller than the mask.
Furthermore, `RankRect` is less sensitive to noise than the
corresponding gray value morphology operators. Therefore, to obtain
a more robust version of the gray value morphology, instead of using
1 or *`maskWidth`* * *`maskHeight`*,
slightly larger or smaller values should be selected for
*`rank`*.

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Attention

If even values instead of odd values are passed in
*`maskHeight`* or *`maskWidth`*, `RankRect` uses
the next larger odd values instead.

`RankRect` uses an algorithm with constant runtime per pixel,
i.e., the runtime only depends on the size of the input image and
not on the mask size. Therefore, for large mask sizes
`RankRect` is the fastest implementation of the rank filter
in HALCON. Depending on the computer architecture (processor type,
availability of SIMD instructions like SSE2 or MMX, cache size and
throughput, memory throughput), for small mask sizes the
implementation used in [`RankImage`](rank_image.md) is faster than
`RankRect`. Typically, this is the case for
*`maskHeight`* $\le$ 15, but can also happen for larger
mask sizes, e.g., if SIMD instructions are unavailable and memory
throughput is low.

Furthermore, it should be noted that `RankRect` uses a
recursive implementation, which internally computes the filter
response on the smallest enclosing rectangle of the domain of the
input image. Therefore, if the domain of the input image only
covers a small fraction of the smallest enclosing rectangle, it can
happen that [`RankImage`](rank_image.md) is faster than `RankRect` even
for larger values of *`maskHeight`*.

`RankRect` should neither be used with *`rank`* = 1 to perform a gray value erosion nor with
*`rank`* = *`maskWidth`* *
*`maskHeight`* to perform a gray value dilation. In these
cases, the operators [`GrayErosionRect`](gray_erosion_rect.md) or
[`GrayErosionShape`](gray_erosion_shape.md) and [`GrayDilationRect`](gray_dilation_rect.md) or
[`GrayDilationShape`](gray_dilation_shape.md), respectively, are faster than
`RankRect` for almost all mask sizes.

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte)

Image to be filtered.

**`imageRank`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte)

Filtered image.

**`maskWidth`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Width of the filter mask.

Default:
15

Suggested values:
3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 31, 49, 51, 61, 71, 81, 91, 101

Value range:
`3
≤
maskWidth
≤
4095`

Minimum increment:
2

Recommended increment:
2

**`maskHeight`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Height of the filter mask.

Default:
15

Suggested values:
3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 31, 49, 51, 61, 71, 81, 91, 101

Value range:
`3
≤
maskHeight
≤
4095`

Minimum increment:
2

Recommended increment:
2

**`rank`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Rank of the output gray value.

Default:
5

Suggested values:
3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 31, 49, 51, 61, 71, 81, 91, 101

Minimum increment:
1

Recommended increment:
2

Restriction:
`1 <= Rank && Rank <= MaskWidth * MaskHeight`

## Complexity

For each pixel: O(1).

## Result

If the parameter values are correct the operator `RankRect`
returns the value 2 (
H_MSG_TRUE)
. The behavior in case of empty input (no
input images available) is set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Predecessors

`ReadImage`

## Possible Successors

`Threshold`,
`DynThreshold`,
`Regiongrowing`

## Alternatives

`RankImage`,
`MedianRect`,
`MedianImage`

## See also

`GrayErosionRect`,
`GrayDilationRect`,
`GrayErosionShape`,
`GrayDilationShape`,
`GrayErosion`,
`GrayDilation`

## References

S. Perreault, P. Hébert; “Median Filtering in Constant Time”;
IEEE Transactions on Image Processing, vol. 16, no. 9,
pp. 2389-2394, 2007.
  
D. Cline, K.B. White, P.K. Egbert; “Fast 8-Bit Median Filtering
Based On Separability”; International Conference on Image
Processing, vol. V, pp. 281-284, 2007.

## Module

Foundation
