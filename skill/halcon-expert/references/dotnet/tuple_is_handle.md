# TupleIsHandle (Operator)

## Name

`TupleIsHandle` — Test if the internal representation of a tuple is of type `handle`.

## Signature

`static void HOperatorSet.TupleIsHandle(HTuple t, out HTuple isHandle)`

`HTuple HTuple.TupleIsHandle()`

## Description

`TupleIsHandle` tests if the internal representation of the
input tuple *`t`* is of type `handle`. In that case the value
*1* (true) is returned in *`isHandle`*, otherwise the value
*0* (false) is returned. If a tuple consists of `handle`
elements only, *`isHandle`* can nevertheless be 0 in case the internal
representation is H_TYPE_MIXED; see [`TupleType`](tuple_type.md) for details.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns *1*.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleIsHandle`,
which can be used in an expression in the following syntax:

[`IsHandle := is_handle(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Attention

Even if all tuple elements are of type `handle`,
`TupleIsHandle` returns *0* (false) if the internal
representation of the tuple is of type H_TYPE_MIXED. To test if the elements
of the tuple are of type `handle`, the operator
[`TupleIsHandleElem`](tuple_is_handle_elem.md) should be used.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*HHandle* / double / int / long / string)

Input tuple.

**`isHandle`** (output_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Boolean value indicating if the input tuple is of type
`handle`.

## Result

If the parameters are valid, the operator
`TupleIsHandle` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`TupleType`,
`TupleIsNumber`,
`TupleIsHandleElem`,
`TupleIsString`,
`TupleSemType`

## See also

`TupleIsInt`,
`TupleIsReal`,
`TupleIsString`

## Module

Foundation
