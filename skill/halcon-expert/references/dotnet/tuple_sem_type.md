# TupleSemType (Operator)

## Name

`TupleSemType` — Return the semantic type of a tuple.

## Signature

`static void HOperatorSet.TupleSemType(HTuple t, out HTuple semType)`

`HTuple HTuple.TupleSemType()`

`string HHandle.TupleSemType()`

## Description

`TupleSemType` returns the semantic type of the input tuple
*`t`*.
The type is returned as a string value in the output parameter
*`semType`*.

If *`t`* contains only valid handles of the same type, the
corresponding semantic type of the handles is returned (e.g.,
*"matrix"*).
If it contains only valid or invalid handles,
or handles of different type, *"handle"* is returned.
If *`t`* contains elements of different types, *"any"* is
returned.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns *"any"*.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleSemType`,
which can be used in an expression in the following syntax:

[`SemType := sem_type(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*HHandle* / double / int / long / string)

Input tuple.

**`semType`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

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
`TupleSemType` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`TupleIsInt`,
`TupleIsNumber`,
`TupleIsReal`,
`TupleIsString`,
`TupleType`

## See also

`GetObjClass`

## Module

Foundation
