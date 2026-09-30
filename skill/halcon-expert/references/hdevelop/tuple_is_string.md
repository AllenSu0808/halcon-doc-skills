# tuple_is_string (Operator)

## Name

`tuple_is_string` — Test if the internal representation of a tuple is of type `string`.

## Signature

`tuple_is_string( : : T : IsString)`

## Description

`tuple_is_string` tests if the internal representation of the
input tuple *`T`* is of type `string`. In that case the value
*1* (true) is returned in *`IsString`*, otherwise the value
*0* (false) is returned. If a tuple consists of `string`
elements only, *`IsString`* can nevertheless be 0 in case the internal
representation is H_TYPE_MIXED; see [`tuple_type`](tuple_type.md) for details.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns 1.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_is_string`,
which can be used in an expression in the following syntax:

[`IsString := is_string(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Attention

Even if all tuple elements are of type `string`,
`tuple_is_string` returns *0* (false) if the internal representation
of the tuple is of type H_TYPE_MIXED. To test if the elements of the
tuple are of type `string` the operator [`tuple_is_string_elem`](tuple_is_string_elem.md)
should be used.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  tuple(-array) `→`  (string / real / integer / handle)

Input tuple.

**`IsString`** (output_control)  number `→`  (integer)

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
`tuple_is_string` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`tuple_type`,
`tuple_is_number`,
`tuple_is_string_elem`

## See also

`tuple_is_int`,
`tuple_is_real`,
`tuple_is_handle`

## Module

Foundation
