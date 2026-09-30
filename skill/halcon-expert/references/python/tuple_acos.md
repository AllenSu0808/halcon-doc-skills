# tuple_acos (Operator)

## Name

`tuple_acos` — Compute the arccosine of a tuple.

## Signature

`def tuple_acos(t: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_acos_s(t: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_acos` computes the arccosine of the input tuple
*`t`*. The arccosine is always returned as a floating point
number in *`acos`*. The angles in *`acos`* are represented in
radians. The arccosine of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_acos`,
which can be used in an expression in the following syntax:

[`ACos := acos(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

Restriction:
`-1 <= T <= 1`

**`acos`** (output_control)  angle.rad(-array) `→` Sequence[float]

Arccosine of the input tuple.

## Alternatives

`tuple_asin`,
`tuple_atan`,
`tuple_atan2`

## See also

`tuple_cos`,
`tuple_cosh`,
`tuple_acosh`

## Module

Foundation
