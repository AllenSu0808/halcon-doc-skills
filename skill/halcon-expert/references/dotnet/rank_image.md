# RankImage (Operator)

## Name

`RankImage` — Compute a rank filter with arbitrary masks.

## Signature

`static void HOperatorSet.RankImage(HObject image, HObject mask, out HObject imageRank, HTuple rank, HTuple margin)`

`HImage HImage.RankImage(HRegion mask, int rank, HTuple margin)`

`HImage HImage.RankImage(HRegion mask, int rank, string margin)`

## Description

`RankImage` performs a rank filter on the input image
*`image`* with a mask that is specified by the region
*`mask`* and returns the filtered image in *`imageRank`*.
The shape of the mask can be chosen arbitrarily and can, for
example, be created with operators like [`GenCircle`](gen_circle.md) or
[`DrawRegion`](draw_region.md). The position of the mask does not influence
the result since the center of gravity of the mask region is used as
the reference point of the mask.

Conceptually, the rank filter sorts all gray values within the mask
in ascending order and then selects the gray value with rank
*`rank`*. The rank 1 corresponds to the smallest gray value
and the rank A corresponds to the largest gray value within the
mask. Here, A denotes the area of *`mask`* (see
[`AreaCenter`](area_center.md)). For *`rank`* = (A - 1) / 2 + 1,
`RankImage` returns the median gray value (see
[`MedianImage`](median_image.md)). For *`rank`* = 1, `RankImage`
performs a gray value erosion (see [`GrayErosionRect`](gray_erosion_rect.md),
[`GrayErosionShape`](gray_erosion_shape.md), and [`GrayErosion`](gray_erosion.md)), while for
*`rank`* = A `RankImage` performs a gray value
dilation (see [`GrayDilationRect`](gray_dilation_rect.md),
[`GrayDilationShape`](gray_dilation_shape.md), and [`GrayDilation`](gray_dilation.md)).

`RankImage` can be used, for example, to suppress noise or to
suppress unwanted objects that are smaller than the mask.
Furthermore, `RankImage` is less sensitive to noise than the
corresponding gray value morphology operators. Therefore, to obtain
a more robust version of the gray value morphology, instead of using
1 or A, slightly larger or smaller values should be selected for
*`rank`*.

Several border treatments can be chosen for filtering via the
parameter *`margin`*:

- **gray value** —

  Pixels outside of the image border are assumed to be
  constant (with the indicated gray value).
- ***"continued"*** —

  Continuation of the gray values at the image
  border.
- ***"cyclic"*** —

  Cyclic continuation at the image borders.
- ***"mirrored"*** —

  Reflection of pixels at the image borders.

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Attention

`RankImage` uses an algorithm with a runtime per pixel that
depends on the number of runs in the mask *`mask`*. Therefore,
`RankImage` is slower than [`RankRect`](rank_rect.md) for rectangular
masks with a large mask height. The precise mask height for which
[`RankRect`](rank_rect.md) will become faster than `RankImage` depends
on the computer architecture (processor type, availability of SIMD
instructions like SSE2 or MMX, cache size and throughput, memory
throughput). Typically, this is the case for mask heights > 15,
but can also be the case only for larger mask sizes, e.g., if SIMD
instructions are unavailable and memory throughput is low.

Furthermore, it should be noted that [`RankRect`](rank_rect.md) uses a
recursive implementation, which internally computes the filter
response on the smallest enclosing rectangle of the domain of the
input image. Therefore, if the domain of the input image only
covers a small fraction of the smallest enclosing rectangle, it can
happen that `RankImage` is faster than [`RankRect`](rank_rect.md) even
for larger mask heights.

`RankImage` should neither be used with *`rank`* = 1
to perform a gray value erosion nor with *`rank`* = A to
perform a gray value dilation. In these cases, the operators
[`GrayErosionRect`](gray_erosion_rect.md), [`GrayErosionShape`](gray_erosion_shape.md), or
[`GrayErosion`](gray_erosion.md) and [`GrayDilationRect`](gray_dilation_rect.md),
[`GrayDilationShape`](gray_dilation_shape.md), or [`GrayDilation`](gray_dilation.md), respectively,
are typically faster than `RankImage`.

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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / int4 / real)

Image to be filtered.

**`mask`** (input_object)  region `→` [HRegion](HRegion.md)

Filter mask.

**`imageRank`** (output_object)  multichannel-image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / int4 / real)

Filtered image.

**`rank`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Rank of the output gray value.

Default:
5

Suggested values:
3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 31, 49, 51, 61, 71, 81, 91, 101

Value range:
`1
≤
rank
≤
4095`

Minimum increment:
1

Recommended increment:
2

**`margin`** (input_control)  string `→` [HTuple](HTuple.md) (*string* / int / long / double)

Border treatment.

Default:
"mirrored"

Suggested values:
"mirrored", "cyclic", "continued", 0, 30, 60, 90, 120, 150, 180, 210, 240, 255

## Example (HDevelop)

```
read_image (Image, 'fabrik')
draw_region (Region, WindowHandle)
rank_image (Image, Region, ImageRank, 5, 'mirrored')
dev_display(ImageRank)
```

## Complexity

For each pixel: O(N), where N is the number of runs of
*`mask`* (see [`RunlengthFeatures`](runlength_features.md)).

## Result

If the parameter values are correct the operator `RankImage`
returns the value 2 (
H_MSG_TRUE)
. The behavior in case of empty input (no
input images available) is set via the operator
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Predecessors

`ReadImage`,
`DrawRegion`,
`GenCircle`,
`GenRectangle1`,
`GenRectangle2`

## Possible Successors

`Threshold`,
`DynThreshold`,
`Regiongrowing`

## Alternatives

`RankRect`,
`MedianImage`,
`MedianRect`

## See also

`GrayErosionRect`,
`GrayDilationRect`,
`GrayErosionShape`,
`GrayDilationShape`,
`GrayErosion`,
`GrayDilation`

## References

T.S. Huang, G.J. Yang, G.Y. Tang; “A Fast Two-Dimensional Median
Filtering Algorithm”; IEEE Transactions on Acoustics, Speech, and
Signal Processing, vol. 27, no. 1, pp. 13-18, 1979.
  
R. Haralick, L. Shapiro; “Computer and Robot Vision”;
Addison-Wesley, 1992, pp. 318-320.

## Module

Foundation
