# skeleton (Operator)

## Name

`skeleton` — Compute the skeleton of a region.

## Signature

`skeleton(Region : Skeleton : : )`

## Description

`skeleton` computes the skeleton, i.e., the medial axis of the input
regions. The skeleton is constructed in a way that each point on it
can be seen as the center point of a circle with the largest radius possible
while still being completely contained in the region.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

This operator supports canceling timeouts and interrupts.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Region to be thinned.

**`Skeleton`** (output_object)  region(-array) `→` object

Resulting skeleton.

Number of elements:
Skeleton == Region

## Complexity

Let F be the area of the enclosing rectangle of the input region.
Then the runtime complexity is O(F) (per region).

## Result

`skeleton` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
The behavior in case of empty input (no regions given) can be set
via `set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`sobel_amp`,
`edges_image`,
`bandpass_image`,
`threshold`,
`hysteresis_threshold`

## Possible Successors

`junctions_skeleton`,
`pruning`

## Alternatives

`morph_skeleton`,
`thinning`

## See also

`gray_skeleton`,
`sobel_amp`,
`edges_image`,
`roberts`,
`bandpass_image`,
`threshold`

## References

Eckardt, U. “Verdünnung mit Perfekten Punkten”,
Proceedings 10. DAGM-Symposium, IFB 180, Zurich, 1988

## Module

Foundation
