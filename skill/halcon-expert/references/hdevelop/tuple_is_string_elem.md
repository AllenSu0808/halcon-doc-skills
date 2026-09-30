# tuple_is_string_elem (Operator)

## Name

`tuple_is_string_elem` — Test whether the types of the elements of a tuple are of type
`string`.

## Signature

`tuple_is_string_elem( : : T : IsString)`

## Description

`tuple_is_string_elem` tests the elements of the input tuple *`T`*
separately.
For all elements of type `string` the value *1* (true) is
returned in *`IsString`*, else *0* (false) is returned.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_is_string_elem`,
which can be used in an expression in the following syntax:

[`IsString := is_string_elem(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  tuple(-array) `→`  (string / real / integer / handle)

Input tuple.

**`IsString`** (output_control)  number(-array) `→`  (integer)

Are the elements of the input tuple of type `string`?

## Example (HDevelop)

```
tuple_is_string_elem ([3.1416,'pi',3], IsString)
* IsString = [false, true, false]
```

## Result

If the parameters are valid, the operator
`tuple_is_string_elem` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`tuple_type`,
`tuple_type_elem`,
`tuple_is_string`

## See also

`tuple_is_mixed`,
`tuple_is_int`,
`tuple_is_real`,
`tuple_is_string`,
`tuple_is_mixed`,
`tuple_is_int_elem`,
`tuple_is_real_elem`,
`tuple_is_number`,
`tuple_is_handle_elem`,
`tuple_is_handle`

## Module

Foundation
