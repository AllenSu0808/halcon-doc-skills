# tuple_ceil (Operator)

## Name

`tuple_ceil` — Compute the ceiling function of a tuple.

## Signature

`def tuple_ceil(t: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_ceil_s(t: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_ceil` computes the ceiling function of the input tuple
*`t`*, i.e., the smallest integer greater than or equal to
*`t`*. The ceiling function is always returned as a floating
point number. The ceiling function of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_ceil`,
which can be used in an expression in the following syntax:

[`Ceil := ceil(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`ceil`** (output_control)  number(-array) `→` Sequence[float]

Ceiling function of the input tuple.

## Module

Foundation
