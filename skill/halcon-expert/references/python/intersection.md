# intersection (Operator)

## Name

`intersection` — Calculate the intersection of two regions.

## Signature

`def intersection(region_1: HObject, region_2: HObject) -> HObject`

## Description

`intersection` calculates the intersection of the regions
in *`region_1`* with the regions in *`region_2`*. Each
region in *`region_1`* is intersected with all regions in
*`region_2`*. That is, internally all regions of *`region_2`*
are united to a single region before the individual regions of
*`region_1`* are intersected with the united region. The order of
regions in *`region_intersection`* is identical to the order
of regions in *`region_1`*.

## Attention

Empty input regions are permitted. Because empty result regions are
possible, the system flag *"store_empty_region"* should be
set appropriately.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region_1`** (input_object)  region(-array) `→` HObject

Regions to be intersected with all regions in Region2.

**`region_2`** (input_object)  region(-array) `→` HObject

Regions with which Region1 is intersected.

**`region_intersection`** (output_object)  region(-array) `→` HObject

Result of the intersection.

Number of elements:
RegionIntersection <= Region1

## Complexity

Let N be the number of regions in *`region_1`*, $F_{1}$ be
their average area, and $F_{2}$ be the total area of all regions in
*`region_2`*. Then the runtime complexity is
$O\bigl(F_{1}\log(F_{1}) + N_{*}\bigl(\sqrt{F_{1}} + \sqrt{F_{2}}\bigr)\bigr)$ ![figure](../assets/c70316753b26a297.svg).

## Result

`intersection` always returns 2 (
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

## See also

`union1`,
`union2`,
`complement`

## Module

Foundation
