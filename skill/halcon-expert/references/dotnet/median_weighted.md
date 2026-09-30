# MedianWeighted (Operator)

## Name

`MedianWeighted` — Weighted median filtering with different rank masks.

## Signature

`static void HOperatorSet.MedianWeighted(HObject image, out HObject imageWMedian, HTuple maskType, HTuple maskSize)`

`HImage HImage.MedianWeighted(string maskType, int maskSize)`

## Description

The operator `MedianWeighted` calculates the median of
the gray values within a local environment. In contrast to
[`MedianImage`](median_image.md), which uses all gray values within the
environment exactly once, the operator `MedianWeighted`
weights all gray values several times depending on their position.
A gray value is received into the field to be sorted several times
according to its weighting. The following masks are available:

- **'gauss'** —

  (*`maskSize`* = 3)
  1 2 1
  2 4 2
  1 2 1
- **'inner'** —

  (*`maskSize`* = 3)
  1 1 1
  1 3 1
  1 1 1

The operator `MedianWeighted` means that, contrary to
[`MedianImage`](median_image.md), gray value corners remain.

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
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2)

Image to be filtered.

**`imageWMedian`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2)

Median filtered image.

**`maskType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of median mask.

Default:
"inner"

List of values:
"gauss", "inner"

**`maskSize`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

mask size.

Default:
3

List of values:
3

## Example (HDevelop)

```
read_image(Image,'fabrik')
median_weighted(Image,MedianWeighted,'gauss',3)
dev_display(MedianWeighted)
```

## Complexity

For each pixel: O(F * log(F)) with F = area of *`maskType`*.

## Possible Predecessors

`ReadImage`

## Possible Successors

`Threshold`,
`DynThreshold`,
`Regiongrowing`

## Alternatives

`MedianImage`,
`TrimmedMean`,
`SigmaImage`

## References

R. Haralick, L. Shapiro; “Computer and Robot Vision”;
Addison-Wesley, 1992, Seite 319

## Module

Foundation
