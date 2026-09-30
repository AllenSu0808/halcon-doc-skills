# get_region_index (Operator)

## Name

`get_region_index` — Index of all regions containing a given pixel.

## Signature

`def get_region_index(regions: HObject, row: int, column: int) -> Sequence[int]`

`def get_region_index_s(regions: HObject, row: int, column: int) -> int`

## Description

The operator `get_region_index` returns the index
of all regions in *`regions`* (range of values: 1 to n)
containing the test pixel (*`row`*,*`column`*), i.e.:
$$\lvert Regions[n] \cap \{(Row,Column)\} \neq \emptyset$$ ![figure](../assets/31de7689f7af6617.svg)
The returned indices can be used, e.g., in [`select_obj`](select_obj.md) to
select the regions containing the test pixel.

## Attention

If the regions overlap more than one region might contain the pixel.
In this case all these regions are returned.
If no region contains the indicated pixel the
empty tuple (= no region) is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions`** (input_object)  region-array `→` HObject

Regions to be examined.

**`row`** (input_control)  point.y `→` int

Line index of the test pixel.

Default:
100

Value range:
`row` (lin)

**`column`** (input_control)  point.x `→` int

Column index of the test pixel.

Default:
100

Value range:
`column` (lin)

**`index`** (output_control)  integer(-array) `→` Sequence[int]

Index of the regions containing the test pixel.

## Complexity

If F is the area of the region and N is the number of regions the
mean runtime complexity is O(ln(sqrt(F)) * N).

## Result

The operator `get_region_index` returns the value 2 (
H_MSG_TRUE)
if the parameters are correct.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`

## Alternatives

`select_region_point`

## See also

`get_mbutton`,
`get_mposition`,
`test_region_point`

## Module

Foundation
