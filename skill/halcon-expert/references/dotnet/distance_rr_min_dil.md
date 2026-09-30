# DistanceRrMinDil (Operator)

## Name

`DistanceRrMinDil` — Minimum distance between two regions with the help of dilation.

## Signature

`static void HOperatorSet.DistanceRrMinDil(HObject regions1, HObject regions2, out HTuple minDistance)`

`HTuple HRegion.DistanceRrMinDil(HRegion regions2)`

## Description

The operator `DistanceRrMinDil` calculates the minimum distance
between pairs of regions, by iteratively applying dilations on both regions
until their intersection is non empty. If several regions are passed in
*`regions1`* and *`regions2`* the distance between the i-th
elements in each case is calculated. It then forms the i-th entry in the
output parameter *`minDistance`*. The calculation is carried out
with the help of dilation with the Golay element *'h'* (see
[`DilationGolay`](dilation_golay.md) for further information). The result is:
$$n_{i}\ast2-1$$ where $n_{i}$ is the number of iterations.
The mask *'h'* has the effect that precisely the maximum metrics are
calculated.

## Attention

Both parameters must contain the same number of regions.
The regions must not be empty.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions1`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be examined.

**`regions2`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be examined.

**`minDistance`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Minimum distances of the regions.

Assertion:
`-1 <= MinDistance`

## Result

The operator `DistanceRrMinDil` returns the value 2 (
H_MSG_TRUE)
if the input is not empty. Otherwise an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`

## Alternatives

`DistanceRrMin`,
`Dilation1`,
`Intersection`

## Module

Foundation
