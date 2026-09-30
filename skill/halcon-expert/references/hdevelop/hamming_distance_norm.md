# hamming_distance_norm (Operator)

## Name

`hamming_distance_norm` — Hamming distance between two regions using normalization.

## Signature

`hamming_distance_norm(Regions1, Regions2 : : Norm : Distance, Similarity)`

## Description

The operator `hamming_distance_norm` returns the hamming distance
between two regions,
i.e., the number of pixels of the regions which are different
(*`Distance`*).
Before calculating the difference the region in
*`Regions1`* is normalized onto
the regions in *`Regions2`*.
The result is the number of pixels contained in one region
but not in the other:
$$Distance = |Norm(Regions1) ∩ Regions2| + |Regions2 ∩ Norm(Regions1)|$$ ![figure](../assets/96d43c1c4a73db42.svg)
The parameter *`Similarity`* describes the similarity between the
two regions based on the hamming distance *`Distance`*:
$$Similarity = 1 - \frac{ Distance }{|Norm(Regions1)| + |Regions2|}$$ ![figure](../assets/8eb5a5f530ed2503.svg)

The following types of normalization are available:

- ***'center'*:** —

  The region is moved so that both regions have the save center
  of gravity.

If both regions are empty *`Similarity`* is set to 0.
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

**`Regions1`** (input_object)  region(-array) `→` object

Regions to be examined.

**`Regions2`** (input_object)  region(-array) `→` object

Comparative regions.

**`Norm`** (input_control)  string(-array) `→`  (string)

Type of normalization.

Default:
'center'

List of values:
'center'

**`Distance`** (output_control)  integer(-array) `→`  (integer)

Hamming distance of two regions.

Assertion:
`Distance >= 0`

**`Similarity`** (output_control)  real(-array) `→`  (real)

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

`threshold`,
`regiongrowing`,
`connection`

## Alternatives

`intersection`,
`complement`,
`area_center`

## See also

`hamming_change_region`

## Module

Foundation
