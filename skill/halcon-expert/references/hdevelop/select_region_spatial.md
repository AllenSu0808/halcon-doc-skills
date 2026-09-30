# select_region_spatial (Operator)

## Name

`select_region_spatial` — Pose relation of regions.

## Signature

`select_region_spatial(Regions1, Regions2 : : Direction : RegionIndex1, RegionIndex2)`

## Description

The operator `select_region_spatial` chooses the regions from *`Regions2`*
which are sufficient for the neighboring relation *`Direction`*.
The regions to be examined have to be passed in *`Regions1`* or
*`Regions2`*, respectively. *`Regions1`* can have
three different states:

- *`Regions1`* is empty:

  In this case all regions in *`Regions2`*
  are permutatively checked for neighborhood.
- *`Regions1`* consists of one region:

  The regions of *`Regions1`* are compared to all regions
  in *`Regions2`*.
- *`Regions1`* consists of the same number of regions
  as *`Regions2`*:

  The regions at the n-th position in
  *`Regions1`* and *`Regions2`* are each
  checked for a neighboring relation.

Possible values for *`Direction`* are:

- ***'left'*:** —

  *`Regions2`* is left of
  *`Regions1`*
- ***'right'*:** —

  *`Regions2`* is right of
  *`Regions1`*
- ***'above'*:** —

  *`Regions2`* is above
  *`Regions1`*
- ***'below'*:** —

  *`Regions2`* is below
  *`Regions1`*

The operator `select_region_spatial` calculates the centers of the regions to be
compared and decides according to the angle between the center straight lines
and the x axis whether the direction relation is fulfilled.
The relation is fulfilled within the area of -45 degree to +45 degree
around the coordinate axes.
Thus, the direction relation can be understood in such a way that the center
of the second region must be located left (or right, above, below) of
the center of the first region.
The indices of the regions fulfilling the direction relation are located
at the n-th position in *`RegionIndex1`* and *`RegionIndex2`*,
i.e., the region with the index *`RegionIndex2`*[n] has the indicated
relation with the region with the index *`RegionIndex1`*[n].
Access to regions via the index can be obtained via the operator
[`copy_obj`](copy_obj.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Regions1`** (input_object)  region(-array) `→` object

Starting regions

**`Regions2`** (input_object)  region(-array) `→` object

Comparative regions

**`Direction`** (input_control)  string `→`  (string)

Desired neighboring relation.

Default:
'left'

List of values:
'above', 'below', 'left', 'right'

**`RegionIndex1`** (output_control)  integer-array `→`  (integer)

Indices in the input tuples (*`Regions1`* or
*`Regions2`*), respectively.

**`RegionIndex2`** (output_control)  integer-array `→`  (integer)

Indices in the input tuples (*`Regions1`* or
*`Regions2`*), respectively.

## Result

The operator `select_region_spatial` returns the value 2 (
H_MSG_TRUE)
if
*`Regions2`* is not empty. The behavior
in case of empty parameter *`Regions2`* (no input regions available)
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
