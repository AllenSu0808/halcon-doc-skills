# ZeroCrossing (Operator)

## Name

`ZeroCrossing` — Extract zero crossings from an image.

## Signature

`static void HOperatorSet.ZeroCrossing(HObject image, out HObject regionCrossing)`

`HRegion HImage.ZeroCrossing()`

## Description

`ZeroCrossing` returns the zero crossings of the input
image as a region. A pixel is accepted as a zero crossing if its
gray value (in *`image`*) is zero, or if at least one of its
neighbors of the 4-neighborhood has a different sign.

This operator is intended to be used after edge operators returning
the second derivative of the image (e.g., [`LaplaceOfGauss`](laplace_of_gauss.md)),
which were possibly followed by a smoothing operator. In this case,
the zero crossings are (candidates for) edges.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (int1 / int2 / int4 / real)

Input image.

**`regionCrossing`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Zero crossings.

## Result

`ZeroCrossing` usually returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`Laplace`,
`LaplaceOfGauss`,
`DerivateGauss`

## Possible Successors

`Connection`,
`Skeleton`,
`Boundary`,
`SelectShape`,
`FillUp`

## Alternatives

`Threshold`,
`DualThreshold`,
`ZeroCrossingSubPix`

## Module

Foundation
