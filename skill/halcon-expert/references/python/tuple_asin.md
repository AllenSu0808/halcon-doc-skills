# tuple_asin (Operator)

## Name

`tuple_asin` — Compute the arcsine of a tuple.

## Signature

`def tuple_asin(t: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_asin_s(t: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_asin` computes the arcsine of the input tuple
*`t`*. The arcsine is always returned as a floating point
number in *`asin`*. The angles in *`asin`* are represented
in radians. The arcsine of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_asin`,
which can be used in an expression in the following syntax:

[`ASin := asin(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

Restriction:
`-1 <= T <= 1`

**`asin`** (output_control)  angle.rad(-array) `→` Sequence[float]

Arcsine of the input tuple.

## Alternatives

`tuple_acos`,
`tuple_atan`,
`tuple_atan2`

## See also

`tuple_sin`,
`tuple_sinh`,
`tuple_asinh`

## Module

Foundation
