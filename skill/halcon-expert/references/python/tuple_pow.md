# tuple_pow (Operator)

## Name

`tuple_pow` — Calculate the power function of two tuples.

## Signature

`def tuple_pow(t1: MaybeSequence[Union[float, int]], t2: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_pow_s(t1: MaybeSequence[Union[float, int]], t2: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_pow` computes the power function of the input tuples
*`t1`*^{*`t2`*}. If both tuples have the same length
the power function is applied to the corresponding elements of both
tuples. Otherwise, either *`t1`* or *`t2`* must have
length 1. In this case, the power function is performed for each
element of the longer tuple with the single element of the other
tuple. The result is always a floating point number. The
power function of strings is not allowed.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_pow`,
which can be used in an expression in the following syntax:

[`Pow := pow(T1, T2)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_exponential_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t1`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple 1.

**`t2`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple 2.

**`pow`** (output_control)  number(-array) `→` Sequence[float]

Power function of the input tuples.

## Alternatives

`tuple_exp`

## See also

`tuple_log`,
`tuple_log10`

## Module

Foundation
