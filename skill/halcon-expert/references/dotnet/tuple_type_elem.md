# TupleTypeElem (Operator)

## Name

`TupleTypeElem` — Return the types of the elements of a tuple.

## Signature

`static void HOperatorSet.TupleTypeElem(HTuple t, out HTuple types)`

`HTuple HTuple.TupleTypeElem()`

## Description

`TupleTypeElem` returns the types of the elements of the input tuple
*`t`*. The types are returned separately as integer values in the output
parameter *`types`*. In HDevelop the corresponding constants are
defined:

- H_TYPE_INT (1).
- H_TYPE_REAL (2).
- H_TYPE_STRING (4).
- H_TYPE_HANDLE (16).

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleTypeElem`,
which can be used in an expression in the following syntax:

[`Types := type_elem(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string / HHandle)

Input tuple.

**`types`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long)

Types of the elements of the input tuple as integer values.

## Example (HDevelop)

```
tuple_type_elem ([3.1416,'pi',3], Types)
* Types = [H_TYPE_REAL, H_TYPE_STRING, H_TYPE_INT]
```

## Result

If the parameters are valid, the operator
`TupleTypeElem` returns the value 2 (
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
`TupleIsStringElem`

## See also

`GetObjClass`,
`TupleIsNumber`

## Module

Foundation
