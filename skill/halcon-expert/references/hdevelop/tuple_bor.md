# tuple_bor (Operator)

## Name

`tuple_bor` — Compute the bitwise or of two tuples.

## Signature

`tuple_bor( : : T1, T2 : BOr)`

## Description

`tuple_bor` computes the bitwise or of the input tuples
*`T1`* and *`T2`*. If both tuples have the same length
the operation is performed on the corresponding elements of both
tuples. Otherwise, either *`T1`* or *`T2`* must have
length 1. In this case, the operation is performed for each element
of the longer tuple with the single element of the other tuple. The
input tuples must contain only integer numbers.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_bor`,
which can be used in an expression in the following syntax:

[`BOr := T1 bor T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_bit_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T1`** (input_control)  integer(-array) `→`  (integer)

Input tuple 1.

**`T2`** (input_control)  integer(-array) `→`  (integer)

Input tuple 2.

**`BOr`** (output_control)  integer(-array) `→`  (integer)

Binary or of the input tuples.

## Alternatives

`tuple_band`,
`tuple_bxor`,
`tuple_bnot`

## See also

`tuple_and`,
`tuple_or`,
`tuple_xor`,
`tuple_not`

## Module

Foundation
