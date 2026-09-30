# test_subset_region (Operator)

## Name

`test_subset_region` — Test whether a region is contained in another region.

## Signature

`test_subset_region(Region1, Region2 : : : IsSubset)`

## Description

`test_subset_region` tests whether *`Region1`* is a
subset of *`Region2`* and returns the result in
*`IsSubset`*. If more than one region should be tested,
*`Region1`* and *`Region2`* must have the same number of
elements. In this case, a tuple that contains as many elements as
*`Region1`* and *`Region2`* is returned in
*`IsSubset`*.

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region1`** (input_object)  region(-array) `→` object

Test region.

**`Region2`** (input_object)  region(-array) `→` object

Region for comparison.

Number of elements:
Region1 == Region2

**`IsSubset`** (output_control)  integer(-array) `→`  (integer)

Is *`Region1`* contained in *`Region2`*?

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
