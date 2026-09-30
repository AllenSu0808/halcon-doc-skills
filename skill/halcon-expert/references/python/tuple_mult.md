# tuple_mult (Operator)

## Name

`tuple_mult` — Multiply two tuples.

## Signature

`def tuple_mult(p1: MaybeSequence[Union[float, int]], p2: MaybeSequence[Union[float, int]]) -> Sequence[Union[float, int]]`

`def tuple_mult_s(p1: MaybeSequence[Union[float, int]], p2: MaybeSequence[Union[float, int]]) -> Union[float, int]`

## Description

`tuple_mult` computes the product of the input tuples
*`p1`* and *`p2`*. If both tuples have the same length
the corresponding elements of both tuples are multiplied.
Otherwise, either *`p1`* or *`p2`* must have length 1. In
this case, the multiplication is performed for each element of the
longer tuple with the single element of the other tuple. If two
integer numbers are multiplied, the result is again an integer
number. If one of the operands is a floating point number, the
result is a floating point number. The multiplication of strings is
not allowed.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_mult`,
which can be used in an expression in the following syntax:

[`Prod := P1 * P2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_arithmetic_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`p1`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple 1.

**`p2`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple 2.

**`prod`** (output_control)  number(-array) `→` Sequence[Union[float, int]]

Product of the input tuples.

## Alternatives

`tuple_div`

## Module

Foundation
