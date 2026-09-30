# find_neighbors (Operator)

## Name

`find_neighbors` — Search direct neighbors.

## Signature

`find_neighbors(Regions1, Regions2 : : MaxDistance : RegionIndex1, RegionIndex2)`

## Description

The operator `find_neighbors` determines neighboring regions with
*`Regions1`* and *`Regions2`* containing the regions to be
examined.
*`Regions1`* can have three different states:

- *`Regions1`* is empty:

  In this case all regions in *`Regions2`*
  are permutatively checked for neighborhood.
- *`Regions1`* consists of one region:

  The regions of *`Regions1`* are compared to all regions
  in *`Regions2`*.
- *`Regions1`* consists of the same number of regions
  as *`Regions2`*:

  Here all regions at the n-th position
  in *`Regions1`* and *`Regions2`* are
  checked for the neighboring relation.

The operator `find_neighbors` uses the chessboard distance
between neighboring regions. It can be specified by the
parameter *`MaxDistance`*.
Neighboring regions are located at the n-th position in
*`RegionIndex1`* and *`RegionIndex2`*, i.e.,
the region with index *`RegionIndex1`*[n] from *`Regions1`* is
the neighbor of the region with index *`RegionIndex2`*[n] from
*`Regions2`*.

## Attention

Covered regions are not found!

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Regions1`** (input_object)  region(-array) `→` object

Starting regions.

**`Regions2`** (input_object)  region(-array) `→` object

Comparative regions.

**`MaxDistance`** (input_control)  integer `→`  (integer)

Maximal distance of regions.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 10, 15, 20, 50

Value range:
`1
≤
MaxDistance
≤
255`

Minimum increment:
1

Recommended increment:
1

**`RegionIndex1`** (output_control)  integer-array `→`  (integer)

Indices of the found regions from *`Regions1`*.

**`RegionIndex2`** (output_control)  integer-array `→`  (integer)

Indices of the found regions from *`Regions2`*.

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
