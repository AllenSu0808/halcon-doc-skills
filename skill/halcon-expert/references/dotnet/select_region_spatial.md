# SelectRegionSpatial (Operator)

## Name

`SelectRegionSpatial` — Pose relation of regions.

## Signature

`static void HOperatorSet.SelectRegionSpatial(HObject regions1, HObject regions2, HTuple direction, out HTuple regionIndex1, out HTuple regionIndex2)`

`HTuple HRegion.SelectRegionSpatial(HRegion regions2, string direction, out HTuple regionIndex2)`

## Description

The operator `SelectRegionSpatial` chooses the regions from *`regions2`*
which are sufficient for the neighboring relation *`direction`*.
The regions to be examined have to be passed in *`regions1`* or
*`regions2`*, respectively. *`regions1`* can have
three different states:

- *`regions1`* is empty:

  In this case all regions in *`regions2`*
  are permutatively checked for neighborhood.
- *`regions1`* consists of one region:

  The regions of *`regions1`* are compared to all regions
  in *`regions2`*.
- *`regions1`* consists of the same number of regions
  as *`regions2`*:

  The regions at the n-th position in
  *`regions1`* and *`regions2`* are each
  checked for a neighboring relation.

Possible values for *`direction`* are:

- ***"left"*:** —

  *`regions2`* is left of
  *`regions1`*
- ***"right"*:** —

  *`regions2`* is right of
  *`regions1`*
- ***"above"*:** —

  *`regions2`* is above
  *`regions1`*
- ***"below"*:** —

  *`regions2`* is below
  *`regions1`*

The operator `SelectRegionSpatial` calculates the centers of the regions to be
compared and decides according to the angle between the center straight lines
and the x axis whether the direction relation is fulfilled.
The relation is fulfilled within the area of -45 degree to +45 degree
around the coordinate axes.
Thus, the direction relation can be understood in such a way that the center
of the second region must be located left (or right, above, below) of
the center of the first region.
The indices of the regions fulfilling the direction relation are located
at the n-th position in *`regionIndex1`* and *`regionIndex2`*,
i.e., the region with the index *`regionIndex2`*[n] has the indicated
relation with the region with the index *`regionIndex1`*[n].
Access to regions via the index can be obtained via the operator
[`CopyObj`](copy_obj.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions1`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Starting regions

**`regions2`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Comparative regions

**`direction`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Desired neighboring relation.

Default:
"left"

List of values:
"above", "below", "left", "right"

**`regionIndex1`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Indices in the input tuples (*`regions1`* or
*`regions2`*), respectively.

**`regionIndex2`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Indices in the input tuples (*`regions1`* or
*`regions2`*), respectively.

## Result

The operator `SelectRegionSpatial` returns the value 2 (
H_MSG_TRUE)
if
*`regions2`* is not empty. The behavior
in case of empty parameter *`regions2`* (no input regions available)
is set via the operator `set_system('no_object_result',<Result>)`.
The behavior in case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`

## Alternatives

`AreaCenter`,
`Intersection`

## See also

`SpatialRelation`,
`FindNeighbors`,
`CopyObj`,
`ObjToInteger`

## Module

Foundation
