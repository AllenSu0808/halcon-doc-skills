# tuple_lgamma (Operator)

## Name

`tuple_lgamma` — Compute the logarithm of the absolute value of the gamma function of
a tuple.

## Signature

`def tuple_lgamma(t: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_lgamma_s(t: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_lgamma` computes the logarithm of the absolute value of
the gamma function of the input tuple *`t`* (for the definition
of the gamma function, see [`tuple_tgamma`](tuple_tgamma.md)). It is defined for
every real number except for nonpositive integers. The logarithm of
the absolute value of the gamma function is always returned as a
floating point number in *`log_gamma`*. The logarithm of the
absolute value of the gamma function of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_lgamma`,
which can be used in an expression in the following syntax:

[`LogGamma := lgamma(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_exponential_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`log_gamma`** (output_control)  number(-array) `→` Sequence[float]

Logarithm of the absolute value of the gamma function
of the input tuple.

## Alternatives

`tuple_tgamma`

## Module

Foundation
