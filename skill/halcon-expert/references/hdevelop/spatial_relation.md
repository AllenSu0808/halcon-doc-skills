# spatial_relation (Operator)

## Name

`spatial_relation` — Pose relation of regions with regard to the coordinate axes.

## Signature

`spatial_relation(Regions1, Regions2 : : Percent : RegionIndex1, RegionIndex2, Relation1, Relation2)`

## Description

The operator `spatial_relation` selects regions located by
*`Percent`* percent “left”, “right”, “above” or “below”
other regions.
*`Regions1`* and *`Regions2`* contain the regions
to be compared.
*`Regions1`* can have three states:

- *`Regions1`* contains an empty object tuple,
  i.e., [`count_obj`](count_obj.md) returns *0*:

  In this case all regions in *`Regions2`*
  are permutatively checked for neighborhood.
- *`Regions1`* consists of one region:

  The regions of *`Regions1`* are compared to all regions
  in *`Regions2`*.
- *`Regions1`* consists of the same number of regions
  as *`Regions2`*:

  *`Regions1`* and *`Regions2`* are checked
  for a neighboring relation.

The percentage *`Percent`* is interpreted in such a way that
the area of the second region has to be located really left/right
or above/below the region margins of the first region by at least
*`Percent`* percent.
The indices of the regions that fulfill at least one of these
conditions are then located at the n-th position in the output parameters
*`RegionIndex1`* and *`RegionIndex2`*.
Additionally the output parameters *`Relation1`* and
*`Relation2`* contain at the n-th position the type of relation of the
region pair (*`RegionIndex1`*[n], *`RegionIndex2`*[n]),
i.e., region with index *`RegionIndex2`*[n] has the relation
*`Relation1`*[n] and *`Relation2`*[n] with region with
index *`RegionIndex1`*[n].

Possible values for *`Relation1`* and *`Relation2`* are:

- *`Relation1`*: *'above'*, *'below'* or *''*
- *`Relation2`*: *'left'*, *'right'* or *''*

In *`RegionIndex1`* and *`RegionIndex2`* the indices of the
regions in the tuples of the input regions (*`Regions1`* or
*`Regions2`*), respectively, are entered as image identifiers.
Access to chosen regions via the index can be obtained by the operator
[`copy_obj`](copy_obj.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Regions1`** (input_object)  region(-array) `→` object

Starting regions.

**`Regions2`** (input_object)  region(-array) `→` object

Comparative regions.

**`Percent`** (input_control)  integer `→`  (integer)

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
Percent
≤
100` (lin)

Minimum increment:
1

Recommended increment:
10

**`RegionIndex1`** (output_control)  integer-array `→`  (integer)

Indices of the regions in the tuple of the input
regions which fulfill the pose relation.

**`RegionIndex2`** (output_control)  integer-array `→`  (integer)

Indices of the regions in the tuple of the input regions
which fulfill the pose relation.

**`Relation1`** (output_control)  string-array `→`  (string)

Vertical pose relation in which
*`RegionIndex2`*[n] stands with
*`RegionIndex1`*[n].

**`Relation2`** (output_control)  string-array `→`  (string)

Horizontal pose relation in which *`RegionIndex2`*[n]
stands with *`RegionIndex1`*[n].

## Result

The operator `spatial_relation` returns the value 2 (
H_MSG_TRUE)
if
*`Regions2`* is not empty and *`Percent`* is correctly
chosen. The behavior in case of empty parameter *`Regions2`*
(no input regions available) is set via the operator
`set_system('no_object_result',<Result>)`.
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

`select_region_spatial`,
`find_neighbors`,
`copy_obj`,
`obj_to_integer`

## Module

Foundation
