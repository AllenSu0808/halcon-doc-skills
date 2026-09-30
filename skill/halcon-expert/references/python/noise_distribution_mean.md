# noise_distribution_mean (Operator)

## Name

`noise_distribution_mean` — Determine the noise distribution of an image.

## Signature

`def noise_distribution_mean(const_region: HObject, image: HObject, filter_size: int) -> Sequence[float]`

## Description

`noise_distribution_mean` calculates the noise
distribution in a region of the image *`image`*. The
parameter *`const_region`* determines a region of the image
with approximately constant gray values. Ideally, the changes in
gray values should only be caused by noise in this region. From
this region the noise distribution is determined by using the
[`mean_image`](mean_image.md) operator to smooth the image, and to use the gray
value differences in this area as an estimate for the noise
distribution, which is returned in *`distribution`*.

## Attention

It is important to ensure that the region *`const_region`* is
not too close to a large gradient in the image, because the gradient
values are then used for calculating the mean. This means the
distance of *`const_region`* must be at least as large as the
filter size *`filter_size`* used for calculating the mean.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`const_region`** (input_object)  region(-array) `→` HObject

Region from which the noise distribution is to
be estimated.

**`image`** (input_object)  singlechannelimage `→` HObject (byte)

Corresponding image.

**`filter_size`** (input_control)  integer `→` int

Size of the mean filter.

Default:
21

Suggested values:
5, 11, 15, 21, 31, 51, 101

Value range:
`3
≤
filter_size
≤
501` (lin)

Minimum increment:
2

Recommended increment:
2

**`distribution`** (output_control)  distribution.values-array `→` Sequence[float]

Noise distribution of all input regions.

## Possible Predecessors

`draw_region`,
`gen_circle`,
`gen_ellipse`,
`gen_rectangle1`,
`gen_rectangle2`,
`threshold`,
`erosion_circle`,
`binomial_filter`,
`gauss_filter`,
`smooth_image`,
`sub_image`

## Possible Successors

`add_noise_distribution`

## See also

`mean_image`,
`gauss_distribution`

## Module

Foundation
