# tuple_tan (Operator)

## Name

`tuple_tan` — Compute the tangent of a tuple.

## Signature

`def tuple_tan(t: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_tan_s(t: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_tan` computes the tangent of the input tuple *`t`*.
The tangent is always returned as a floating point number in *`tan`*.
The angles in *`t`* are represented in radians. The
tangent of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_tan`,
which can be used in an expression in the following syntax:

[`Tan := tan(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  angle.rad(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`tan`** (output_control)  number(-array) `→` Sequence[float]

Tangent of the input tuple.

## Alternatives

`tuple_sin`,
`tuple_cos`

## See also

`tuple_atan`,
`tuple_atan2`,
`tuple_tanh`,
`tuple_atanh`

## Module

Foundation
