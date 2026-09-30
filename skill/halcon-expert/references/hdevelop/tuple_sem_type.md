# tuple_sem_type (Operator)

## Name

`tuple_sem_type` — Return the semantic type of a tuple.

## Signature

`tuple_sem_type( : : T : SemType)`

## Description

`tuple_sem_type` returns the semantic type of the input tuple
*`T`*.
The type is returned as a string value in the output parameter
*`SemType`*.

If *`T`* contains only valid handles of the same type, the
corresponding semantic type of the handles is returned (e.g.,
*'matrix'*).
If it contains only valid or invalid handles,
or handles of different type, *'handle'* is returned.
If *`T`* contains elements of different types, *'any'* is
returned.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns *'any'*.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_sem_type`,
which can be used in an expression in the following syntax:

[`SemType := sem_type(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  tuple(-array) `→`  (handle / real / integer / string)

Input tuple.

**`SemType`** (output_control)  string `→`  (string)

Semantic type of the input tuple as a string.

## Example (HDevelop)

```
create_matrix (3, 3, 0, MatrixID)
tuple_sem_type (MatrixID, SemType)
* SemType == 'matrix' (Handle of specific type)
clear_handle (MatrixID)
tuple_sem_type (MatrixID, SemType)
* SemType == 'handle' (Cleared handle)
tuple_sem_type ([MatrixID,123], SemType)
* SemType == 'any' (Mixed types)
```

## Result

If the parameters are valid, the operator
`tuple_sem_type` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`tuple_is_int`,
`tuple_is_number`,
`tuple_is_real`,
`tuple_is_string`,
`tuple_type`

## See also

`get_obj_class`

## Module

Foundation
