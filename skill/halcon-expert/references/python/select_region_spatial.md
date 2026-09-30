# select_region_spatial (Operator)

## Name

`select_region_spatial` — Pose relation of regions.

## Signature

`def select_region_spatial(regions_1: HObject, regions_2: HObject, direction: str) -> Tuple[Sequence[int], Sequence[int]]`

## Description

The operator `select_region_spatial` chooses the regions from *`regions_2`*
which are sufficient for the neighboring relation *`direction`*.
The regions to be examined have to be passed in *`regions_1`* or
*`regions_2`*, respectively. *`regions_1`* can have
three different states:

- *`regions_1`* is empty:

  In this case all regions in *`regions_2`*
  are permutatively checked for neighborhood.
- *`regions_1`* consists of one region:

  The regions of *`regions_1`* are compared to all regions
  in *`regions_2`*.
- *`regions_1`* consists of the same number of regions
  as *`regions_2`*:

  The regions at the n-th position in
  *`regions_1`* and *`regions_2`* are each
  checked for a neighboring relation.

Possible values for *`direction`* are:

- ***"left"*:** —

  *`regions_2`* is left of
  *`regions_1`*
- ***"right"*:** —

  *`regions_2`* is right of
  *`regions_1`*
- ***"above"*:** —

  *`regions_2`* is above
  *`regions_1`*
- ***"below"*:** —

  *`regions_2`* is below
  *`regions_1`*

The operator `select_region_spatial` calculates the centers of the regions to be
compared and decides according to the angle between the center straight lines
and the x axis whether the direction relation is fulfilled.
The relation is fulfilled within the area of -45 degree to +45 degree
around the coordinate axes.
Thus, the direction relation can be understood in such a way that the center
of the second region must be located left (or right, above, below) of
the center of the first region.
The indices of the regions fulfilling the direction relation are located
at the n-th position in *`region_index_1`* and *`region_index_2`*,
i.e., the region with the index *`region_index_2`*[n] has the indicated
relation with the region with the index *`region_index_1`*[n].
Access to regions via the index can be obtained via the operator
[`copy_obj`](copy_obj.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions_1`** (input_object)  region(-array) `→` HObject

Starting regions

**`regions_2`** (input_object)  region(-array) `→` HObject

Comparative regions

**`direction`** (input_control)  string `→` str

Desired neighboring relation.

Default:
"left"

List of values:
"above", "below", "left", "right"

**`region_index_1`** (output_control)  integer-array `→` Sequence[int]

Indices in the input tuples (*`regions_1`* or
*`regions_2`*), respectively.

**`region_index_2`** (output_control)  integer-array `→` Sequence[int]

Indices in the input tuples (*`regions_1`* or
*`regions_2`*), respectively.

## Result

The operator `select_region_spatial` returns the value 2 (
H_MSG_TRUE)
if
*`regions_2`* is not empty. The behavior
in case of empty parameter *`regions_2`* (no input regions available)
is set via the operator `set_system('no_object_result',<Result>)`.
The behavior in case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`

## Alternatives

`area_center`,
`intersection`

## See also

`spatial_relation`,
`find_neighbors`,
`copy_obj`,
`obj_to_integer`

## Module

Foundation
