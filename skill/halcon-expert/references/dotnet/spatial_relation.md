# SpatialRelation (Operator)

## Name

`SpatialRelation` — Pose relation of regions with regard to the coordinate axes.

## Signature

`static void HOperatorSet.SpatialRelation(HObject regions1, HObject regions2, HTuple percent, out HTuple regionIndex1, out HTuple regionIndex2, out HTuple relation1, out HTuple relation2)`

`HTuple HRegion.SpatialRelation(HRegion regions2, int percent, out HTuple regionIndex2, out HTuple relation1, out HTuple relation2)`

## Description

The operator `SpatialRelation` selects regions located by
*`percent`* percent “left”, “right”, “above” or “below”
other regions.
*`regions1`* and *`regions2`* contain the regions
to be compared.
*`regions1`* can have three states:

- *`regions1`* contains an empty object tuple,
  i.e., [`CountObj`](count_obj.md) returns *0*:

  In this case all regions in *`regions2`*
  are permutatively checked for neighborhood.
- *`regions1`* consists of one region:

  The regions of *`regions1`* are compared to all regions
  in *`regions2`*.
- *`regions1`* consists of the same number of regions
  as *`regions2`*:

  *`regions1`* and *`regions2`* are checked
  for a neighboring relation.

The percentage *`percent`* is interpreted in such a way that
the area of the second region has to be located really left/right
or above/below the region margins of the first region by at least
*`percent`* percent.
The indices of the regions that fulfill at least one of these
conditions are then located at the n-th position in the output parameters
*`regionIndex1`* and *`regionIndex2`*.
Additionally the output parameters *`relation1`* and
*`relation2`* contain at the n-th position the type of relation of the
region pair (*`regionIndex1`*[n], *`regionIndex2`*[n]),
i.e., region with index *`regionIndex2`*[n] has the relation
*`relation1`*[n] and *`relation2`*[n] with region with
index *`regionIndex1`*[n].

Possible values for *`relation1`* and *`relation2`* are:

- *`relation1`*: *"above"*, *"below"* or *""*
- *`relation2`*: *"left"*, *"right"* or *""*

In *`regionIndex1`* and *`regionIndex2`* the indices of the
regions in the tuples of the input regions (*`regions1`* or
*`regions2`*), respectively, are entered as image identifiers.
Access to chosen regions via the index can be obtained by the operator
[`CopyObj`](copy_obj.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions1`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Starting regions.

**`regions2`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Comparative regions.

**`percent`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Percentage of the area of the comparative region
which must be located left/right or above/below
the region margins of the starting region.

Default:
50

Suggested values:
0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100

Value range:
`0
≤
percent
≤
100` (lin)

Minimum increment:
1

Recommended increment:
10

**`regionIndex1`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Indices of the regions in the tuple of the input
regions which fulfill the pose relation.

**`regionIndex2`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Indices of the regions in the tuple of the input regions
which fulfill the pose relation.

**`relation1`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Vertical pose relation in which
*`regionIndex2`*[n] stands with
*`regionIndex1`*[n].

**`relation2`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Horizontal pose relation in which *`regionIndex2`*[n]
stands with *`regionIndex1`*[n].

## Result

The operator `SpatialRelation` returns the value 2 (
H_MSG_TRUE)
if
*`regions2`* is not empty and *`percent`* is correctly
chosen. The behavior in case of empty parameter *`regions2`*
(no input regions available) is set via the operator
`set_system('no_object_result',<Result>)`.
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

`SelectRegionSpatial`,
`FindNeighbors`,
`CopyObj`,
`ObjToInteger`

## Module

Foundation
