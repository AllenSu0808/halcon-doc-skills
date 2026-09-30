# tuple_tanh (Operator)

## Name

`tuple_tanh` — Compute the hyperbolic tangent of a tuple.

## Signature

`tuple_tanh( : : T : Tanh)`

## Description

`tuple_tanh` computes the hyperbolic tangent of the input
tuple *`T`*. The hyperbolic tangent is always returned as a
floating point number in *`Tanh`*. The hyperbolic tangent of a string
is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_tanh`,
which can be used in an expression in the following syntax:

[`Tanh := tanh(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  number(-array) `→`  (real / integer)

Input tuple.

**`Tanh`** (output_control)  number(-array) `→`  (real)

Hyperbolic tangent of the input tuple.

## Alternatives

`tuple_sinh`,
`tuple_cosh`

## See also

`tuple_atanh`,
`tuple_tan`,
`tuple_atan`,
`tuple_atan2`

## Module

Foundation
