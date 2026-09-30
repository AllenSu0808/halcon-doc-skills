# NoiseDistributionMean (Operator)

## Name

`NoiseDistributionMean` — Determine the noise distribution of an image.

## Signature

`static void HOperatorSet.NoiseDistributionMean(HObject constRegion, HObject image, HTuple filterSize, out HTuple distribution)`

`HTuple HImage.NoiseDistributionMean(HRegion constRegion, int filterSize)`

`HTuple HRegion.NoiseDistributionMean(HImage image, int filterSize)`

## Description

`NoiseDistributionMean` calculates the noise
distribution in a region of the image *`image`*. The
parameter *`constRegion`* determines a region of the image
with approximately constant gray values. Ideally, the changes in
gray values should only be caused by noise in this region. From
this region the noise distribution is determined by using the
[`MeanImage`](mean_image.md) operator to smooth the image, and to use the gray
value differences in this area as an estimate for the noise
distribution, which is returned in *`distribution`*.

## Attention

It is important to ensure that the region *`constRegion`* is
not too close to a large gradient in the image, because the gradient
values are then used for calculating the mean. This means the
distance of *`constRegion`* must be at least as large as the
filter size *`filterSize`* used for calculating the mean.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`constRegion`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region from which the noise distribution is to
be estimated.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte)

Corresponding image.

**`filterSize`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Size of the mean filter.

Default:
21

Suggested values:
5, 11, 15, 21, 31, 51, 101

Value range:
`3
≤
filterSize
≤
501` (lin)

Minimum increment:
2

Recommended increment:
2

**`distribution`** (output_control)  distribution.values-array `→` [HTuple](HTuple.md) (*double*)

Noise distribution of all input regions.

## Possible Predecessors

`DrawRegion`,
`GenCircle`,
`GenEllipse`,
`GenRectangle1`,
`GenRectangle2`,
`Threshold`,
`ErosionCircle`,
`BinomialFilter`,
`GaussFilter`,
`SmoothImage`,
`SubImage`

## Possible Successors

`AddNoiseDistribution`

## See also

`MeanImage`,
`GaussDistribution`

## Module

Foundation
