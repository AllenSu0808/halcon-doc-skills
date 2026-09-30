# tuple_cosh (Operator)

## Name

`tuple_cosh` — Compute the hyperbolic cosine of a tuple.

## Signature

`tuple_cosh( : : T : Cosh)`

## Description

`tuple_cosh` computes the hyperbolic cosine of the input tuple
*`T`*. The hyperbolic cosine is always returned as a floating
point number in *`Cosh`*. The hyperbolic cosine of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_cosh`,
which can be used in an expression in the following syntax:

[`Cosh := cosh(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  number(-array) `→`  (real / integer)

Input tuple.

**`Cosh`** (output_control)  number(-array) `→`  (real)

Hyperbolic cosine of the input tuple.

## Alternatives

`tuple_sinh`,
`tuple_tanh`

## See also

`tuple_acosh`,
`tuple_cos`,
`tuple_acos`

## Module

Foundation
