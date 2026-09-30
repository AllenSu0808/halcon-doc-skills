# Pruning (Operator)

## Name

`Pruning` — Prune the branches of a region.

## Signature

`static void HOperatorSet.Pruning(HObject region, out HObject regionPrune, HTuple length)`

`HRegion HRegion.Pruning(int length)`

## Description

`Pruning` removes branches from a skeleton
(*`region`*) having a length less than *`length`*.
All other branches are preserved.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be processed.

**`regionPrune`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Result of the pruning operation.

**`length`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Length of the branches to be removed.

Default:
2

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 17, 20, 30, 40, 50

Value range:
`1
≤
length
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

## Complexity

Let F be the area of the input region. Then the runtime
complexity for one region is
$$O\left(\text{Length} \cdot 3 \cdot \sqrt{F}\right)$$ ![figure](../assets/59929868bf9b48d0.svg)

## Result

`Pruning` returns 2 (
H_MSG_TRUE)
if all parameters are correct. The
behavior in case of empty or no input region can be set via:

- no region:
  `set_system('no_object_result',<RegionResult>)`
- empty region:
  `set_system('empty_region_result',<RegionResult>)`

Otherwise, an exception is raised.

## Possible Predecessors

`Skeleton`

## Possible Successors

`ReduceDomain`,
`SelectShape`,
`AreaCenter`,
`Connection`

## See also

`JunctionsSkeleton`

## Module

Foundation
