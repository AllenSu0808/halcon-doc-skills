# symm_difference (Operator)

## Name

`symm_difference` — Calculate the symmetric difference of two regions.

## Signature

`def symm_difference(region_1: HObject, region_2: HObject) -> HObject`

## Description

`symm_difference` calculates the symmetric difference of two
regions. Note that, internally, all regions of *`region_2`* are united to
a single region before the symmetric differences between the individual regions of
*`region_1`* and the united region are calculated.
Two possible definitions of the symmetric difference can
be seen in the example below. A third definition is to regard the
exclusive or of the two regions.

## Attention

Empty regions are valid for both parameters. On output, empty
regions may result. The value of the system flag
*"store_empty_region"* determines the behavior in this
case.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region_1`** (input_object)  region(-array) `→` HObject

Input region 1.

**`region_2`** (input_object)  region(-array) `→` HObject

Input region 2.

**`region_difference`** (output_object)  region(-array) `→` HObject

Resulting region.

## Example (HDevelop)

```
* Simulate the symmetric difference of Region1 and Region2 with
* difference and union:
difference(Region1, Region2, Diff1)
difference(Region2, Region1, Diff2)
union2(Diff1, Diff2, Difference)

* Simulate the symmetric difference of Region1 and Region2 with
* union, intersection, and difference:
union2(Region1, Region2, Union)
intersection(Region1, Region2, Intersection)
difference(Union, Intersection, Difference)
```

## Result

`symm_difference` always returns the value 2 (
H_MSG_TRUE)
. The behavior
in case of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)` and the behavior in
case of an empty input region via
`set_system('empty_region_result',<Result>)`. If necessary,
an exception is raised.

## Possible Successors

`select_shape`,
`disp_region`

## See also

`intersection`,
`union1`,
`union2`,
`complement`,
`difference`

## Module

Foundation
