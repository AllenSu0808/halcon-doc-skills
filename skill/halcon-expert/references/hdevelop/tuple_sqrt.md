# tuple_sqrt (Operator)

## Name

`tuple_sqrt` — Compute the square root of a tuple.

## Signature

`tuple_sqrt( : : T : Sqrt)`

## Description

`tuple_sqrt` computes the square root of the input tuple
*`T`*. The square root is always returned as a floating point
number. The square root of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_sqrt`,
which can be used in an expression in the following syntax:

[`Sqrt := sqrt(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  number(-array) `→`  (real / integer)

Input tuple.

Restriction:
`T >= 0`

**`Sqrt`** (output_control)  number(-array) `→`  (real)

Square root of the input tuple.

## Alternatives

`tuple_pow`

## See also

`tuple_cbrt`,
`tuple_hypot`

## Module

Foundation
