# TupleIsHandleElem (Operator)

## Name

`TupleIsHandleElem` — Test whether the elements of a tuple are of type `handle`.

## Signature

`static void HOperatorSet.TupleIsHandleElem(HTuple t, out HTuple isHandle)`

`HTuple HTuple.TupleIsHandleElem()`

## Description

`TupleIsHandleElem` tests the elements of the input tuple *`t`*
separately.
For all elements of type `handle` the value *1* (true) is returned in
*`isHandle`*, else *0* (false) is returned.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleIsHandleElem`,
which can be used in an expression in the following syntax:

[`IsHandle := is_handle_elem(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*HHandle* / double / int / long / string)

Input tuple.

**`isHandle`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long)

Boolean values indicating if the elements of the input tuple
are of type `handle`.

## Result

If the parameters are valid, the operator
`TupleIsHandleElem` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`TupleType`,
`TupleTypeElem`,
`TupleIsHandle`

## See also

`TupleIsMixed`,
`TupleIsInt`,
`TupleIsReal`,
`TupleIsString`,
`TupleIsMixed`,
`TupleIsIntElem`,
`TupleIsRealElem`,
`TupleIsNumber`,
`TupleIsHandle`

## Module

Foundation
