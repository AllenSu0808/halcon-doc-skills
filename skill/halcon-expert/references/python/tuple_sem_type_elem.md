# tuple_sem_type_elem (Operator)

## Name

`tuple_sem_type_elem` — Return the semantic type of the elements of a tuple.

## Signature

`def tuple_sem_type_elem(t: HTupleType) -> Sequence[str]`

`def tuple_sem_type_elem_s(t: HTupleType) -> str`

## Description

`tuple_sem_type_elem` returns the semantic type of each element
of the input tuple *`t`*.
The semantic type is returned as a tuple of string values in the output
parameter *`sem_types`*.

If an element is a valid handle, the corresponding semantic type of
the handle is returned. For an invalid or cleared handle, *"handle"*
is returned.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_sem_type_elem`,
which can be used in an expression in the following syntax:

[`SemTypes := sem_type_elem(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  tuple(-array) `→` HTupleType

Input tuple.

**`sem_types`** (output_control)  string(-array) `→` Sequence[str]

Semantic types of the elements of the input tuple as strings.

## Example (HDevelop)

```
create_matrix (3, 3, 0, MatrixID)
tuple_sem_type_elem ([MatrixID,1,1.0,'HALCON',HNULL], SemTypeElem)
* SemTypeElem == ['matrix','integer','real','string','handle']
```

## Result

If the parameters are valid, the operator
`tuple_sem_type_elem` returns the value 2 (
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
`tuple_is_string_elem`,
`tuple_type_elem`,
`tuple_sem_type`

## See also

`get_obj_class`

## Module

Foundation
