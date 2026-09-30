# tuple_bnot (Operator)

## Name

`tuple_bnot` — Compute the bitwise not of a tuple.

## Signature

`tuple_bnot( : : T : BNot)`

## Description

`tuple_bnot` computes the bitwise not of the input tuple
*`T`*. The input tuple must contain only integer numbers.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_bnot`,
which can be used in an expression in the following syntax:

[`BNot := bnot T`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_bit_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  integer(-array) `→`  (integer)

Input tuple.

**`BNot`** (output_control)  integer(-array) `→`  (integer)

Binary not of the input tuple.

## Alternatives

`tuple_band`,
`tuple_bor`,
`tuple_bxor`

## See also

`tuple_and`,
`tuple_or`,
`tuple_xor`,
`tuple_not`

## Module

Foundation
