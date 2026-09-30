# TupleXor (Operator)

## Name

`TupleXor` — Compute the logical exclusive or of two tuples.

## Signature

`static void HOperatorSet.TupleXor(HTuple t1, HTuple t2, out HTuple xor)`

`HTuple HTuple.TupleXor(HTuple t2)`

## Description

`TupleXor` computes the logical exclusive or of the input
tuples *`t1`* and *`t2`*. If both tuples have the same
length the operation is performed on the corresponding elements of
both tuples. Otherwise, either *`t1`* or *`t2`* must have
length 1. In this case, the operation is performed for each element
of the longer tuple with the single element of the other tuple. The
input tuples must contain only integer numbers.

### Exception: Empty input tuples

If any of the input tuples is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleXor`,
which can be used in an expression in the following syntax:

[`Xor := T1 xor T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_boolean_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t1`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Input tuple 1.

**`t2`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Input tuple 2.

**`xor`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Binary exclusive or of the input tuples.

## Alternatives

`TupleAnd`,
`TupleOr`,
`TupleNot`

## See also

`TupleBand`,
`TupleBor`,
`TupleBxor`,
`TupleBnot`

## Module

Foundation
