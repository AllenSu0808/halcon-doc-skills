# Intersection (Operator)

## Name

`Intersection` — Calculate the intersection of two regions.

## Signature

`static void HOperatorSet.Intersection(HObject region1, HObject region2, out HObject regionIntersection)`

`HRegion HRegion.Intersection(HRegion region2)`

## Description

`Intersection` calculates the intersection of the regions
in *`region1`* with the regions in *`region2`*. Each
region in *`region1`* is intersected with all regions in
*`region2`*. That is, internally all regions of *`region2`*
are united to a single region before the individual regions of
*`region1`* are intersected with the united region. The order of
regions in *`regionIntersection`* is identical to the order
of regions in *`region1`*.

## Attention

Empty input regions are permitted. Because empty result regions are
possible, the system flag *"store_empty_region"* should be
set appropriately.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region1`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be intersected with all regions in Region2.

**`region2`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions with which Region1 is intersected.

**`regionIntersection`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Result of the intersection.

Number of elements:
RegionIntersection <= Region1

## Complexity

Let N be the number of regions in *`region1`*, $F_{1}$ be
their average area, and $F_{2}$ be the total area of all regions in
*`region2`*. Then the runtime complexity is
$O\bigl(F_{1}\log(F_{1}) + N_{*}\bigl(\sqrt{F_{1}} + \sqrt{F_{2}}\bigr)\bigr)$ ![figure](../assets/c70316753b26a297.svg).

## Result

`Intersection` always returns 2 (
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

## See also

`Union1`,
`Union2`,
`Complement`

## Module

Foundation
