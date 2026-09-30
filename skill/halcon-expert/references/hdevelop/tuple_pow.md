# tuple_pow (Operator)

## Name

`tuple_pow` — Calculate the power function of two tuples.

## Signature

`tuple_pow( : : T1, T2 : Pow)`

## Description

`tuple_pow` computes the power function of the input tuples
*`T1`*^{*`T2`*}. If both tuples have the same length
the power function is applied to the corresponding elements of both
tuples. Otherwise, either *`T1`* or *`T2`* must have
length 1. In this case, the power function is performed for each
element of the longer tuple with the single element of the other
tuple. The result is always a floating point number. The
power function of strings is not allowed.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_pow`,
which can be used in an expression in the following syntax:

[`Pow := pow(T1, T2)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_exponential_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T1`** (input_control)  number(-array) `→`  (real / integer)

Input tuple 1.

**`T2`** (input_control)  number(-array) `→`  (real / integer)

Input tuple 2.

**`Pow`** (output_control)  number(-array) `→`  (real)

Power function of the input tuples.

## Alternatives

`tuple_exp`

## See also

`tuple_log`,
`tuple_log10`

## Module

Foundation
