# tuple_atanh (Operator)

## Name

`tuple_atanh` — Compute the inverse hyperbolic tangent of a tuple.

## Signature

`tuple_atanh( : : T : Atanh)`

## Description

`tuple_atanh` computes the inverse hyperbolic tangent of the
input tuple *`T`*. The inverse hyperbolic tangent is always
returned as a floating point number in *`Atanh`*. The inverse
hyperbolic tangent of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_atanh`,
which can be used in an expression in the following syntax:

[`Atanh := atanh(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  number(-array) `→`  (real / integer)

Input tuple.

**`Atanh`** (output_control)  number(-array) `→`  (real)

Inverse hyperbolic tangent of the input tuple.

## Alternatives

`tuple_asinh`,
`tuple_acosh`

## See also

`tuple_tanh`,
`tuple_tan`,
`tuple_atan`,
`tuple_atan2`

## Module

Foundation
