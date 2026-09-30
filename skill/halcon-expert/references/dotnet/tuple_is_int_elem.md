# TupleIsIntElem (Operator)

## Name

`TupleIsIntElem` — Test whether the types of the elements of a tuple are of type
`integer`.

## Signature

`static void HOperatorSet.TupleIsIntElem(HTuple t, out HTuple isInt)`

`HTuple HTuple.TupleIsIntElem()`

## Description

`TupleIsIntElem` tests the elements of the input tuple *`t`*
separately.
For all elements of type `integer` the value *1* (true) is returned in
*`isInt`*, else *0* (false) is returned.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleIsIntElem`,
which can be used in an expression in the following syntax:

[`IsInt := is_int_elem(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Attention

`TupleIsIntElem` returns 2 (
H_MSG_TRUE)
if the internal data type
of the elements of the tuple is `integer`. In contrast to
[`TupleIsNumber`](tuple_is_number.md) it does not return whether the elements of a tuple
could be represented as `integer` values.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string / HHandle)

Input tuple.

**`isInt`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long)

Are the elements of the input tuple of type `integer`?

## Example (HDevelop)

```
tuple_is_int_elem ([3.1416,'pi',3,3.0], IsInt)
* IsInt = [false, false, true, false]
```

## Result

If the parameters are valid, the operator
`TupleIsIntElem` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`TupleType`,
`TupleTypeElem`,
`TupleIsInt`

## See also

`TupleIsMixed`,
`TupleIsInt`,
`TupleIsReal`,
`TupleIsString`,
`TupleIsMixed`,
`TupleIsRealElem`,
`TupleIsStringElem`,
`TupleIsNumber`,
`TupleIsHandleElem`,
`TupleIsHandle`

## Module

Foundation
