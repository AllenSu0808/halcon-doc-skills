# distance_rr_min_dil (Operator)

## Name

`distance_rr_min_dil` — Minimum distance between two regions with the help of dilation.

## Signature

`distance_rr_min_dil(Regions1, Regions2 : : : MinDistance)`

## Description

The operator `distance_rr_min_dil` calculates the minimum distance
between pairs of regions, by iteratively applying dilations on both regions
until their intersection is non empty. If several regions are passed in
*`Regions1`* and *`Regions2`* the distance between the i-th
elements in each case is calculated. It then forms the i-th entry in the
output parameter *`MinDistance`*. The calculation is carried out
with the help of dilation with the Golay element *'h'* (see
[`dilation_golay`](dilation_golay.md) for further information). The result is:
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

**`Regions1`** (input_object)  region(-array) `→` object

Regions to be examined.

**`Regions2`** (input_object)  region(-array) `→` object

Regions to be examined.

**`MinDistance`** (output_control)  integer(-array) `→`  (integer)

Minimum distances of the regions.

Assertion:
`-1 <= MinDistance`

## Result

The operator `distance_rr_min_dil` returns the value 2 (
H_MSG_TRUE)
if the input is not empty. Otherwise an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`

## Alternatives

`distance_rr_min`,
`dilation1`,
`intersection`

## Module

Foundation
