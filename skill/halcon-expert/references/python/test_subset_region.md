# test_subset_region (Operator)

## Name

`test_subset_region` — Test whether a region is contained in another region.

## Signature

`def test_subset_region(region_1: HObject, region_2: HObject) -> Sequence[int]`

`def test_subset_region_s(region_1: HObject, region_2: HObject) -> int`

## Description

`test_subset_region` tests whether *`region_1`* is a
subset of *`region_2`* and returns the result in
*`is_subset`*. If more than one region should be tested,
*`region_1`* and *`region_2`* must have the same number of
elements. In this case, a tuple that contains as many elements as
*`region_1`* and *`region_2`* is returned in
*`is_subset`*.

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region_1`** (input_object)  region(-array) `→` HObject

Test region.

**`region_2`** (input_object)  region(-array) `→` HObject

Region for comparison.

Number of elements:
Region1 == Region2

**`is_subset`** (output_control)  integer(-array) `→` Sequence[int]

Is *`region_1`* contained in *`region_2`*?

## Result

`test_subset_region` returns the value 2 (
H_MSG_TRUE)
if the parameters
are correct. The behavior in case of empty input (no input objects
available) is set via the operator
`set_system(::'no_object_result',<Result>:)`. If the number
of objects differs an exception is raised.

## Alternatives

`difference`,
`area_center`

## See also

`test_equal_region`,
`compare_obj`

## Module

Foundation
