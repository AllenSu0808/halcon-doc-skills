# TupleFabs (Operator)

## Name

`TupleFabs` — Compute the absolute value of a tuple (as floating point numbers).

## Signature

`static void HOperatorSet.TupleFabs(HTuple t, out HTuple abs)`

`HTuple HTuple.TupleFabs()`

## Description

`TupleFabs` computes the absolute value of the input tuple
*`t`*. In contrast to [`TupleAbs`](tuple_abs.md), the absolute value is
always returned as a floating point number by `TupleFabs`.
The absolute value of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleFabs`,
which can be used in an expression in the following syntax:

[`Abs := fabs(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`abs`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Absolute value of the input tuple.

## Alternatives

`TupleAbs`

## Module

Foundation
