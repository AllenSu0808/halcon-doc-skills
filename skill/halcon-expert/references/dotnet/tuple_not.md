# TupleNot (Operator)

## Name

`TupleNot` — Compute the logical not of a tuple.

## Signature

`static void HOperatorSet.TupleNot(HTuple t, out HTuple not)`

`HTuple HTuple.TupleNot()`

## Description

`TupleNot` computes the logical not of the input tuple
*`t`*. The input tuple must contain only integer numbers.

### Exception: Empty input tuple

If the input tuple is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleNot`,
which can be used in an expression in the following syntax:

[`Not := not T1`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_boolean_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Input tuple.

**`not`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Binary not of the input tuple.

## Alternatives

`TupleAnd`,
`TupleOr`,
`TupleXor`

## See also

`TupleBand`,
`TupleBor`,
`TupleBxor`,
`TupleBnot`

## Module

Foundation
