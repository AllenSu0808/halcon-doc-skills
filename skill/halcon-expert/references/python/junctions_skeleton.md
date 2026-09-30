# junctions_skeleton (Operator)

## Name

`junctions_skeleton` — Find junctions and end points in a skeleton.

## Signature

`def junctions_skeleton(region: HObject) -> Tuple[HObject, HObject]`

## Description

`junctions_skeleton` detects junctions and end points in a skeleton (see
[`skeleton`](skeleton.md)). The junctions in the input region
*`region`* are output as a region in *`junc_points`*,
while the end points are output as a region in *`end_points`*.

To obtain reasonable results with `junctions_skeleton` the input
region *`region`* must not contain lines which are more than one
pixel wide. Regions obtained by [`skeleton`](skeleton.md) meet this condition,
while regions obtained by [`morph_skeleton`](morph_skeleton.md) do not meet this
condition in general.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Input skeletons.

**`end_points`** (output_object)  region(-array) `→` HObject

Extracted end points.

Number of elements:
EndPoints == Region

**`junc_points`** (output_object)  region(-array) `→` HObject

Extracted junctions.

Number of elements:
JuncPoints == Region

## Complexity

Let F be the area of the input region. Then the runtime
complexity is O(F).

## Result

`junctions_skeleton` always returns the value 2 (
H_MSG_TRUE)
. The behavior in
case of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`,
the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`,
and the behavior in case of an empty result region via
`set_system('store_empty_region',<'true'/'false'>)`.
If necessary, an exception is raised.

## Possible Predecessors

`skeleton`

## Possible Successors

`area_center`,
`connection`,
`get_region_points`,
`difference`

## See also

`pruning`,
`split_skeleton_region`

## Module

Foundation
