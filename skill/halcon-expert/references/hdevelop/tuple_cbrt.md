# tuple_cbrt (Operator)

## Name

`tuple_cbrt` — Compute the cube root of a tuple.

## Signature

`tuple_cbrt( : : T : Cbrt)`

## Description

`tuple_cbrt` computes the cube root of the input tuple
*`T`*. The cube root is always returned as a floating point
number. The cube root of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_cbrt`,
which can be used in an expression in the following syntax:

[`Cbrt := cbrt(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  number(-array) `→`  (real / integer)

Input tuple.

**`Cbrt`** (output_control)  number(-array) `→`  (real)

Cube root of the input tuple.

## Alternatives

`tuple_pow`

## See also

`tuple_sqrt`

## Module

Foundation
