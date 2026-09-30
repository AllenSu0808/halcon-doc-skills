# TestEqualObj (Operator)

## Name

`TestEqualObj` — Compare image objects regarding equality.

## Signature

`static void HOperatorSet.TestEqualObj(HObject objects1, HObject objects2, out HTuple isEqual)`

`int HObject.TestEqualObj(HObject objects2)`

`int HImage.TestEqualObj(HImage objects2)`

`int HRegion.TestEqualObj(HRegion objects2)`

`int HXLD.TestEqualObj(HXLD objects2)`

`int HXLDCont.TestEqualObj(HXLDCont objects2)`

`int HXLDPoly.TestEqualObj(HXLDPoly objects2)`

`int HXLDPara.TestEqualObj(HXLDPara objects2)`

`int HXLDModPara.TestEqualObj(HXLDModPara objects2)`

`int HXLDExtPara.TestEqualObj(HXLDExtPara objects2)`

## Description

The operator `TestEqualObj` compares the regions and gray value
components of all objects of the two input parameters.
The n-th object in *`objects1`* is compared to the n-th
object in *`objects2`* (for all n). If all corresponding
regions are equal and the number of regions is also identical the
parameter *`isEqual`* is set to TRUE, otherwise FALSE.

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
*`isEqual`* is set to TRUE, since all input (= empty set) is equal.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objects1`** (input_object)  object-array `→` [HObject](HObject.md)

Test objects.

**`objects2`** (input_object)  object-array `→` [HObject](HObject.md)

Comparative objects.

**`isEqual`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Boolean result value.

## Complexity

If F is the area of a region the runtime complexity is
O(1) or O(sqrt(F)) if the result is TRUE and
O(sqrt(F)) if the result is FALSE.

## Result

The operator `TestEqualObj` returns the value 2 (
H_MSG_TRUE)
if the parameters are correct.
The behavior in case of empty input (no input objects available) is set via
the operator `set_system(::'no_object_result',<Result>:)`.
If the number of objects differs an exception is raised.
Else `TestEqualObj` returns 2 (
H_MSG_TRUE)

## See also

`CompareObj`,
`TestEqualRegion`

## Module

Foundation
