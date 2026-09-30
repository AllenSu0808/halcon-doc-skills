# tuple_round (Operator)

## Name

`tuple_round` — Convert a tuple into a tuple of integer numbers.

## Signature

`tuple_round( : : T : Round)`

## Description

`tuple_round` converts the input tuple *`T`* into a tuple
of integer numbers by rounding *`T`* to the nearest integer.
The conversion of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_round`,
which can be used in an expression in the following syntax:

[`Round := round(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  number(-array) `→`  (real / integer)

Input tuple.

**`Round`** (output_control)  number(-array) `→`  (integer)

Result of the rounding.

## Alternatives

`tuple_int`

## Module

Foundation
