# tuple_atan (Operator)

## Name

`tuple_atan` — Compute the arctangent of a tuple.

## Signature

`def tuple_atan(t: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_atan_s(t: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_atan` computes the arctangent of the input tuple
*`t`*. The arctangent is always returned as a floating point
number in *`atan`*. The angles in *`atan`* are represented in
radians. The arctangent of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_atan`,
which can be used in an expression in the following syntax:

[`ATan := atan(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`atan`** (output_control)  angle.rad(-array) `→` Sequence[float]

Arctangent of the input tuple.

## Alternatives

`tuple_atan2`,
`tuple_asin`,
`tuple_acos`

## See also

`tuple_tan`,
`tuple_tanh`,
`tuple_atanh`

## Module

Foundation
