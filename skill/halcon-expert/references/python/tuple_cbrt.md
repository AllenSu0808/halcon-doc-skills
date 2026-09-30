# tuple_cbrt (Operator)

## Name

`tuple_cbrt` — Compute the cube root of a tuple.

## Signature

`def tuple_cbrt(t: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_cbrt_s(t: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_cbrt` computes the cube root of the input tuple
*`t`*. The cube root is always returned as a floating point
number. The cube root of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_cbrt`,
which can be used in an expression in the following syntax:

[`Cbrt := cbrt(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`cbrt`** (output_control)  number(-array) `→` Sequence[float]

Cube root of the input tuple.

## Alternatives

`tuple_pow`

## See also

`tuple_sqrt`

## Module

Foundation
