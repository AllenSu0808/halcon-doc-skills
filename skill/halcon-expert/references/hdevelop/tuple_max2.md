# tuple_max2 (Operator)

## Name

`tuple_max2` — Calculate the elementwise maximum of two tuples.

## Signature

`tuple_max2( : : T1, T2 : Max2)`

## Description

`tuple_max2` returns the elementwise maximum of the input tuples
*`T1`* and *`T2`* in the output tuple *`Max2`*.
If both tuples have the same length the corresponding elements
of both tuples are compared.
Otherwise, either *`T1`* or *`T2`* must have
length 1. In this case, the comparison is performed for each
element of the longer tuple with the single element of the other
tuple. If the corresponding elements of the two tuples have the same
type, it is allowed to mix strings with numerical values.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_max2`,
which can be used in an expression in the following syntax:

[`Max2 := max2(T1, T2)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T1`** (input_control)  tuple(-array) `→`  (real / integer / string)

Input tuple 1.

**`T2`** (input_control)  tuple(-array) `→`  (real / integer / string)

Input tuple 2.

**`Max2`** (output_control)  tuple(-array) `→`  (real / integer / string)

Elementwise maximum of the input tuples.

## See also

`tuple_min2`,
`tuple_min`,
`tuple_max`,
`tuple_cumul`

## Module

Foundation
