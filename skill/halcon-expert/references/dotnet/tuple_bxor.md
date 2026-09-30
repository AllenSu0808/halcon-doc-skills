# TupleBxor (Operator)

## Name

`TupleBxor` — Compute the bitwise exclusive or of two tuples.

## Signature

`static void HOperatorSet.TupleBxor(HTuple t1, HTuple t2, out HTuple BXor)`

`HTuple HTuple.TupleBxor(HTuple t2)`

## Description

`TupleBxor` computes the bitwise exclusive or of the input
tuples *`t1`* and *`t2`*. If both tuples have the same
length the operation is performed on the corresponding elements of
both tuples. Otherwise, either *`t1`* or *`t2`* must have
length 1. In this case, the operation is performed for each element
of the longer tuple with the single element of the other tuple. The
input tuples must contain only integer numbers.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleBxor`,
which can be used in an expression in the following syntax:

[`BXor := T1 bxor T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_bit_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t1`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Input tuple 1.

**`t2`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Input tuple 2.

**`BXor`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Binary exclusive or of the input tuples.

## Alternatives

`TupleBand`,
`TupleBor`,
`TupleBnot`

## See also

`TupleAnd`,
`TupleOr`,
`TupleXor`,
`TupleNot`

## Module

Foundation
