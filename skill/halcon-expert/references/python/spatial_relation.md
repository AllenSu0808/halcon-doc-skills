# spatial_relation (Operator)

## Name

`spatial_relation` — Pose relation of regions with regard to the coordinate axes.

## Signature

`def spatial_relation(regions_1: HObject, regions_2: HObject, percent: int) -> Tuple[Sequence[int], Sequence[int], Sequence[str], Sequence[str]]`

## Description

The operator `spatial_relation` selects regions located by
*`percent`* percent “left”, “right”, “above” or “below”
other regions.
*`regions_1`* and *`regions_2`* contain the regions
to be compared.
*`regions_1`* can have three states:

- *`regions_1`* contains an empty object tuple,
  i.e., [`count_obj`](count_obj.md) returns *0*:

  In this case all regions in *`regions_2`*
  are permutatively checked for neighborhood.
- *`regions_1`* consists of one region:

  The regions of *`regions_1`* are compared to all regions
  in *`regions_2`*.
- *`regions_1`* consists of the same number of regions
  as *`regions_2`*:

  *`regions_1`* and *`regions_2`* are checked
  for a neighboring relation.

The percentage *`percent`* is interpreted in such a way that
the area of the second region has to be located really left/right
or above/below the region margins of the first region by at least
*`percent`* percent.
The indices of the regions that fulfill at least one of these
conditions are then located at the n-th position in the output parameters
*`region_index_1`* and *`region_index_2`*.
Additionally the output parameters *`relation_1`* and
*`relation_2`* contain at the n-th position the type of relation of the
region pair (*`region_index_1`*[n], *`region_index_2`*[n]),
i.e., region with index *`region_index_2`*[n] has the relation
*`relation_1`*[n] and *`relation_2`*[n] with region with
index *`region_index_1`*[n].

Possible values for *`relation_1`* and *`relation_2`* are:

- *`relation_1`*: *"above"*, *"below"* or *""*
- *`relation_2`*: *"left"*, *"right"* or *""*

In *`region_index_1`* and *`region_index_2`* the indices of the
regions in the tuples of the input regions (*`regions_1`* or
*`regions_2`*), respectively, are entered as image identifiers.
Access to chosen regions via the index can be obtained by the operator
[`copy_obj`](copy_obj.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions_1`** (input_object)  region(-array) `→` HObject

Starting regions.

**`regions_2`** (input_object)  region(-array) `→` HObject

Comparative regions.

**`percent`** (input_control)  integer `→` int

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

**`region_index_1`** (output_control)  integer-array `→` Sequence[int]

Indices of the regions in the tuple of the input
regions which fulfill the pose relation.

**`region_index_2`** (output_control)  integer-array `→` Sequence[int]

Indices of the regions in the tuple of the input regions
which fulfill the pose relation.

**`relation_1`** (output_control)  string-array `→` Sequence[str]

Vertical pose relation in which
*`region_index_2`*[n] stands with
*`region_index_1`*[n].

**`relation_2`** (output_control)  string-array `→` Sequence[str]

Horizontal pose relation in which *`region_index_2`*[n]
stands with *`region_index_1`*[n].

## Result

The operator `spatial_relation` returns the value 2 (
H_MSG_TRUE)
if
*`regions_2`* is not empty and *`percent`* is correctly
chosen. The behavior in case of empty parameter *`regions_2`*
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
