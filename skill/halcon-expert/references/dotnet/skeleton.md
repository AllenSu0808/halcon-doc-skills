# Skeleton (Operator)

## Name

`Skeleton` — Compute the skeleton of a region.

## Signature

`static void HOperatorSet.Skeleton(HObject region, out HObject skeleton)`

`HRegion HRegion.Skeleton()`

## Description

`Skeleton` computes the skeleton, i.e., the medial axis of the input
regions. The skeleton is constructed in a way that each point on it
can be seen as the center point of a circle with the largest radius possible
while still being completely contained in the region.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

This operator supports canceling timeouts and interrupts.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region to be thinned.

**`skeleton`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Resulting skeleton.

Number of elements:
Skeleton == Region

## Complexity

Let F be the area of the enclosing rectangle of the input region.
Then the runtime complexity is O(F) (per region).

## Result

`Skeleton` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
The behavior in case of empty input (no regions given) can be set
via `set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`SobelAmp`,
`EdgesImage`,
`BandpassImage`,
`Threshold`,
`HysteresisThreshold`

## Possible Successors

`JunctionsSkeleton`,
`Pruning`

## Alternatives

`MorphSkeleton`,
`Thinning`

## See also

`GraySkeleton`,
`SobelAmp`,
`EdgesImage`,
`Roberts`,
`BandpassImage`,
`Threshold`

## References

Eckardt, U. “Verdünnung mit Perfekten Punkten”,
Proceedings 10. DAGM-Symposium, IFB 180, Zurich, 1988

## Module

Foundation
