# TupleIsNanElem (Operator)

## Name

`TupleIsNanElem` — Check a tuple whether it represents NaNs (Not-a-number).

## Signature

`static void HOperatorSet.TupleIsNanElem(HTuple t, out HTuple isNaN)`

`HTuple HTuple.TupleIsNanElem()`

## Description

`TupleIsNanElem` checks each element of the input tuple
*`t`* whether it represents a NaN. If it does, 1 is
returned for that element, otherwise 0.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleIsNanElem`,
which can be used in an expression in the following syntax:

[`IsNaN := is_nan_elem(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`isNaN`** (output_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Tuple with Boolean numbers.

## Alternatives

`TupleType`,
`TupleIsNumber`,
`TupleSemType`

## See also

`TupleIsInt`,
`TupleIsReal`,
`TupleIsString`

## Module

Foundation
