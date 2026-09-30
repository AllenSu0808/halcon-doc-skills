# tuple_mod (Operator)

## Name

`tuple_mod` — Calculate the remainder of the integer division of two tuples.

## Signature

`tuple_mod( : : T1, T2 : Mod)`

## Description

`tuple_mod` returns the remainder of the integer
division of the input tuples *`T1`*/*`T2`* in the
output tuple *`Mod`*. If both
tuples have the same length the division is performed for the
corresponding elements of both tuples. Otherwise, either
*`T1`* or *`T2`* must have length 1. In this case, the
division is performed for each element of the longer tuple with the
single element of the other tuple. The result is always an integer
number. The division of strings is not allowed.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_mod`,
which can be used in an expression in the following syntax:

[`Mod := T1 % T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_arithmetic_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T1`** (input_control)  number(-array) `→`  (integer)

Input tuple 1.

**`T2`** (input_control)  number(-array) `→`  (integer)

Input tuple 2.

Restriction:
`T2 != 0`

**`Mod`** (output_control)  number(-array) `→`  (integer)

Remainder of the division of the input tuples.

## See also

`tuple_fmod`,
`tuple_div`

## Module

Foundation
