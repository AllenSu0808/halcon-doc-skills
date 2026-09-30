# TupleRound (Operator)

## Name

`TupleRound` — Convert a tuple into a tuple of integer numbers.

## Signature

`static void HOperatorSet.TupleRound(HTuple t, out HTuple round)`

`HTuple HTuple.TupleRound()`

## Description

`TupleRound` converts the input tuple *`t`* into a tuple
of integer numbers by rounding *`t`* to the nearest integer.
The conversion of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleRound`,
which can be used in an expression in the following syntax:

[`Round := round(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`round`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long)

Result of the rounding.

## Alternatives

`TupleInt`

## Module

Foundation
