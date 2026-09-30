# union2 (Operator)

## Name

`union2` — Return the union of two regions.

## Signature

`def union2(region_1: HObject, region_2: HObject) -> HObject`

## Description

`union2` computes the union of the region in
*`region_1`* with all regions in *`region_2`*.
Internally, all regions of *`region_2`* are united to
a single region before the individual regions of
*`region_1`* are united with the already united region. This
means that `union2` is not commutative!

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region_1`** (input_object)  region(-array) `→` HObject

Region for which the union with all regions in Region2
is to be computed.

**`region_2`** (input_object)  region(-array) `→` HObject

Regions which should be added to Region1.

**`region_union`** (output_object)  region(-array) `→` HObject

Resulting regions.

Number of elements:
RegionUnion == Region1

## Complexity

Let F be the sum of all areas of the input regions. Then the
runtime complexity is O(log(sqrt(F)) * sqrt(F)).

## Result

`union2` always returns 2 (
H_MSG_TRUE)
. The behavior in case of
empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`threshold`,
`connection`,
`regiongrowing`,
`pouring`

## Possible Successors

`select_shape`,
`disp_region`

## Alternatives

`union1`

## See also

`intersection`,
`complement`

## Module

Foundation
