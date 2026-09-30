# tuple_cos (Operator)

## Name

`tuple_cos` — Compute the cosine of a tuple.

## Signature

`def tuple_cos(t: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_cos_s(t: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_cos` computes the cosine of the input tuple *`t`*.
The cosine is always returned as a floating point number in *`cos`*.
The angles in *`t`* are represented in radians. The
cosine of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_cos`,
which can be used in an expression in the following syntax:

[`Cos := cos(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  angle.rad(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`cos`** (output_control)  number(-array) `→` Sequence[float]

Cosine of the input tuple.

## Alternatives

`tuple_sin`,
`tuple_tan`

## See also

`tuple_acos`,
`tuple_cosh`,
`tuple_acosh`

## Module

Foundation
