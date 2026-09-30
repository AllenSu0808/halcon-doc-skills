# MedianRect (Operator)

## Name

`MedianRect` — Compute a median filter with rectangular masks.

## Signature

`static void HOperatorSet.MedianRect(HObject image, out HObject imageMedian, HTuple maskWidth, HTuple maskHeight)`

`HImage HImage.MedianRect(int maskWidth, int maskHeight)`

## Description

`MedianRect` performs a median filter on the input image
*`image`* with a rectangular mask of size *`maskWidth`*
× *`maskHeight`* and returns the filtered image
in *`imageMedian`*.

Conceptually, the median filter sorts all gray values within the
mask in ascending order and then selects the median of the gray
values. The median is the “middle” one of the sorted gray values,
i.e., the gray value with rank (position) (*`maskWidth`* *
*`maskHeight`* - 1) / 2 + 1 of the sorted gray values, where
the rank 1 corresponds to the smallest gray value and the rank
*`maskWidth`*
* *`maskHeight`* corresponds to the largest gray value within
the mask (see also [`RankRect`](rank_rect.md)).

`MedianRect` can be used, for example, to smooth images, to
suppress unwanted objects (e.g., point-like or line-like structures)
that are smaller than the mask, and can therefore be used to
estimate the background illumination for a shading correction or as
a preprocessing step for the dynamic threshold operation (see
[`DynThreshold`](dyn_threshold.md)).

When using a 3x3 or 5x5 filter mask, `MedianRect` can be executed
on OpenCL devices.

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Attention

If even values instead of odd values are passed in
*`maskHeight`* or *`maskWidth`*, `MedianRect` uses
the next larger odd values instead.

`MedianRect` uses an algorithm with constant runtime per
pixel, i.e., the runtime only depends on the size of the input image
and not on the mask size. Therefore, for large mask sizes
`MedianRect` is the fastest implementation of the median
filter in HALCON. Depending on the computer architecture (processor
type, availability of SIMD instructions like SSE2 or MMX, cache size
and throughput, memory throughput), for small mask sizes the
implementation used in [`MedianImage`](median_image.md) and [`RankImage`](rank_image.md)
is faster than `MedianRect`. Typically, this is the case for
*`maskHeight`* $\le$ 15, but can also happen for larger
mask sizes, e.g., if SIMD instructions are unavailable and memory
throughput is low.

Furthermore, it should be noted that `MedianRect` uses a
recursive implementation, which internally computes the filter
response on the smallest enclosing rectangle of the domain of the
input image. Therefore, if the domain of the input image only
covers a small fraction of the smallest enclosing rectangle, it can
happen that [`MedianImage`](median_image.md) and [`RankImage`](rank_image.md) are faster
than `MedianRect` even for larger values of
*`maskHeight`*.

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte*) **allowed for compute devices*

Image to be filtered.

**`imageMedian`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte)

Filtered image.

**`maskWidth`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Width of the filter mask.

Default:
15

List of values (for compute devices):
3, 5

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

List of values (for compute devices):
3, 5

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

## Complexity

For each pixel: O(1).

## Result

If the parameter values are correct the operator `MedianRect`
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

`MedianImage`,
`RankRect`,
`RankImage`

## See also

`GrayErosionRect`,
`GrayDilationRect`,
`GrayErosionShape`,
`GrayDilationShape`,
`GrayErosion`,
`GrayDilation`

## References

S. Perreault, P. Hébert; “Median Filtering in Constant Time”;
IEEE Transactions on Image Processing vol. 16, no. 9, pp. 2389-2394,
2007.
  
D. Cline, K.B. White, P.K. Egbert; “Fast 8-Bit Median Filtering
Based On Separability”; International Conference on Image
Processing, vol. V, pp. 281-284, 2007.

## Module

Foundation
