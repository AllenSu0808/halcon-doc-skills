# TupleIsReal (Operator)

## Name

`TupleIsReal` — Test if the internal representation of a tuple is of type `real`.

## Signature

`static void HOperatorSet.TupleIsReal(HTuple t, out HTuple isReal)`

`HTuple HTuple.TupleIsReal()`

## Description

`TupleIsReal` tests if the internal representation of the
input tuple *`t`* is of type `real`. In that case
the value *1* (true) is returned in *`isReal`*, otherwise the
value *0* (false) is returned. If a tuple consists of `real`
elements only, *`isReal`* can nevertheless be 0 in case the internal
representation is H_TYPE_MIXED; see [`TupleType`](tuple_type.md) for details.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns 1.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleIsReal`,
which can be used in an expression in the following syntax:

[`IsReal := is_real(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Attention

Even if all tuple elements are of type `real`,
`TupleIsReal` returns *0* (false) if the internal representation
of the tuple is of type H_TYPE_MIXED. To test if the elements of the
tuple are of type `real` the operator [`TupleIsRealElem`](tuple_is_real_elem.md)
should be used.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string / HHandle)

Input tuple.

**`isReal`** (output_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Is the input tuple of type `real`?

## Example (HDevelop)

```
tuple_is_real ([3.1416,'pi',3], IsRealA)
* IsRealA = false
tuple_is_real ([1.0,2.0,3.0], IsRealB)
* IsRealB = true
tuple_is_real ([], IsRealC)
* IsRealC = true
```

## Result

If the parameters are valid, the operator
`TupleIsReal` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`TupleType`,
`TupleIsNumber`,
`TupleIsRealElem`

## See also

`TupleIsInt`,
`TupleIsString`,
`TupleIsHandle`

## Module

Foundation
