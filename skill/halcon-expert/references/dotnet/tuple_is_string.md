# TupleIsString (Operator)

## Name

`TupleIsString` — Test if the internal representation of a tuple is of type `string`.

## Signature

`static void HOperatorSet.TupleIsString(HTuple t, out HTuple isString)`

`HTuple HTuple.TupleIsString()`

## Description

`TupleIsString` tests if the internal representation of the
input tuple *`t`* is of type `string`. In that case the value
*1* (true) is returned in *`isString`*, otherwise the value
*0* (false) is returned. If a tuple consists of `string`
elements only, *`isString`* can nevertheless be 0 in case the internal
representation is H_TYPE_MIXED; see [`TupleType`](tuple_type.md) for details.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns 1.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleIsString`,
which can be used in an expression in the following syntax:

[`IsString := is_string(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Attention

Even if all tuple elements are of type `string`,
`TupleIsString` returns *0* (false) if the internal representation
of the tuple is of type H_TYPE_MIXED. To test if the elements of the
tuple are of type `string` the operator [`TupleIsStringElem`](tuple_is_string_elem.md)
should be used.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long / HHandle)

Input tuple.

**`isString`** (output_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Is the input tuple of type `string`?

## Example (HDevelop)

```
tuple_is_string ([3.1416,'pi',3], IsStringA)
* IsStringA = false
tuple_is_string (['a','b','111'], IsStringB)
* IsStringB = true
tuple_is_string ([], IsStringC)
* IsStringC = true
```

## Result

If the parameters are valid, the operator
`TupleIsString` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`TupleType`,
`TupleIsNumber`,
`TupleIsStringElem`

## See also

`TupleIsInt`,
`TupleIsReal`,
`TupleIsHandle`

## Module

Foundation
