# SymmDifference (Operator)

## Name

`SymmDifference` — Calculate the symmetric difference of two regions.

## Signature

`static void HOperatorSet.SymmDifference(HObject region1, HObject region2, out HObject regionDifference)`

`HRegion HRegion.SymmDifference(HRegion region2)`

## Description

`SymmDifference` calculates the symmetric difference of two
regions. Note that, internally, all regions of *`region2`* are united to
a single region before the symmetric differences between the individual regions of
*`region1`* and the united region are calculated.
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

**`region1`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Input region 1.

**`region2`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Input region 2.

**`regionDifference`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

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

`SymmDifference` always returns the value 2 (
H_MSG_TRUE)
. The behavior
in case of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)` and the behavior in
case of an empty input region via
`set_system('empty_region_result',<Result>)`. If necessary,
an exception is raised.

## Possible Successors

`SelectShape`,
`DispRegion`

## See also

`Intersection`,
`Union1`,
`Union2`,
`Complement`,
`Difference`

## Module

Foundation
