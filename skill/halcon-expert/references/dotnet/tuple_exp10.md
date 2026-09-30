# TupleExp10 (Operator)

## Name

`TupleExp10` — Compute the base 10 exponential of a tuple.

## Signature

`static void HOperatorSet.TupleExp10(HTuple t, out HTuple exp)`

`HTuple HTuple.TupleExp10()`

## Description

`TupleExp10` computes the base 10 exponential of the input
tuple *`t`*. The exponential is always returned as a floating
point number. The exponential of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleExp10`,
which can be used in an expression in the following syntax:

[`Exp := exp10(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_exponential_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`exp`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Base 10 exponential of the input tuple.

## Alternatives

`TupleExp`,
`TupleExp2`,
`TuplePow`

## See also

`TupleLog`,
`TupleLog2`,
`TupleLog10`

## Module

Foundation
