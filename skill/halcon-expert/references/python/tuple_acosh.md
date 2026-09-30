# tuple_acosh (Operator)

## Name

`tuple_acosh` — Compute the inverse hyperbolic cosine of a tuple.

## Signature

`def tuple_acosh(t: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_acosh_s(t: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_acosh` computes the inverse hyperbolic cosine of the
input tuple *`t`*. The inverse hyperbolic cosine is always
returned as a floating point number in *`acosh`*. The inverse
hyperbolic cosine of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_acosh`,
which can be used in an expression in the following syntax:

[`Acosh := acosh(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`acosh`** (output_control)  number(-array) `→` Sequence[float]

Inverse hyperbolic cosine of the input tuple.

## Alternatives

`tuple_asinh`,
`tuple_atanh`

## See also

`tuple_cosh`,
`tuple_cos`,
`tuple_acos`

## Module

Foundation
