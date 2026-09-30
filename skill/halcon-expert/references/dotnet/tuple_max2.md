# TupleMax2 (Operator)

## Name

`TupleMax2` — Calculate the elementwise maximum of two tuples.

## Signature

`static void HOperatorSet.TupleMax2(HTuple t1, HTuple t2, out HTuple max2)`

`HTuple HTuple.TupleMax2(HTuple t2)`

## Description

`TupleMax2` returns the elementwise maximum of the input tuples
*`t1`* and *`t2`* in the output tuple *`max2`*.
If both tuples have the same length the corresponding elements
of both tuples are compared.
Otherwise, either *`t1`* or *`t2`* must have
length 1. In this case, the comparison is performed for each
element of the longer tuple with the single element of the other
tuple. If the corresponding elements of the two tuples have the same
type, it is allowed to mix strings with numerical values.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleMax2`,
which can be used in an expression in the following syntax:

[`Max2 := max2(T1, T2)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t1`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Input tuple 1.

**`t2`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Input tuple 2.

**`max2`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Elementwise maximum of the input tuples.

## See also

`TupleMin2`,
`TupleMin`,
`TupleMax`,
`TupleCumul`

## Module

Foundation
