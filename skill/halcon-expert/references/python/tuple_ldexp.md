# tuple_ldexp (Operator)

## Name

`tuple_ldexp` — Calculate the ldexp function of two tuples.

## Signature

`def tuple_ldexp(t1: MaybeSequence[Union[float, int]], t2: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_ldexp_s(t1: MaybeSequence[Union[float, int]], t2: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_ldexp` computes the ldexp function of the input tuples, i.e.,
$T1 \cdot 2^{f\mathrm{floor}}(\mathrm{T2})$ ![figure](../assets/fd4934e165a5379c.svg).
If both tuples have the same
length the operation is performed for the corresponding elements of
both tuples. Otherwise, either *`t1`* or *`t2`* must have
length 1. In this case, the operation is performed for each element
of the longer tuple with the single element of the other tuple. The
result is always a floating point number. The ldexp function of
strings is not allowed.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_ldexp`,
which can be used in an expression in the following syntax:

[`Ldexp := ldexp(T1, T2)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_exponential_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t1`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple 1.

**`t2`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple 2.

**`ldexp`** (output_control)  number(-array) `→` Sequence[float]

Ldexp function of the input tuples.

## See also

`tuple_exp`

## Module

Foundation
