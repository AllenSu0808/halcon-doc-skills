# tuple_asinh (Operator)

## Name

`tuple_asinh` — Compute the inverse hyperbolic sine of a tuple.

## Signature

`def tuple_asinh(t: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_asinh_s(t: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_asinh` computes the inverse hyperbolic sine of the
input tuple *`t`*. The inverse hyperbolic sine is always
returned as a floating point number in *`asinh`*. The inverse
hyperbolic sine of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_asinh`,
which can be used in an expression in the following syntax:

[`Asinh := asinh(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`asinh`** (output_control)  number(-array) `→` Sequence[float]

Inverse hyperbolic sine of the input tuple.

## Alternatives

`tuple_acosh`,
`tuple_atanh`

## See also

`tuple_asin`,
`tuple_sin`,
`tuple_asin`

## Module

Foundation
