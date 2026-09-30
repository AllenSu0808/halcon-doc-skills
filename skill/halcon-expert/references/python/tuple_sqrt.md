# tuple_sqrt (Operator)

## Name

`tuple_sqrt` — Compute the square root of a tuple.

## Signature

`def tuple_sqrt(t: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_sqrt_s(t: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_sqrt` computes the square root of the input tuple
*`t`*. The square root is always returned as a floating point
number. The square root of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_sqrt`,
which can be used in an expression in the following syntax:

[`Sqrt := sqrt(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

Restriction:
`T >= 0`

**`sqrt`** (output_control)  number(-array) `→` Sequence[float]

Square root of the input tuple.

## Alternatives

`tuple_pow`

## See also

`tuple_cbrt`,
`tuple_hypot`

## Module

Foundation
