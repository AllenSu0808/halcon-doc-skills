# difference (Operator)

## Name

`difference` — Calculate the difference of two regions.

## Signature

`difference(Region, Sub : RegionDifference : : )`

## Description

`difference` calculates the set-theoretic difference of
two regions:
(Regions in Region) - (Regions in Sub)
The resulting region is defined as the input region
(*`Region`*) with all points from *`Sub`* removed.
Note that, internally, all regions of *`Sub`* are united to
a single region before the differences between the individual regions of
*`Region`* and the united region are calculated.

## Attention

Empty regions are valid for both parameters. On output, empty
regions may result. The value of the system flag
*'store_empty_region'* determines the behavior in this
case.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Regions to be processed.

**`Sub`** (input_object)  region(-array) `→` object

The union of these regions is subtracted from Region.

**`RegionDifference`** (output_object)  region(-array) `→` object

Resulting region.

## Example (HDevelop)

```
* provides the region X without the points in Y
difference(X,Y,RegionDifference)
```

## Complexity

Let $N$ be the number of regions, $F_{1}$ be their average area, and
$F_{2}$ be the total area of all regions in *`Sub`*. Then
the runtime complexity is
$O(F_1 * log(F_1) + N * (\sqrt{F_1} + \sqrt{F_2}))$ ![figure](../assets/fc8d068d51b2ac42.svg).

## Result

`difference` always returns the value 2 (
H_MSG_TRUE)
. The
behavior in case of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`threshold`,
`connection`,
`regiongrowing`,
`pouring`,
`class_ndim_norm`

## Possible Successors

`select_shape`,
`disp_region`

## See also

`intersection`,
`union1`,
`union2`,
`complement`,
`symm_difference`

## Module

Foundation
