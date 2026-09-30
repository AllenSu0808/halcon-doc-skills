# TupleIsRealElem (Operator)

## Name

`TupleIsRealElem` — Test whether the types of the elements of a tuple are of type `real`.

## Signature

`static void HOperatorSet.TupleIsRealElem(HTuple t, out HTuple isReal)`

`HTuple HTuple.TupleIsRealElem()`

## Description

`TupleIsRealElem` tests the elements of the input tuple *`t`*
separately.
For all elements of type `real` the value *1* (true) is returned in
*`isReal`*, else *0* (false) is returned.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleIsRealElem`,
which can be used in an expression in the following syntax:

[`IsReal := is_real_elem(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Attention

`TupleIsRealElem` returns 2 (
H_MSG_TRUE)
if the internal data type
of the elements of the tuple is `real`. In contrast to
[`TupleIsNumber`](tuple_is_number.md) it does not return whether the elements of a tuple
could be represented as `real` values.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string / HHandle)

Input tuple.

**`isReal`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long)

Are the elements of the input tuple of type `real`?

## Example (HDevelop)

```
tuple_is_real_elem ([3.1416,'pi',3,3.0], IsReal)
* IsReal = [true, false, false, true]
```

## Result

If the parameters are valid, the operator
`TupleIsRealElem` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`TupleType`,
`TupleTypeElem`,
`TupleIsReal`

## See also

`TupleIsMixed`,
`TupleIsInt`,
`TupleIsReal`,
`TupleIsString`,
`TupleIsMixed`,
`TupleIsIntElem`,
`TupleIsStringElem`,
`TupleIsNumber`,
`TupleIsHandleElem`,
`TupleIsHandle`

## Module

Foundation
