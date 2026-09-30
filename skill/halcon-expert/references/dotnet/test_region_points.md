# TestRegionPoints (Operator)

## Name

`TestRegionPoints` — Test if points are contained in regions.

## Signature

`static void HOperatorSet.TestRegionPoints(HObject regions, HTuple row, HTuple column, out HTuple isInside)`

`HTuple HRegion.TestRegionPoints(HTuple row, HTuple column)`

`int HRegion.TestRegionPoints(int row, int column)`

## Description

`TestRegionPoints` tests if points (*`row`*,*`column`*)
are contained in the regions *`regions`*.

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple or object array
of length *1* or *N*.
Parameters with length *1* will be repeated internally
such that the number of computed tests is always *N*.

In all cases, for each performed test, *`isInside`* is set to
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

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region(s) to be examined.

**`row`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

Row index of the test pixel(s).

Default:
100

**`column`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

Column index of the test pixel(s).

Number of elements:
Row == Column

Default:
100

**`isInside`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Boolean result value.

## Result

The operator `TestRegionPoints` returns the value 2 (
H_MSG_TRUE)
if the parameters are correct.
The behavior in case of an empty object is
set via the operator `set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`

## Alternatives

`Intersection`,
`AreaCenter`,
`TestRegionPoint`

## See also

`SelectRegionPoint`,
`TestRegionPoint`

## Module

Foundation
