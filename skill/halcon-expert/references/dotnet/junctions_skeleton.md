# JunctionsSkeleton (Operator)

## Name

`JunctionsSkeleton` — Find junctions and end points in a skeleton.

## Signature

`static void HOperatorSet.JunctionsSkeleton(HObject region, out HObject endPoints, out HObject juncPoints)`

`HRegion HRegion.JunctionsSkeleton(out HRegion juncPoints)`

## Description

`JunctionsSkeleton` detects junctions and end points in a skeleton (see
[`Skeleton`](skeleton.md)). The junctions in the input region
*`region`* are output as a region in *`juncPoints`*,
while the end points are output as a region in *`endPoints`*.

To obtain reasonable results with `JunctionsSkeleton` the input
region *`region`* must not contain lines which are more than one
pixel wide. Regions obtained by [`Skeleton`](skeleton.md) meet this condition,
while regions obtained by [`MorphSkeleton`](morph_skeleton.md) do not meet this
condition in general.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Input skeletons.

**`endPoints`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Extracted end points.

Number of elements:
EndPoints == Region

**`juncPoints`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Extracted junctions.

Number of elements:
JuncPoints == Region

## Example (HDevelop)

```
* non-connected branches of a skeleton
skeleton(Region,Skeleton)
junctions_skeleton(Skeleton,EPoints,JPoints)
difference(Skeleton,JPoints,Rows)
set_system('neighborhood',4)
connection(Rows,Parts)
```

## Complexity

Let F be the area of the input region. Then the runtime
complexity is O(F).

## Result

`JunctionsSkeleton` always returns the value 2 (
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

`Skeleton`

## Possible Successors

`AreaCenter`,
`Connection`,
`GetRegionPoints`,
`Difference`

## See also

`Pruning`,
`SplitSkeletonRegion`

## Module

Foundation
