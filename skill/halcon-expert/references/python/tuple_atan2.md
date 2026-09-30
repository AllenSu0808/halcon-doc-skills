# tuple_atan2 (Operator)

## Name

`tuple_atan2` — Compute the arctangent of a tuple for all four quadrants.

## Signature

`def tuple_atan2(y: MaybeSequence[Union[float, int]], x: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_atan2_s(y: MaybeSequence[Union[float, int]], x: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_atan2` computes the arctangent of the input tuples
*`y`*/*`x`* while treating all four quadrants
correctly. The arctangent is always returned as a floating point
number in *`atan`*. The angles in *`atan`* are represented in
radians. The arctangent of a string is not allowed.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_atan2`,
which can be used in an expression in the following syntax:

[`ATan := atan2(Y, X)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`y`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple of the y-values.

**`x`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple of the x-values.

**`atan`** (output_control)  angle.rad(-array) `→` Sequence[float]

Arctangent of the input tuple.

## Alternatives

`tuple_atan`,
`tuple_asin`,
`tuple_acos`

## See also

`tuple_tan`,
`tuple_tanh`

## Module

Foundation
