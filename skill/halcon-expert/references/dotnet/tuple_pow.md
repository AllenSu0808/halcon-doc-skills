# TuplePow (Operator)

## Name

`TuplePow` — Calculate the power function of two tuples.

## Signature

`static void HOperatorSet.TuplePow(HTuple t1, HTuple t2, out HTuple pow)`

`HTuple HTuple.TuplePow(HTuple t2)`

## Description

`TuplePow` computes the power function of the input tuples
*`t1`*^{*`t2`*}. If both tuples have the same length
the power function is applied to the corresponding elements of both
tuples. Otherwise, either *`t1`* or *`t2`* must have
length 1. In this case, the power function is performed for each
element of the longer tuple with the single element of the other
tuple. The result is always a floating point number. The
power function of strings is not allowed.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TuplePow`,
which can be used in an expression in the following syntax:

[`Pow := pow(T1, T2)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_exponential_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t1`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple 1.

**`t2`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple 2.

**`pow`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Power function of the input tuples.

## Alternatives

`TupleExp`

## See also

`TupleLog`,
`TupleLog10`

## Module

Foundation
