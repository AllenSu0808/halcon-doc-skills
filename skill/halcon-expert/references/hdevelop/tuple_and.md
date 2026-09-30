# tuple_and (Operator)

## Name

`tuple_and` — Compute the logical and of two tuples.

## Signature

`tuple_and( : : T1, T2 : And)`

## Description

`tuple_and` computes the logical and of the input tuples
*`T1`* and *`T2`*. If both tuples have the same length
the operation is performed on the corresponding elements of both
tuples. Otherwise, either *`T1`* or *`T2`* must have
length 1. In this case, the operation is performed for each element
of the longer tuple with the single element of the other tuple. The
input tuples must contain only integer numbers.

### Exception: Empty input tuples

If any of the input tuples is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_and`,
which can be used in an expression in the following syntax:

[`And := T1 and T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_boolean_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T1`** (input_control)  integer(-array) `→`  (integer)

Input tuple 1.

**`T2`** (input_control)  integer(-array) `→`  (integer)

Input tuple 2.

**`And`** (output_control)  integer(-array) `→`  (integer)

Logical and of the input tuples.

## Alternatives

`tuple_or`,
`tuple_xor`,
`tuple_not`

## See also

`tuple_band`,
`tuple_bor`,
`tuple_bxor`,
`tuple_bnot`

## Module

Foundation
