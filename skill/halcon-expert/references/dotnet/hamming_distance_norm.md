# HammingDistanceNorm (Operator)

## Name

`HammingDistanceNorm` — Hamming distance between two regions using normalization.

## Signature

`static void HOperatorSet.HammingDistanceNorm(HObject regions1, HObject regions2, HTuple norm, out HTuple distance, out HTuple similarity)`

`HTuple HRegion.HammingDistanceNorm(HRegion regions2, HTuple norm, out HTuple similarity)`

`int HRegion.HammingDistanceNorm(HRegion regions2, string norm, out double similarity)`

## Description

The operator `HammingDistanceNorm` returns the hamming distance
between two regions,
i.e., the number of pixels of the regions which are different
(*`distance`*).
Before calculating the difference the region in
*`regions1`* is normalized onto
the regions in *`regions2`*.
The result is the number of pixels contained in one region
but not in the other:
$$Distance = |Norm(Regions1) ∩ Regions2| + |Regions2 ∩ Norm(Regions1)|$$ ![figure](../assets/96d43c1c4a73db42.svg)
The parameter *`similarity`* describes the similarity between the
two regions based on the hamming distance *`distance`*:
$$Similarity = 1 - \frac{ Distance }{|Norm(Regions1)| + |Regions2|}$$ ![figure](../assets/8eb5a5f530ed2503.svg)

The following types of normalization are available:

- ***"center"*:** —

  The region is moved so that both regions have the save center
  of gravity.

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

**`norm`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Type of normalization.

Default:
"center"

List of values:
"center"

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

hamming_distance_norm returns the value 2 (
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
