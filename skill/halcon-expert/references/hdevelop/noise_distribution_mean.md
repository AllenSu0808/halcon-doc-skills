# noise_distribution_mean (Operator)

## Name

`noise_distribution_mean` — Determine the noise distribution of an image.

## Signature

`noise_distribution_mean(ConstRegion, Image : : FilterSize : Distribution)`

## Description

`noise_distribution_mean` calculates the noise
distribution in a region of the image *`Image`*. The
parameter *`ConstRegion`* determines a region of the image
with approximately constant gray values. Ideally, the changes in
gray values should only be caused by noise in this region. From
this region the noise distribution is determined by using the
[`mean_image`](mean_image.md) operator to smooth the image, and to use the gray
value differences in this area as an estimate for the noise
distribution, which is returned in *`Distribution`*.

## Attention

It is important to ensure that the region *`ConstRegion`* is
not too close to a large gradient in the image, because the gradient
values are then used for calculating the mean. This means the
distance of *`ConstRegion`* must be at least as large as the
filter size *`FilterSize`* used for calculating the mean.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ConstRegion`** (input_object)  region(-array) `→` object

Region from which the noise distribution is to
be estimated.

**`Image`** (input_object)  singlechannelimage `→` object (byte)

Corresponding image.

**`FilterSize`** (input_control)  integer `→`  (integer)

Size of the mean filter.

Default:
21

Suggested values:
5, 11, 15, 21, 31, 51, 101

Value range:
`3
≤
FilterSize
≤
501` (lin)

Minimum increment:
2

Recommended increment:
2

**`Distribution`** (output_control)  distribution.values-array `→`  (real)

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
