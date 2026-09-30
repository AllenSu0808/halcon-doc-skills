# median_image (Operator)

## Name

`median_image` — Compute a median filter with various masks.

## Signature

`median_image(Image : ImageMedian : MaskType, Radius, Margin : )`

## Description

`median_image` performs a median filter on the input image
*`Image`* with a square or circular mask and returns the
filtered image in *`ImageMedian`*. The shape of the mask can
be selected with *`MaskType`*. The radius of the mask can be
selected with *`Radius`*.

Conceptually, the median filter sorts all gray values within the
mask in ascending order and then selects the median of the gray
values. The median is the “middle” one of the sorted gray values,
i.e., the gray value with rank (position) (N - 1) / 2 + 1 of the
sorted gray values, where N denotes the number of pixels covered by
the filter mask.
Here, the rank 1 corresponds to the smallest gray value and the rank N
corresponds to the largest gray value within the mask (see also
[`rank_image`](rank_image.md)).

The filter mask is determined by *`Radius`*, defining the size, and
*`MaskType`*, defining the shape of the mask.
For latter one, the following options are available:

- ***'circle'*** —

  The mask consists of the pixel within a circle
  with *`Radius`* around the pixel of the mask center.
- ***'square'*** —

  The mask consists of the pixel within a square
  with an edge length of
  $2\cdot$*`Radius`* $+1$ pixel.

`median_image` can be used, for example, to smooth images, to
suppress unwanted objects (e.g., point-like or line-like structures)
that are smaller than the mask, and can therefore be used to
estimate the background illumination for a shading correction or as
a preprocessing step for the dynamic threshold operation (see
[`dyn_threshold`](dyn_threshold.md)).

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

When using the *`MaskType`* *'square'* with *`Radius`* 1 or 2
(resulting in a 3x3 or 5x5 pixel filter mask) and the border treatment
'mirrored', `median_image` can be executed on OpenCL devices.

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Attention

`median_image` uses an algorithm with a runtime per pixel that
depends on the mask height 2 *
*`Radius`* + 1. Therefore, `median_image` is slower
than [`median_rect`](median_rect.md) for square masks with a large mask height.
The precise mask height for which [`median_rect`](median_rect.md) will become
faster than `median_image` depends on the computer
architecture (processor type, availability of SIMD instructions like
SSE2 or MMX, cache size and throughput, memory throughput).
Typically, this is the case for mask heights > 15, but can also be
the case only for larger mask sizes, e.g., if SIMD instructions are
unavailable and memory throughput is low.

Furthermore, it should be noted that [`median_rect`](median_rect.md) uses a
recursive implementation, which internally computes the filter
response on the smallest enclosing rectangle of the domain of the
input image. Therefore, if the domain of the input image only
covers a small fraction of the smallest enclosing rectangle, it can
happen that `median_image` is faster than [`median_rect`](median_rect.md)
even for larger mask heights.

Due to performance reasons, the input *`Image`* is not checked whether
it contains NaNs. Using an input image with NaNs crashes HALCON.

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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte* / int2* / uint2* / int4* / real*) **allowed for compute devices*

Image to be filtered.

**`ImageMedian`** (output_object)  (multichannel-)image(-array) `→` object (byte / int2 / uint2 / int4 / real)

Filtered image.

**`MaskType`** (input_control)  string `→`  (string)

Filter mask type.

Default:
'circle'

List of values:
'circle', 'square'

List of values (for compute devices):
'square'

**`Radius`** (input_control)  integer `→`  (integer)

Radius of the filter mask.

Default:
1

List of values (for compute devices):
1, 2

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 15, 19, 25, 31, 39, 47, 59

Value range:
`1
≤
Radius
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

List of values (for compute devices):
'mirrored'

Suggested values:
'mirrored', 'cyclic', 'continued', 0, 30, 60, 90, 120, 150, 180, 210, 240, 255

## Example (HDevelop)

```
read_image (Image, 'fabrik')
median_image (Image, Median, 'circle', 3, 'continued')
dev_display(Median)
```

## Complexity

For each pixel: O(2 *
*`Radius`* + 1).

## Result

If the parameter values are correct the operator
`median_image` returns the value 2 (
H_MSG_TRUE)
. The behavior in case
of empty input (no input images available) is set via the operator
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Predecessors

`read_image`

## Possible Successors

`threshold`,
`dyn_threshold`,
`regiongrowing`

## Alternatives

`median_rect`,
`rank_image`,
`rank_rect`

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
