# rank_image (Operator)

## Name

`rank_image` — Compute a rank filter with arbitrary masks.

## Signature

`rank_image(Image, Mask : ImageRank : Rank, Margin : )`

## Description

`rank_image` performs a rank filter on the input image
*`Image`* with a mask that is specified by the region
*`Mask`* and returns the filtered image in *`ImageRank`*.
The shape of the mask can be chosen arbitrarily and can, for
example, be created with operators like [`gen_circle`](gen_circle.md) or
[`draw_region`](draw_region.md). The position of the mask does not influence
the result since the center of gravity of the mask region is used as
the reference point of the mask.

Conceptually, the rank filter sorts all gray values within the mask
in ascending order and then selects the gray value with rank
*`Rank`*. The rank 1 corresponds to the smallest gray value
and the rank A corresponds to the largest gray value within the
mask. Here, A denotes the area of *`Mask`* (see
[`area_center`](area_center.md)). For *`Rank`* = (A - 1) / 2 + 1,
`rank_image` returns the median gray value (see
[`median_image`](median_image.md)). For *`Rank`* = 1, `rank_image`
performs a gray value erosion (see [`gray_erosion_rect`](gray_erosion_rect.md),
[`gray_erosion_shape`](gray_erosion_shape.md), and [`gray_erosion`](gray_erosion.md)), while for
*`Rank`* = A `rank_image` performs a gray value
dilation (see [`gray_dilation_rect`](gray_dilation_rect.md),
[`gray_dilation_shape`](gray_dilation_shape.md), and [`gray_dilation`](gray_dilation.md)).

`rank_image` can be used, for example, to suppress noise or to
suppress unwanted objects that are smaller than the mask.
Furthermore, `rank_image` is less sensitive to noise than the
corresponding gray value morphology operators. Therefore, to obtain
a more robust version of the gray value morphology, instead of using
1 or A, slightly larger or smaller values should be selected for
*`Rank`*.

Several border treatments can be chosen for filtering via the
parameter *`Margin`*:

- **gray value** —

  Pixels outside of the image border are assumed to be
  constant (with the indicated gray value).
- ***'continued'*** —

  Continuation of the gray values at the image
  border.
- ***'cyclic'*** —

  Cyclic continuation at the image borders.
- ***'mirrored'*** —

  Reflection of pixels at the image borders.

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Attention

`rank_image` uses an algorithm with a runtime per pixel that
depends on the number of runs in the mask *`Mask`*. Therefore,
`rank_image` is slower than [`rank_rect`](rank_rect.md) for rectangular
masks with a large mask height. The precise mask height for which
[`rank_rect`](rank_rect.md) will become faster than `rank_image` depends
on the computer architecture (processor type, availability of SIMD
instructions like SSE2 or MMX, cache size and throughput, memory
throughput). Typically, this is the case for mask heights > 15,
but can also be the case only for larger mask sizes, e.g., if SIMD
instructions are unavailable and memory throughput is low.

Furthermore, it should be noted that [`rank_rect`](rank_rect.md) uses a
recursive implementation, which internally computes the filter
response on the smallest enclosing rectangle of the domain of the
input image. Therefore, if the domain of the input image only
covers a small fraction of the smallest enclosing rectangle, it can
happen that `rank_image` is faster than [`rank_rect`](rank_rect.md) even
for larger mask heights.

`rank_image` should neither be used with *`Rank`* = 1
to perform a gray value erosion nor with *`Rank`* = A to
perform a gray value dilation. In these cases, the operators
[`gray_erosion_rect`](gray_erosion_rect.md), [`gray_erosion_shape`](gray_erosion_shape.md), or
[`gray_erosion`](gray_erosion.md) and [`gray_dilation_rect`](gray_dilation_rect.md),
[`gray_dilation_shape`](gray_dilation_shape.md), or [`gray_dilation`](gray_dilation.md), respectively,
are typically faster than `rank_image`.

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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / int2 / uint2 / int4 / real)

Image to be filtered.

**`Mask`** (input_object)  region `→` object

Filter mask.

**`ImageRank`** (output_object)  multichannel-image(-array) `→` object (byte / int2 / uint2 / int4 / real)

Filtered image.

**`Rank`** (input_control)  integer `→`  (integer)

Rank of the output gray value.

Default:
5

Suggested values:
3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 31, 49, 51, 61, 71, 81, 91, 101

Value range:
`1
≤
Rank
≤
4095`

Minimum increment:
1

Recommended increment:
2

**`Margin`** (input_control)  string `→`  (string / integer / real)

Border treatment.

Default:
'mirrored'

Suggested values:
'mirrored', 'cyclic', 'continued', 0, 30, 60, 90, 120, 150, 180, 210, 240, 255

## Example (HDevelop)

```
read_image (Image, 'fabrik')
draw_region (Region, WindowHandle)
rank_image (Image, Region, ImageRank, 5, 'mirrored')
dev_display(ImageRank)
```

## Complexity

For each pixel: O(N), where N is the number of runs of
*`Mask`* (see [`runlength_features`](runlength_features.md)).

## Result

If the parameter values are correct the operator `rank_image`
returns the value 2 (
H_MSG_TRUE)
. The behavior in case of empty input (no
input images available) is set via the operator
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Predecessors

`read_image`,
`draw_region`,
`gen_circle`,
`gen_rectangle1`,
`gen_rectangle2`

## Possible Successors

`threshold`,
`dyn_threshold`,
`regiongrowing`

## Alternatives

`rank_rect`,
`median_image`,
`median_rect`

## See also

`gray_erosion_rect`,
`gray_dilation_rect`,
`gray_erosion_shape`,
`gray_dilation_shape`,
`gray_erosion`,
`gray_dilation`

## References

T.S. Huang, G.J. Yang, G.Y. Tang; “A Fast Two-Dimensional Median
Filtering Algorithm”; IEEE Transactions on Acoustics, Speech, and
Signal Processing, vol. 27, no. 1, pp. 13-18, 1979.
  
R. Haralick, L. Shapiro; “Computer and Robot Vision”;
Addison-Wesley, 1992, pp. 318-320.

## Module

Foundation
