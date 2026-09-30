# tuple_exp10 (Operator)

## Name

`tuple_exp10` — Compute the base 10 exponential of a tuple.

## Signature

`def tuple_exp10(t: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_exp10_s(t: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_exp10` computes the base 10 exponential of the input
tuple *`t`*. The exponential is always returned as a floating
point number. The exponential of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_exp10`,
which can be used in an expression in the following syntax:

[`Exp := exp10(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_exponential_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`exp`** (output_control)  number(-array) `→` Sequence[float]

Base 10 exponential of the input tuple.

## Alternatives

`tuple_exp`,
`tuple_exp2`,
`tuple_pow`

## See also

`tuple_log`,
`tuple_log2`,
`tuple_log10`

## Module

Foundation
