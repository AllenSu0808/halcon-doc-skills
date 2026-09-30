# TupleSemTypeElem (Operator)

## Name

`TupleSemTypeElem` — Return the semantic type of the elements of a tuple.

## Signature

`static void HOperatorSet.TupleSemTypeElem(HTuple t, out HTuple semTypes)`

`HTuple HTuple.TupleSemTypeElem()`

## Description

`TupleSemTypeElem` returns the semantic type of each element
of the input tuple *`t`*.
The semantic type is returned as a tuple of string values in the output
parameter *`semTypes`*.

If an element is a valid handle, the corresponding semantic type of
the handle is returned. For an invalid or cleared handle, *"handle"*
is returned.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleSemTypeElem`,
which can be used in an expression in the following syntax:

[`SemTypes := sem_type_elem(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*HHandle* / double / int / long / string)

Input tuple.

**`semTypes`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Semantic types of the elements of the input tuple as strings.

## Example (HDevelop)

```
create_matrix (3, 3, 0, MatrixID)
tuple_sem_type_elem ([MatrixID,1,1.0,'HALCON',HNULL], SemTypeElem)
* SemTypeElem == ['matrix','integer','real','string','handle']
```

## Result

If the parameters are valid, the operator
`TupleSemTypeElem` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`TupleType`,
`TupleIsMixed`,
`TupleIsInt`,
`TupleIsReal`,
`TupleIsString`,
`TupleIsMixed`,
`TupleIsIntElem`,
`TupleIsRealElem`,
`TupleIsStringElem`,
`TupleTypeElem`,
`TupleSemType`

## See also

`GetObjClass`

## Module

Foundation
