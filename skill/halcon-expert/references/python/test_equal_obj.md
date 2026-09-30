# test_equal_obj (Operator)

## Name

`test_equal_obj` — Compare image objects regarding equality.

## Signature

`def test_equal_obj(objects_1: HObject, objects_2: HObject) -> int`

## Description

The operator `test_equal_obj` compares the regions and gray value
components of all objects of the two input parameters.
The n-th object in *`objects_1`* is compared to the n-th
object in *`objects_2`* (for all n). If all corresponding
regions are equal and the number of regions is also identical the
parameter *`is_equal`* is set to TRUE, otherwise FALSE.

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

## Attention

Image matrices and XLDs are not compared regarding their contents. Thus,
two images or XLDs, respectively, are “equal” if they are located at
the same place in the storage.
By contrast, regions that are not located at the same place in the
storage are compared regarding their actual contents.
If the input parameters are empty and the behavior was set via the operator
`set_system(::'no_object_result','true':)`, the parameter
*`is_equal`* is set to TRUE, since all input (= empty set) is equal.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objects_1`** (input_object)  object-array `→` HObject

Test objects.

**`objects_2`** (input_object)  object-array `→` HObject

Comparative objects.

**`is_equal`** (output_control)  integer `→` int

Boolean result value.

## Complexity

If F is the area of a region the runtime complexity is
O(1) or O(sqrt(F)) if the result is TRUE and
O(sqrt(F)) if the result is FALSE.

## Result

The operator `test_equal_obj` returns the value 2 (
H_MSG_TRUE)
if the parameters are correct.
The behavior in case of empty input (no input objects available) is set via
the operator `set_system(::'no_object_result',<Result>:)`.
If the number of objects differs an exception is raised.
Else `test_equal_obj` returns 2 (
H_MSG_TRUE)

## See also

`compare_obj`,
`test_equal_region`

## Module

Foundation
