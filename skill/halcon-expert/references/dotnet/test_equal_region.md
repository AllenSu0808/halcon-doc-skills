# TestEqualRegion (Operator)

## Name

`TestEqualRegion` — Test whether the regions of two objects are identical.

## Signature

`static void HOperatorSet.TestEqualRegion(HObject regions1, HObject regions2, out HTuple isEqual)`

`int HRegion.TestEqualRegion(HRegion regions2)`

## Description

The operator `TestEqualRegion` compares the regions of the
two input parameters. The n-th element in *`regions1`* is
compared to the n-th object in *`regions2`* (for all n). If
all regions are equal and the number of regions is identical the
operator *`isEqual`* is set to TRUE, otherwise FALSE.

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions1`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Test regions.

**`regions2`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Comparative regions.

Number of elements:
Regions1 == Regions2

**`isEqual`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Boolean result value.

## Complexity

If F is the area of a region the runtime complexity is
O(1) or O(sqrt(F)) if the result is TRUE,
O(sqrt(F)) if the result is FALSE.

## Result

The operator `TestEqualRegion` returns the value 2 (
H_MSG_TRUE)
if the parameters are correct.
The behavior in case of empty input (no input objects available) is set via
the operator `set_system(::'no_object_result',<Result>:)`.
If the number of objects differs an exception is raised.
Else `TestEqualRegion` returns the value 2 (
H_MSG_TRUE)

## Alternatives

`Intersection`,
`Complement`,
`AreaCenter`

## See also

`TestEqualObj`

## Module

Foundation
