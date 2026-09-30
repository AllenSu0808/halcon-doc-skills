# tuple_cosh (Operator)

## Name

`tuple_cosh` — Compute the hyperbolic cosine of a tuple.

## Signature

`def tuple_cosh(t: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_cosh_s(t: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_cosh` computes the hyperbolic cosine of the input tuple
*`t`*. The hyperbolic cosine is always returned as a floating
point number in *`cosh`*. The hyperbolic cosine of a string is not allowed.

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

**`t`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`cosh`** (output_control)  number(-array) `→` Sequence[float]

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
