# TupleIsStringElem (Operator)

## Name

`TupleIsStringElem` — Test whether the types of the elements of a tuple are of type
`string`.

## Signature

`static void HOperatorSet.TupleIsStringElem(HTuple t, out HTuple isString)`

`HTuple HTuple.TupleIsStringElem()`

## Description

`TupleIsStringElem` tests the elements of the input tuple *`t`*
separately.
For all elements of type `string` the value *1* (true) is
returned in *`isString`*, else *0* (false) is returned.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleIsStringElem`,
which can be used in an expression in the following syntax:

[`IsString := is_string_elem(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long / HHandle)

Input tuple.

**`isString`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long)

Are the elements of the input tuple of type `string`?

## Example (HDevelop)

```
tuple_is_string_elem ([3.1416,'pi',3], IsString)
* IsString = [false, true, false]
```

## Result

If the parameters are valid, the operator
`TupleIsStringElem` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`TupleType`,
`TupleTypeElem`,
`TupleIsString`

## See also

`TupleIsMixed`,
`TupleIsInt`,
`TupleIsReal`,
`TupleIsString`,
`TupleIsMixed`,
`TupleIsIntElem`,
`TupleIsRealElem`,
`TupleIsNumber`,
`TupleIsHandleElem`,
`TupleIsHandle`

## Module

Foundation
