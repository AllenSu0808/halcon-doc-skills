# tuple_div (Operator)

## Name

`tuple_div` — Divide two tuples.

## Signature

`tuple_div( : : Q1, Q2 : Quot)`

## Description

`tuple_div` computes the quotient of the input tuples
*`Q1`* and *`Q2`*. If both tuples have the same length
the corresponding elements of both tuples are divided. Otherwise,
either *`Q1`* or *`Q2`* must have length 1. In this case,
the division is performed for each element of the longer tuple with
the single element of the other tuple. If two integer numbers are
divided, the result is again an integer number. If one of the
operands is a floating point number, the result is a floating point
number. The division of strings is not allowed.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_div`,
which can be used in an expression in the following syntax:

[`Quot := Q1 / Q2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_arithmetic_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Q1`** (input_control)  number(-array) `→`  (real / integer)

Input tuple 1.

**`Q2`** (input_control)  number(-array) `→`  (real / integer)

Input tuple 2.

Restriction:
`Q2 != 0`

**`Quot`** (output_control)  number(-array) `→`  (real / integer)

Quotient of the input tuples.

## Alternatives

`tuple_mult`

## Module

Foundation
