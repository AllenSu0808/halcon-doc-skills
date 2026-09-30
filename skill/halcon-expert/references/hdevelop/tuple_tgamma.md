# tuple_tgamma (Operator)

## Name

`tuple_tgamma` — Compute the gamma function of a tuple.

## Signature

`tuple_tgamma( : : T : Gamma)`

## Description

`tuple_tgamma` computes the gamma function of the input
tuple *`T`*. The gamma function is defined as:
$$\Gamma\left(x\right)=\int_{0}^{\infty} t^{x-1} e^{-t}\,dt.$$ ![figure](../assets/25e95836785db5e1.svg)
It is defined for every real number except for nonpositive
integers. For nonnegative integer $m$, it holds that
$$\Gamma(m+1)=m!$$
and, more generally, for all $x$:
$$\Gamma(x+1)=x\Gamma(x).$$
The value of the gamma function is always returned as a floating
point number in *`Gamma`*. The gamma function of a string is
not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_tgamma`,
which can be used in an expression in the following syntax:

[`Gamma := tgamma(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_exponential_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  number(-array) `→`  (real / integer)

Input tuple.

**`Gamma`** (output_control)  number(-array) `→`  (real)

Value of the gamma function of the input tuple.

## Alternatives

`tuple_lgamma`

## Module

Foundation
