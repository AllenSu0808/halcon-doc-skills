# Difference (Operator)

## Name

`Difference` — Calculate the difference of two regions.

## Signature

`static void HOperatorSet.Difference(HObject region, HObject sub, out HObject regionDifference)`

`HRegion HRegion.Difference(HRegion sub)`

## Description

`Difference` calculates the set-theoretic difference of
two regions:
(Regions in Region) - (Regions in Sub)
The resulting region is defined as the input region
(*`region`*) with all points from *`sub`* removed.
Note that, internally, all regions of *`sub`* are united to
a single region before the differences between the individual regions of
*`region`* and the united region are calculated.

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

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be processed.

**`sub`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

The union of these regions is subtracted from Region.

**`regionDifference`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Resulting region.

## Example (HDevelop)

```
* provides the region X without the points in Y
difference(X,Y,RegionDifference)
```

## Complexity

Let $N$ be the number of regions, $F_{1}$ be their average area, and
$F_{2}$ be the total area of all regions in *`sub`*. Then
the runtime complexity is
$O(F_1 * log(F_1) + N * (\sqrt{F_1} + \sqrt{F_2}))$ ![figure](../assets/fc8d068d51b2ac42.svg).

## Result

`Difference` always returns the value 2 (
H_MSG_TRUE)
. The
behavior in case of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`Threshold`,
`Connection`,
`Regiongrowing`,
`Pouring`,
`ClassNdimNorm`

## Possible Successors

`SelectShape`,
`DispRegion`

## See also

`Intersection`,
`Union1`,
`Union2`,
`Complement`,
`SymmDifference`

## Module

Foundation
