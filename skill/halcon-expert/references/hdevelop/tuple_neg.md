# tuple_neg (Operator)

## Name

`tuple_neg` — Negate a tuple.

## Signature

`tuple_neg( : : T : Neg)`

## Description

`tuple_neg` computes the negation of the input tuple
*`T`*, i.e., *`Neg`* = -*`T`*. The negation of an
integer number is again an integer number. The negation of a
floating point number is a floating point number. The negation of a
string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_neg`,
which can be used in an expression in the following syntax:

[`Neg := -T`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_arithmetic_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  number(-array) `→`  (real / integer)

Input tuple.

**`Neg`** (output_control)  number(-array) `→`  (real / integer)

Negation of the input tuple.

## Module

Foundation
