# intersection (Operator)

## Name

`intersection` — Calculate the intersection of two regions.

## Signature

`intersection(Region1, Region2 : RegionIntersection : : )`

## Description

`intersection` calculates the intersection of the regions
in *`Region1`* with the regions in *`Region2`*. Each
region in *`Region1`* is intersected with all regions in
*`Region2`*. That is, internally all regions of *`Region2`*
are united to a single region before the individual regions of
*`Region1`* are intersected with the united region. The order of
regions in *`RegionIntersection`* is identical to the order
of regions in *`Region1`*.

## Attention

Empty input regions are permitted. Because empty result regions are
possible, the system flag *'store_empty_region'* should be
set appropriately.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Region1`** (input_object)  region(-array) `→` object

Regions to be intersected with all regions in Region2.

**`Region2`** (input_object)  region(-array) `→` object

Regions with which Region1 is intersected.

**`RegionIntersection`** (output_object)  region(-array) `→` object

Result of the intersection.

Number of elements:
RegionIntersection <= Region1

## Complexity

Let N be the number of regions in *`Region1`*, $F_{1}$ be
their average area, and $F_{2}$ be the total area of all regions in
*`Region2`*. Then the runtime complexity is
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
