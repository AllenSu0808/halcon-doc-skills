# Union2 (Operator)

## Name

`Union2` — Return the union of two regions.

## Signature

`static void HOperatorSet.Union2(HObject region1, HObject region2, out HObject regionUnion)`

`HRegion HRegion.Union2(HRegion region2)`

## Description

`Union2` computes the union of the region in
*`region1`* with all regions in *`region2`*.
Internally, all regions of *`region2`* are united to
a single region before the individual regions of
*`region1`* are united with the already united region. This
means that `Union2` is not commutative!

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region1`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region for which the union with all regions in Region2
is to be computed.

**`region2`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions which should be added to Region1.

**`regionUnion`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Resulting regions.

Number of elements:
RegionUnion == Region1

## Complexity

Let F be the sum of all areas of the input regions. Then the
runtime complexity is O(log(sqrt(F)) * sqrt(F)).

## Result

`Union2` always returns 2 (
H_MSG_TRUE)
. The behavior in case of
empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`Threshold`,
`Connection`,
`Regiongrowing`,
`Pouring`

## Possible Successors

`SelectShape`,
`DispRegion`

## Alternatives

`Union1`

## See also

`Intersection`,
`Complement`

## Module

Foundation
