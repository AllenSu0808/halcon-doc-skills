# tuple_less_equal_elem (Operator)

## Name

`tuple_less_equal_elem` — Test, whether a tuple is elementwise less or equal to another tuple.

## Signature

`tuple_less_equal_elem( : : T1, T2 : Lesseq)`

## Description

`tuple_less_equal_elem` tests elementwise whether the input tuple
*`T1`* is less than or equal to *`T2`*.
If both tuples have the same length, the corresponding
elements of both tuples are compared. Otherwise, either *`T1`*
or *`T2`* must have length 1. In this case, the comparison is
performed for each element of the longer tuple with the single element
of the other tuple. As a precondition for comparing the tuples elementwise
two corresponding elements must either both be (integer or floating point)
numbers or both be strings. Otherwise `tuple_less_equal_elem`
returns an error.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_less_equal_elem`,
which can be used in an expression in the following syntax:

[`Lesseq := T1 [<=] T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_comparison_elem_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T1`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple 1.

**`T2`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple 2.

**`Lesseq`** (output_control)  integer(-array) `→`  (integer)

Result of the comparison of the input tuples.

## Alternatives

`tuple_equal_elem`,
`tuple_not_equal_elem`,
`tuple_greater_elem`,
`tuple_less_elem`,
`tuple_greater_equal_elem`,
`tuple_equal`,
`tuple_not_equal`,
`tuple_less`,
`tuple_greater`,
`tuple_less_equal`,
`tuple_greater_equal`

## Module

Foundation
