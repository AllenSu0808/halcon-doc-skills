# HammingDistance (Operator)

## Name

`HammingDistance` — Hamming distance between two regions.

## Signature

`static void HOperatorSet.HammingDistance(HObject regions1, HObject regions2, out HTuple distance, out HTuple similarity)`

`HTuple HRegion.HammingDistance(HRegion regions2, out HTuple similarity)`

`int HRegion.HammingDistance(HRegion regions2, out double similarity)`

## Description

The operator `HammingDistance` returns the hamming distance
between two regions,
i.e., the number of pixels of the regions which are different
(*`distance`*), i.e., the number of pixels contained in one region
but not in the other:
$$Distance = \left|\text{Regions1} \cap \text{Regions2}\right| + \left|\text{Regions2} \cap \text{Regions1}\right|$$ ![figure](../assets/d9301c68a2aab462.svg)
The parameter *`similarity`* describes the similarity between the
two regions based on the hamming distance *`distance`*:
$$Similarity = 1 - \frac{\text{Distance}}{|\text{Regions1}| + |\text{Regions2}|}$$ ![figure](../assets/f5053ccc76c44b0e.svg)
If both regions are empty *`similarity`* is set to 0.
The regions with the same index from both input parameters are
always compared.

## Attention

In both input parameters the same number of
regions must be passed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions1`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be examined.

**`regions2`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Comparative regions.

**`distance`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Hamming distance of two regions.

Assertion:
`Distance >= 0`

**`similarity`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Similarity of two regions.

Assertion:
`0 <= Similarity && Similarity <= 1`

## Complexity

If F is the area of a region the mean runtime
complexity is O(sqrt(F)).

## Result

hamming_distance returns the value 2 (
H_MSG_TRUE)
if the number of objects in
both parameters is the same and is not 0.
The behavior in case of empty input (no input objects available) is
set via the operator `set_system('no_object_result',<Result>)`.
The behavior in case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`

## Alternatives

`Intersection`,
`Complement`,
`AreaCenter`

## See also

`HammingChangeRegion`

## Module

Foundation
