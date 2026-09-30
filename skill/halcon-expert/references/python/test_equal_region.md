# test_equal_region (Operator)

## Name

`test_equal_region` — Test whether the regions of two objects are identical.

## Signature

`def test_equal_region(regions_1: HObject, regions_2: HObject) -> int`

## Description

The operator `test_equal_region` compares the regions of the
two input parameters. The n-th element in *`regions_1`* is
compared to the n-th object in *`regions_2`* (for all n). If
all regions are equal and the number of regions is identical the
operator *`is_equal`* is set to TRUE, otherwise FALSE.

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions_1`** (input_object)  region(-array) `→` HObject

Test regions.

**`regions_2`** (input_object)  region(-array) `→` HObject

Comparative regions.

Number of elements:
Regions1 == Regions2

**`is_equal`** (output_control)  integer `→` int

Boolean result value.

## Complexity

If F is the area of a region the runtime complexity is
O(1) or O(sqrt(F)) if the result is TRUE,
O(sqrt(F)) if the result is FALSE.

## Result

The operator `test_equal_region` returns the value 2 (
H_MSG_TRUE)
if the parameters are correct.
The behavior in case of empty input (no input objects available) is set via
the operator `set_system(::'no_object_result',<Result>:)`.
If the number of objects differs an exception is raised.
Else `test_equal_region` returns the value 2 (
H_MSG_TRUE)

## Alternatives

`intersection`,
`complement`,
`area_center`

## See also

`test_equal_obj`

## Module

Foundation
