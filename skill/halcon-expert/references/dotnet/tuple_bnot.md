# TupleBnot (Operator)

## Name

`TupleBnot` — Compute the bitwise not of a tuple.

## Signature

`static void HOperatorSet.TupleBnot(HTuple t, out HTuple BNot)`

`HTuple HTuple.TupleBnot()`

## Description

`TupleBnot` computes the bitwise not of the input tuple
*`t`*. The input tuple must contain only integer numbers.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleBnot`,
which can be used in an expression in the following syntax:

[`BNot := bnot T`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_bit_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Input tuple.

**`BNot`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Binary not of the input tuple.

## Alternatives

`TupleBand`,
`TupleBor`,
`TupleBxor`

## See also

`TupleAnd`,
`TupleOr`,
`TupleXor`,
`TupleNot`

## Module

Foundation
