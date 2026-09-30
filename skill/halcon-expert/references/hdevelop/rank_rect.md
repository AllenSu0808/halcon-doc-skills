# rank_rect (Operator)

## Name

`rank_rect` — Compute a rank filter with rectangular masks.

## Signature

`rank_rect(Image : ImageRank : MaskWidth, MaskHeight, Rank : )`

## Description

`rank_rect` performs a rank filter on the input image
*`Image`* with a rectangular mask of size *`MaskWidth`*
× *`MaskHeight`* and returns the filtered image
in *`ImageRank`*.

Conceptually, the rank filter sorts all gray values within the mask
in ascending order and then selects the gray value with rank
*`Rank`*. The rank 1 corresponds to the smallest gray value
and the rank *`MaskWidth`* * *`MaskHeight`*
corresponds to the largest gray value within the mask. For
*`Rank`* = (*`MaskWidth`* *
*`MaskHeight`* - 1) / 2 + 1, `rank_rect` returns the
median gray value (see [`median_rect`](median_rect.md)). For *`Rank`* = 1, `rank_rect` performs a gray value
erosion (see [`gray_erosion_rect`](gray_erosion_rect.md), [`gray_erosion_shape`](gray_erosion_shape.md),
and [`gray_erosion`](gray_erosion.md)), while for *`Rank`* =
*`MaskWidth`* * *`MaskHeight`* `rank_rect`
performs a gray value dilation (see [`gray_dilation_rect`](gray_dilation_rect.md),
[`gray_dilation_shape`](gray_dilation_shape.md), and [`gray_dilation`](gray_dilation.md)).

`rank_rect` can be used, for example, to suppress noise or to
suppress unwanted objects that are smaller than the mask.
Furthermore, `rank_rect` is less sensitive to noise than the
corresponding gray value morphology operators. Therefore, to obtain
a more robust version of the gray value morphology, instead of using
1 or *`MaskWidth`* * *`MaskHeight`*,
slightly larger or smaller values should be selected for
*`Rank`*.

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Attention

If even values instead of odd values are passed in
*`MaskHeight`* or *`MaskWidth`*, `rank_rect` uses
the next larger odd values instead.

`rank_rect` uses an algorithm with constant runtime per pixel,
i.e., the runtime only depends on the size of the input image and
not on the mask size. Therefore, for large mask sizes
`rank_rect` is the fastest implementation of the rank filter
in HALCON. Depending on the computer architecture (processor type,
availability of SIMD instructions like SSE2 or MMX, cache size and
throughput, memory throughput), for small mask sizes the
implementation used in [`rank_image`](rank_image.md) is faster than
`rank_rect`. Typically, this is the case for
*`MaskHeight`* $\le$ 15, but can also happen for larger
mask sizes, e.g., if SIMD instructions are unavailable and memory
throughput is low.

Furthermore, it should be noted that `rank_rect` uses a
recursive implementation, which internally computes the filter
response on the smallest enclosing rectangle of the domain of the
input image. Therefore, if the domain of the input image only
covers a small fraction of the smallest enclosing rectangle, it can
happen that [`rank_image`](rank_image.md) is faster than `rank_rect` even
for larger values of *`MaskHeight`*.

`rank_rect` should neither be used with *`Rank`* = 1 to perform a gray value erosion nor with
*`Rank`* = *`MaskWidth`* *
*`MaskHeight`* to perform a gray value dilation. In these
cases, the operators [`gray_erosion_rect`](gray_erosion_rect.md) or
[`gray_erosion_shape`](gray_erosion_shape.md) and [`gray_dilation_rect`](gray_dilation_rect.md) or
[`gray_dilation_shape`](gray_dilation_shape.md), respectively, are faster than
`rank_rect` for almost all mask sizes.

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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte)

Image to be filtered.

**`ImageRank`** (output_object)  (multichannel-)image(-array) `→` object (byte)

Filtered image.

**`MaskWidth`** (input_control)  integer `→`  (integer)

Width of the filter mask.

Default:
15

Suggested values:
3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 31, 49, 51, 61, 71, 81, 91, 101

Value range:
`3
≤
MaskWidth
≤
4095`

Minimum increment:
2

Recommended increment:
2

**`MaskHeight`** (input_control)  integer `→`  (integer)

Height of the filter mask.

Default:
15

Suggested values:
3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 31, 49, 51, 61, 71, 81, 91, 101

Value range:
`3
≤
MaskHeight
≤
4095`

Minimum increment:
2

Recommended increment:
2

**`Rank`** (input_control)  integer `→`  (integer)

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

If the parameter values are correct the operator `rank_rect`
returns the value 2 (
H_MSG_TRUE)
. The behavior in case of empty input (no
input images available) is set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Predecessors

`read_image`

## Possible Successors

`threshold`,
`dyn_threshold`,
`regiongrowing`

## Alternatives

`rank_image`,
`median_rect`,
`median_image`

## See also

`gray_erosion_rect`,
`gray_dilation_rect`,
`gray_erosion_shape`,
`gray_dilation_shape`,
`gray_erosion`,
`gray_dilation`

## References

S. Perreault, P. Hébert; “Median Filtering in Constant Time”;
IEEE Transactions on Image Processing, vol. 16, no. 9,
pp. 2389-2394, 2007.
  
D. Cline, K.B. White, P.K. Egbert; “Fast 8-Bit Median Filtering
Based On Separability”; International Conference on Image
Processing, vol. V, pp. 281-284, 2007.

## Module

Foundation
