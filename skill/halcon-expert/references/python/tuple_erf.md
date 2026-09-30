# tuple_erf (Operator)

## Name

`tuple_erf` — Compute the error function of a tuple.

## Signature

`def tuple_erf(t: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_erf_s(t: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_erf` computes the error function of the input
tuple *`t`*. The error function is defined as:
$$\mathrm{erf}(x) = \frac{2}{\sqrt{\pi}} \int_{0}^{x} e^{-t^{2}} \, dt.$$ ![figure](../assets/c0078a951370d080.svg)
The value of the error function is always returned as a floating
point number in *`erf`*. The error function of a string is not
allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_erf`, which
can be used in an expression in the following syntax:

[`Erf := erf(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_exponential_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`erf`** (output_control)  number(-array) `→` Sequence[float]

Value of the error function of the input tuple.

## Alternatives

`tuple_erfc`

## See also

`tuple_exp`

## Module

Foundation
