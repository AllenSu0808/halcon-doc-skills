# select_region_point (Operator)

## Name

`select_region_point` — Choose all regions containing a given pixel.

## Signature

`def select_region_point(regions: HObject, row: int, column: int) -> HObject`

## Description

The operator `select_region_point` selects all regions from *`regions`*
containing the test pixel (*`row`*,*`column`*), i.e.:
$$|\texttt{Regions}[n]\cap\{(\texttt{Row},\texttt{Column})\}|=1$$

## Attention

If the regions overlap more than one region might contain the pixel.
In this case all these regions are returned.
If no region contains the indicated pixel the
empty tuple (= no region) is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region-array `→` HObject

Regions to be examined.

**`dest_regions`** (output_object)  region-array `→` HObject

All regions containing the test pixel.

**`row`** (input_control)  point.y `→` int

Line index of the test pixel.

Default:
100

**`column`** (input_control)  point.x `→` int

Column index of the test pixel.

Default:
100

## Complexity

If F is the area of the region and N is the number of regions, the
mean runtime complexity is O(ln(sqrt(F)) * N).

## Result

The operator `select_region_point` returns the value 2 (
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

`test_region_point`

## See also

`get_mbutton`,
`get_mposition`

## Module

Foundation
