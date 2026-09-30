# tuple_sin (Operator)

## Name

`tuple_sin` — Compute the sine of a tuple.

## Signature

`def tuple_sin(t: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_sin_s(t: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_sin` computes the sine of the input tuple *`t`*.
The sine is always returned as a floating point number in *`sin`*.
The angles in *`t`* are represented in radians. The sine of
a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_sin`,
which can be used in an expression in the following syntax:

[`Sin := sin(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  angle.rad(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`sin`** (output_control)  number(-array) `→` Sequence[float]

Sine of the input tuple.

## Alternatives

`tuple_cos`,
`tuple_tan`

## See also

`tuple_asin`,
`tuple_sinh`,
`tuple_asinh`

## Module

Foundation
