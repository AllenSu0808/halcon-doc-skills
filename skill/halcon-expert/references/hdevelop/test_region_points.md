# test_region_points (Operator)

## Name

`test_region_points` — Test if points are contained in regions.

## Signature

`test_region_points(Regions : : Row, Column : IsInside)`

## Description

`test_region_points` tests if points (*`Row`*,*`Column`*)
are contained in the regions *`Regions`*.

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple or object array
of length *1* or *N*.
Parameters with length *1* will be repeated internally
such that the number of computed tests is always *N*.

In all cases, for each performed test, *`IsInside`* is set to
TRUE (*1*) if the point is contained in the region and to
FALSE (*0*) otherwise.

If (*`Row`*,*`Column`*) are real-valued, rounding is
performed internally since regions are pixel precise.

## Attention

Test pixels are not contained in an empty region.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Region(s) to be examined.

**`Row`** (input_control)  point.y(-array) `→`  (integer / real)

Row index of the test pixel(s).

Default:
100

**`Column`** (input_control)  point.x(-array) `→`  (integer / real)

Column index of the test pixel(s).

Number of elements:
Row == Column

Default:
100

**`IsInside`** (output_control)  integer(-array) `→`  (integer)

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
