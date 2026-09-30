# tuple_hypot (Operator)

## Name

`tuple_hypot` — Calculate the hypotenuse of two tuples.

## Signature

`tuple_hypot( : : T1, T2 : Hypot)`

## Description

`tuple_hypot` computes the hypotenuse
$\sqrt{T_1^2 + T_2^2}$ ![figure](../assets/d2c7b67ac701c568.svg)
of the input tuples. The calculation is performed without undue arithmetic
overflow or underflow during the intermediate steps of the
calculation. If both tuples have the same length, the hypotenuse is
applied to the corresponding elements of both tuples. Otherwise,
either *`T1`* or *`T2`* must have length 1. In this case,
the hypotenuse is calculated for each element of the longer tuple
with the single element of the other tuple. The result is always a
floating point number. The hypotenuse of strings is not allowed.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_hypot`,
which can be used in an expression in the following syntax:

[`Hypot := hypot(T1, T2)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T1`** (input_control)  number(-array) `→`  (real / integer)

Input tuple 1.

**`T2`** (input_control)  number(-array) `→`  (real / integer)

Input tuple 2.

**`Hypot`** (output_control)  number(-array) `→`  (real)

Hypotenuse of the input tuples.

## Alternatives

`tuple_sqrt`

## See also

`tuple_mult`,
`tuple_add`

## Module

Foundation
