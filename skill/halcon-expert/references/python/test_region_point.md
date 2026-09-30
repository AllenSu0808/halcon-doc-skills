# test_region_point (Operator)

## Name

`test_region_point` — Test if the region contains a given point.

## Signature

`def test_region_point(regions: HObject, row: MaybeSequence[Union[int, float]], column: MaybeSequence[Union[int, float]]) -> int`

## Description

If an array of regions and one test point is provided,
`test_region_point` tests if at least one input region of
*`regions`* contains the single test point given in
(*`row`*,*`column`*). If this is the case, *`is_inside`* is
set to TRUE, else to FALSE. Alternatively, if a single region and several
test points are provided, `test_region_point` tests if at least
one of the test points (given in *`row`*,*`column`*) is contained
in the input region given in *`regions`*.
If this is the case, *`is_inside`* is set to TRUE, otherwise it is set
to FALSE. If (*`row`*,*`column`*) are real-valued, rounding is
performed internally since regions are pixel precise.

To test, which points exactly are contained in a region, use the
operator [`test_region_points`](test_region_points.md).

## Attention

The test pixel is not contained in an empty region
(no pixel of the region corresponds to the pixel).
If all regions are empty *`is_inside`* is set to
FALSE.

In case of an empty input object (empty tuple) *`regions`* and
`set_system('no_object_result','true')`, an empty tuple is
returned in *`is_inside`*. If
`set_system('no_object_result','false')` was set, an exception is
raised.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Region(s) to be examined.

**`row`** (input_control)  point.y(-array) `→` MaybeSequence[Union[int, float]]

Row index of the test pixel(s).

Default:
100

**`column`** (input_control)  point.x(-array) `→` MaybeSequence[Union[int, float]]

Column index of the test pixel(s).

Number of elements:
Row == Column

Default:
100

**`is_inside`** (output_control)  integer `→` int

Boolean result value.

## Complexity

If F is the area of one region, N is the number of regions, and M is
the number of test points, the runtime complexity is
O(ln(sqrt(F)) * N) in the case of one test point and several regions and
O(ln(sqrt(F)) * M) in the case of one region and several test points.

## Result

The operator `test_region_point` returns the value 2 (
H_MSG_TRUE)
if the parameters are correct.
The behavior in case of an empty object is
set via the operator `set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`

## Alternatives

`union1`,
`intersection`,
`area_center`,
`test_region_points`

## See also

`select_region_point`,
`test_region_points`

## Module

Foundation
