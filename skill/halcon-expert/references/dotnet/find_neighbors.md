# FindNeighbors (Operator)

## Name

`FindNeighbors` — Search direct neighbors.

## Signature

`static void HOperatorSet.FindNeighbors(HObject regions1, HObject regions2, HTuple maxDistance, out HTuple regionIndex1, out HTuple regionIndex2)`

`HTuple HRegion.FindNeighbors(HRegion regions2, int maxDistance, out HTuple regionIndex2)`

## Description

The operator `FindNeighbors` determines neighboring regions with
*`regions1`* and *`regions2`* containing the regions to be
examined.
*`regions1`* can have three different states:

- *`regions1`* is empty:

  In this case all regions in *`regions2`*
  are permutatively checked for neighborhood.
- *`regions1`* consists of one region:

  The regions of *`regions1`* are compared to all regions
  in *`regions2`*.
- *`regions1`* consists of the same number of regions
  as *`regions2`*:

  Here all regions at the n-th position
  in *`regions1`* and *`regions2`* are
  checked for the neighboring relation.

The operator `FindNeighbors` uses the chessboard distance
between neighboring regions. It can be specified by the
parameter *`maxDistance`*.
Neighboring regions are located at the n-th position in
*`regionIndex1`* and *`regionIndex2`*, i.e.,
the region with index *`regionIndex1`*[n] from *`regions1`* is
the neighbor of the region with index *`regionIndex2`*[n] from
*`regions2`*.

## Attention

Covered regions are not found!

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions1`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Starting regions.

**`regions2`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Comparative regions.

**`maxDistance`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximal distance of regions.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 10, 15, 20, 50

Value range:
`1
≤
maxDistance
≤
255`

Minimum increment:
1

Recommended increment:
1

**`regionIndex1`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Indices of the found regions from *`regions1`*.

**`regionIndex2`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Indices of the found regions from *`regions2`*.

## Result

The operator `FindNeighbors` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`.
The behavior in case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`

## See also

`SpatialRelation`,
`SelectRegionSpatial`,
`ExpandRegion`,
`DistanceTransform`,
`Interjacent`,
`Boundary`

## Module

Foundation
