# find_neighbors (Operator)

## Name

`find_neighbors` — Search direct neighbors.

## Signature

`def find_neighbors(regions_1: HObject, regions_2: HObject, max_distance: int) -> Tuple[Sequence[int], Sequence[int]]`

## Description

The operator `find_neighbors` determines neighboring regions with
*`regions_1`* and *`regions_2`* containing the regions to be
examined.
*`regions_1`* can have three different states:

- *`regions_1`* is empty:

  In this case all regions in *`regions_2`*
  are permutatively checked for neighborhood.
- *`regions_1`* consists of one region:

  The regions of *`regions_1`* are compared to all regions
  in *`regions_2`*.
- *`regions_1`* consists of the same number of regions
  as *`regions_2`*:

  Here all regions at the n-th position
  in *`regions_1`* and *`regions_2`* are
  checked for the neighboring relation.

The operator `find_neighbors` uses the chessboard distance
between neighboring regions. It can be specified by the
parameter *`max_distance`*.
Neighboring regions are located at the n-th position in
*`region_index_1`* and *`region_index_2`*, i.e.,
the region with index *`region_index_1`*[n] from *`regions_1`* is
the neighbor of the region with index *`region_index_2`*[n] from
*`regions_2`*.

## Attention

Covered regions are not found!

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions_1`** (input_object)  region(-array) `→` HObject

Starting regions.

**`regions_2`** (input_object)  region(-array) `→` HObject

Comparative regions.

**`max_distance`** (input_control)  integer `→` int

Maximal distance of regions.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 10, 15, 20, 50

Value range:
`1
≤
max_distance
≤
255`

Minimum increment:
1

Recommended increment:
1

**`region_index_1`** (output_control)  integer-array `→` Sequence[int]

Indices of the found regions from *`regions_1`*.

**`region_index_2`** (output_control)  integer-array `→` Sequence[int]

Indices of the found regions from *`regions_2`*.

## Result

The operator `find_neighbors` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`.
The behavior in case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`

## See also

`spatial_relation`,
`select_region_spatial`,
`expand_region`,
`distance_transform`,
`interjacent`,
`boundary`

## Module

Foundation
