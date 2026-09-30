# GetRegionIndex (Operator)

## Name

`GetRegionIndex` — Index of all regions containing a given pixel.

## Signature

`static void HOperatorSet.GetRegionIndex(HObject regions, HTuple row, HTuple column, out HTuple index)`

`HTuple HRegion.GetRegionIndex(int row, int column)`

## Description

The operator `GetRegionIndex` returns the index
of all regions in *`regions`* (range of values: 1 to n)
containing the test pixel (*`row`*,*`column`*), i.e.:
$$\lvert Regions[n] \cap \{(Row,Column)\} \neq \emptyset$$ ![figure](../assets/31de7689f7af6617.svg)
The returned indices can be used, e.g., in [`SelectObj`](select_obj.md) to
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

**`regions`** (input_object)  region-array `→` [HRegion](HRegion.md)

Regions to be examined.

**`row`** (input_control)  point.y `→` [HTuple](HTuple.md) (*int* / long)

Line index of the test pixel.

Default:
100

Value range:
`row` (lin)

**`column`** (input_control)  point.x `→` [HTuple](HTuple.md) (*int* / long)

Column index of the test pixel.

Default:
100

Value range:
`column` (lin)

**`index`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Index of the regions containing the test pixel.

## Complexity

If F is the area of the region and N is the number of regions the
mean runtime complexity is O(ln(sqrt(F)) * N).

## Result

The operator `GetRegionIndex` returns the value 2 (
H_MSG_TRUE)
if the parameters are correct.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`

## Alternatives

`SelectRegionPoint`

## See also

`GetMbutton`,
`GetMposition`,
`TestRegionPoint`

## Module

Foundation
