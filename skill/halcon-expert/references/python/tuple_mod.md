# tuple_mod (Operator)

## Name

`tuple_mod` — Calculate the remainder of the integer division of two tuples.

## Signature

`def tuple_mod(t1: MaybeSequence[int], t2: MaybeSequence[int]) -> Sequence[int]`

`def tuple_mod_s(t1: MaybeSequence[int], t2: MaybeSequence[int]) -> int`

## Description

`tuple_mod` returns the remainder of the integer
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

HDevelop provides an in-line operation for `tuple_mod`,
which can be used in an expression in the following syntax:

[`Mod := T1 % T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_arithmetic_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t1`** (input_control)  number(-array) `→` MaybeSequence[int]

Input tuple 1.

**`t2`** (input_control)  number(-array) `→` MaybeSequence[int]

Input tuple 2.

Restriction:
`T2 != 0`

**`mod`** (output_control)  number(-array) `→` Sequence[int]

Remainder of the division of the input tuples.

## See also

`tuple_fmod`,
`tuple_div`

## Module

Foundation
