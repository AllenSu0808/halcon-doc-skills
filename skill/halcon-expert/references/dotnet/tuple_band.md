# TupleBand (Operator)

## Name

`TupleBand` — Compute the bitwise and of two tuples.

## Signature

`static void HOperatorSet.TupleBand(HTuple t1, HTuple t2, out HTuple BAnd)`

`HTuple HTuple.TupleBand(HTuple t2)`

## Description

`TupleBand` computes the bitwise and of the input tuples
*`t1`* and *`t2`*. If both tuples have the same length
the operation is performed on the corresponding elements of both
tuples. Otherwise, either *`t1`* or *`t2`* must have
length 1. In this case, the operation is performed for each element
of the longer tuple with the single element of the other tuple. The
input tuples must contain only integer numbers.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleBand`,
which can be used in an expression in the following syntax:

[`BAnd := T1 band T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_bit_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t1`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Input tuple 1.

**`t2`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Input tuple 2.

**`BAnd`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Binary and of the input tuples.

## Alternatives

`TupleBor`,
`TupleBxor`,
`TupleBnot`

## See also

`TupleAnd`,
`TupleOr`,
`TupleXor`,
`TupleNot`

## Module

Foundation
