# tuple_exp (Operator)

## Name

`tuple_exp` — Compute the exponential of a tuple.

## Signature

`def tuple_exp(t: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_exp_s(t: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_exp` computes the exponential of the input tuple
*`t`*. The exponential is always returned as a floating point
number. The exponential of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_exp`,
which can be used in an expression in the following syntax:

[`Exp := exp(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_exponential_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`exp`** (output_control)  number(-array) `→` Sequence[float]

Exponential of the input tuple.

## Alternatives

`tuple_exp2`,
`tuple_exp10`,
`tuple_pow`

## See also

`tuple_log`,
`tuple_log2`,
`tuple_log10`

## Module

Foundation
