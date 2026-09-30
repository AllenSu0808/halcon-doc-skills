# tuple_is_handle_elem (Operator)

## Name

`tuple_is_handle_elem` — Test whether the elements of a tuple are of type `handle`.

## Signature

`tuple_is_handle_elem( : : T : IsHandle)`

## Description

`tuple_is_handle_elem` tests the elements of the input tuple *`T`*
separately.
For all elements of type `handle` the value *1* (true) is returned in
*`IsHandle`*, else *0* (false) is returned.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_is_handle_elem`,
which can be used in an expression in the following syntax:

[`IsHandle := is_handle_elem(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  tuple(-array) `→`  (handle / real / integer / string)

Input tuple.

**`IsHandle`** (output_control)  number(-array) `→`  (integer)

Boolean values indicating if the elements of the input tuple
are of type `handle`.

## Result

If the parameters are valid, the operator
`tuple_is_handle_elem` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`tuple_type`,
`tuple_type_elem`,
`tuple_is_handle`

## See also

`tuple_is_mixed`,
`tuple_is_int`,
`tuple_is_real`,
`tuple_is_string`,
`tuple_is_mixed`,
`tuple_is_int_elem`,
`tuple_is_real_elem`,
`tuple_is_number`,
`tuple_is_handle`

## Module

Foundation
