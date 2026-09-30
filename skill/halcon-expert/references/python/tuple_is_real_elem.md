# tuple_is_real_elem (Operator)

## Name

`tuple_is_real_elem` — Test whether the types of the elements of a tuple are of type `real`.

## Signature

`def tuple_is_real_elem(t: HTupleType) -> Sequence[int]`

`def tuple_is_real_elem_s(t: HTupleType) -> int`

## Description

`tuple_is_real_elem` tests the elements of the input tuple *`t`*
separately.
For all elements of type `real` the value *1* (true) is returned in
*`is_real`*, else *0* (false) is returned.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_is_real_elem`,
which can be used in an expression in the following syntax:

[`IsReal := is_real_elem(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Attention

`tuple_is_real_elem` returns 2 (
H_MSG_TRUE)
if the internal data type
of the elements of the tuple is `real`. In contrast to
[`tuple_is_number`](tuple_is_number.md) it does not return whether the elements of a tuple
could be represented as `real` values.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  tuple(-array) `→` HTupleType

Input tuple.

**`is_real`** (output_control)  number(-array) `→` Sequence[int]

Are the elements of the input tuple of type `real`?

## Example (HDevelop)

```
tuple_is_real_elem ([3.1416,'pi',3,3.0], IsReal)
* IsReal = [true, false, false, true]
```

## Result

If the parameters are valid, the operator
`tuple_is_real_elem` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`tuple_type`,
`tuple_type_elem`,
`tuple_is_real`

## See also

`tuple_is_mixed`,
`tuple_is_int`,
`tuple_is_real`,
`tuple_is_string`,
`tuple_is_mixed`,
`tuple_is_int_elem`,
`tuple_is_string_elem`,
`tuple_is_number`,
`tuple_is_handle_elem`,
`tuple_is_handle`

## Module

Foundation
