# TupleSub (Operator)

## Name

`TupleSub` — Subtract two tuples.

## Signature

`static void HOperatorSet.TupleSub(HTuple d1, HTuple d2, out HTuple diff)`

`HTuple HTuple.TupleSub(HTuple d2)`

## Description

`TupleSub` computes the difference of the input tuples
*`d1`* and *`d2`*. If both tuples have the same length
the corresponding elements of both tuples are subtracted.
Otherwise, either *`d1`* or *`d2`* must have length 1. In
this case, the subtraction is performed for each element of the
longer tuple with the single element of the other tuple. If two
integer numbers are subtracted, the result is again an integer
number. If one of the operands is a floating point number, the
result is a floating point number. The subtraction of strings is
not allowed.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleSub`,
which can be used in an expression in the following syntax:

[`Diff := D1 - D2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_arithmetic_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`d1`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple 1.

**`d2`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple 2.

**`diff`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Difference of the input tuples.

## Alternatives

`TupleAdd`

## Module

Foundation
