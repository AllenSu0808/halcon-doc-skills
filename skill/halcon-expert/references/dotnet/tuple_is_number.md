# TupleIsNumber (Operator)

## Name

`TupleIsNumber` — Check a tuple (of strings) whether it represents numbers.

## Signature

`static void HOperatorSet.TupleIsNumber(HTuple t, out HTuple isNumber)`

`HTuple HTuple.TupleIsNumber()`

## Description

`TupleIsNumber` checks each element of the input tuple
*`t`* whether it represents a number. If the element is a
number (`real` or `integer`), 1 is returned for that element.
If the element is a string, it is checked whether the string represents a
number. If so, 1 is returned, otherwise 0.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleIsNumber`,
which can be used in an expression in the following syntax:

[`IsNumber := is_number(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Input tuple.

**`isNumber`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Tuple with Boolean numbers.

## Alternatives

`TupleIsInt`,
`TupleIsReal`,
`TupleType`,
`TupleIsNanElem`

## See also

`TupleNumber`

## Module

Foundation
