# tuple_fabs (Operator)

## Name

`tuple_fabs` — Compute the absolute value of a tuple (as floating point numbers).

## Signature

`tuple_fabs( : : T : Abs)`

## Description

`tuple_fabs` computes the absolute value of the input tuple
*`T`*. In contrast to [`tuple_abs`](tuple_abs.md), the absolute value is
always returned as a floating point number by `tuple_fabs`.
The absolute value of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_fabs`,
which can be used in an expression in the following syntax:

[`Abs := fabs(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  number(-array) `→`  (real / integer)

Input tuple.

**`Abs`** (output_control)  number(-array) `→`  (real)

Absolute value of the input tuple.

## Alternatives

`tuple_abs`

## Module

Foundation
