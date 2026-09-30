# test_region_points (Operator)

## Name

`test_region_points` — Test if points are contained in regions.

## Signature

`def test_region_points(regions: HObject, row: MaybeSequence[Union[int, float]], column: MaybeSequence[Union[int, float]]) -> Sequence[int]`

`def test_region_points_s(regions: HObject, row: MaybeSequence[Union[int, float]], column: MaybeSequence[Union[int, float]]) -> int`

## Description

`test_region_points` tests if points (*`row`*,*`column`*)
are contained in the regions *`regions`*.

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple or object array
of length *1* or *N*.
Parameters with length *1* will be repeated internally
such that the number of computed tests is always *N*.

In all cases, for each performed test, *`is_inside`* is set to
TRUE (*1*) if the point is contained in the region and to
FALSE (*0*) otherwise.

If (*`row`*,*`column`*) are real-valued, rounding is
performed internally since regions are pixel precise.

## Attention

Test pixels are not contained in an empty region.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

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

**`is_inside`** (output_control)  integer(-array) `→` Sequence[int]

Boolean result value.

## Result

The operator `test_region_points` returns the value 2 (
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

`intersection`,
`area_center`,
`test_region_point`

## See also

`select_region_point`,
`test_region_point`

## Module

Foundation
