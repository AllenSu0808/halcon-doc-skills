# tuple_not (Operator)

## Name

`tuple_not` — Compute the logical not of a tuple.

## Signature

`tuple_not( : : T : Not)`

## Description

`tuple_not` computes the logical not of the input tuple
*`T`*. The input tuple must contain only integer numbers.

### Exception: Empty input tuple

If the input tuple is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_not`,
which can be used in an expression in the following syntax:

[`Not := not T1`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_boolean_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  integer(-array) `→`  (integer)

Input tuple.

**`Not`** (output_control)  integer(-array) `→`  (integer)

Binary not of the input tuple.

## Alternatives

`tuple_and`,
`tuple_or`,
`tuple_xor`

## See also

`tuple_band`,
`tuple_bor`,
`tuple_bxor`,
`tuple_bnot`

## Module

Foundation
