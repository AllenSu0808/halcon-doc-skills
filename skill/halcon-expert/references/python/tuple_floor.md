# tuple_floor (Operator)

## Name

`tuple_floor` — Compute the floor function of a tuple.

## Signature

`def tuple_floor(t: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_floor_s(t: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_floor` computes the floor function of the input tuple
*`t`*, i.e., the largest integer less than or equal to
*`t`*. The floor function is always returned as a floating
point number. The floor function of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_floor`,
which can be used in an expression in the following syntax:

[`Floor := floor(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`floor`** (output_control)  number(-array) `→` Sequence[float]

Floor function of the input tuple.

## Alternatives

`tuple_ceil`

## Module

Foundation
