# TupleMod (Operator)

## Name

`TupleMod` — Calculate the remainder of the integer division of two tuples.

## Signature

`static void HOperatorSet.TupleMod(HTuple t1, HTuple t2, out HTuple mod)`

`HTuple HTuple.TupleMod(HTuple t2)`

## Description

`TupleMod` returns the remainder of the integer
division of the input tuples *`t1`*/*`t2`* in the
output tuple *`mod`*. If both
tuples have the same length the division is performed for the
corresponding elements of both tuples. Otherwise, either
*`t1`* or *`t2`* must have length 1. In this case, the
division is performed for each element of the longer tuple with the
single element of the other tuple. The result is always an integer
number. The division of strings is not allowed.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleMod`,
which can be used in an expression in the following syntax:

[`Mod := T1 % T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_arithmetic_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t1`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long)

Input tuple 1.

**`t2`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long)

Input tuple 2.

Restriction:
`T2 != 0`

**`mod`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long)

Remainder of the division of the input tuples.

## See also

`TupleFmod`,
`TupleDiv`

## Module

Foundation
