# tuple_sinh (Operator)

## Name

`tuple_sinh` — Compute the hyperbolic sine of a tuple.

## Signature

`def tuple_sinh(t: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_sinh_s(t: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_sinh` computes the hyperbolic sine of the input tuple
*`t`*. The hyperbolic sine is always returned as a floating
point number in *`sinh`*. The hyperbolic sine of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_sinh`,
which can be used in an expression in the following syntax:

[`Sinh := sinh(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`sinh`** (output_control)  number(-array) `→` Sequence[float]

Hyperbolic sine of the input tuple.

## Alternatives

`tuple_cosh`,
`tuple_tanh`

## See also

`tuple_asinh`,
`tuple_sin`,
`tuple_asin`

## Module

Foundation
