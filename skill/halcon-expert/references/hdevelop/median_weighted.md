# median_weighted (Operator)

## Name

`median_weighted` — Weighted median filtering with different rank masks.

## Signature

`median_weighted(Image : ImageWMedian : MaskType, MaskSize : )`

## Description

The operator `median_weighted` calculates the median of
the gray values within a local environment. In contrast to
[`median_image`](median_image.md), which uses all gray values within the
environment exactly once, the operator `median_weighted`
weights all gray values several times depending on their position.
A gray value is received into the field to be sorted several times
according to its weighting. The following masks are available:

- **'gauss'** —

  (*`MaskSize`* = 3)
  1 2 1
  2 4 2
  1 2 1
- **'inner'** —

  (*`MaskSize`* = 3)
  1 1 1
  1 3 1
  1 1 1

The operator `median_weighted` means that, contrary to
[`median_image`](median_image.md), gray value corners remain.

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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / int2 / uint2)

Image to be filtered.

**`ImageWMedian`** (output_object)  (multichannel-)image(-array) `→` object (byte / int2 / uint2)

Median filtered image.

**`MaskType`** (input_control)  string `→`  (string)

Type of median mask.

Default:
'inner'

List of values:
'gauss', 'inner'

**`MaskSize`** (input_control)  integer `→`  (integer)

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

For each pixel: O(F * log(F)) with F = area of *`MaskType`*.

## Possible Predecessors

`read_image`

## Possible Successors

`threshold`,
`dyn_threshold`,
`regiongrowing`

## Alternatives

`median_image`,
`trimmed_mean`,
`sigma_image`

## References

R. Haralick, L. Shapiro; “Computer and Robot Vision”;
Addison-Wesley, 1992, Seite 319

## Module

Foundation
