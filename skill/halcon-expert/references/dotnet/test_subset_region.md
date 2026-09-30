# TestSubsetRegion (Operator)

## Name

`TestSubsetRegion` — Test whether a region is contained in another region.

## Signature

`static void HOperatorSet.TestSubsetRegion(HObject region1, HObject region2, out HTuple isSubset)`

`HTuple HRegion.TestSubsetRegion(HRegion region2)`

## Description

`TestSubsetRegion` tests whether *`region1`* is a
subset of *`region2`* and returns the result in
*`isSubset`*. If more than one region should be tested,
*`region1`* and *`region2`* must have the same number of
elements. In this case, a tuple that contains as many elements as
*`region1`* and *`region2`* is returned in
*`isSubset`*.

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region1`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Test region.

**`region2`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region for comparison.

Number of elements:
Region1 == Region2

**`isSubset`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Is *`region1`* contained in *`region2`*?

## Result

`TestSubsetRegion` returns the value 2 (
H_MSG_TRUE)
if the parameters
are correct. The behavior in case of empty input (no input objects
available) is set via the operator
`set_system(::'no_object_result',<Result>:)`. If the number
of objects differs an exception is raised.

## Alternatives

`Difference`,
`AreaCenter`

## See also

`TestEqualRegion`,
`CompareObj`

## Module

Foundation
