# tuple_type_elem (Operator)

## Name

`tuple_type_elem` — Return the types of the elements of a tuple.

## Signature

`tuple_type_elem( : : T : Types)`

## Description

`tuple_type_elem` returns the types of the elements of the input tuple
*`T`*. The types are returned separately as integer values in the output
parameter *`Types`*. In HDevelop the corresponding constants are
defined:

- H_TYPE_INT (1).
- H_TYPE_REAL (2).
- H_TYPE_STRING (4).
- H_TYPE_HANDLE (16).

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_type_elem`,
which can be used in an expression in the following syntax:

[`Types := type_elem(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  tuple(-array) `→`  (real / integer / string / handle)

Input tuple.

**`Types`** (output_control)  number(-array) `→`  (integer)

Types of the elements of the input tuple as integer values.

## Example (HDevelop)

```
tuple_type_elem ([3.1416,'pi',3], Types)
* Types = [H_TYPE_REAL, H_TYPE_STRING, H_TYPE_INT]
```

## Result

If the parameters are valid, the operator
`tuple_type_elem` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`tuple_type`,
`tuple_is_mixed`,
`tuple_is_int`,
`tuple_is_real`,
`tuple_is_string`,
`tuple_is_mixed`,
`tuple_is_int_elem`,
`tuple_is_real_elem`,
`tuple_is_string_elem`

## See also

`get_obj_class`,
`tuple_is_number`

## Module

Foundation
