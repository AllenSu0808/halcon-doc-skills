# tuple_not_equal (Operator)

## Name

`tuple_not_equal` — Test whether two tuples are not equal.

## Signature

`tuple_not_equal( : : T1, T2 : Nequal)`

## Description

`tuple_not_equal` tests whether the two input tuples *`T1`*
and *`T2`* are not equal. Two tuples are not equal, if
they consist of a different number of elements or if they differ
when compared elementwise. Two tuple elements differ, if they
are of types that may not be compared (e.g., one string and one integer)
or if they differ in their values.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_not_equal`,
which can be used in an expression in the following syntax:

[`Nequal := T1 != T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_comparison_0000.html)
or
[`Nequal := T1 # T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_comparison_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T1`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple 1.

**`T2`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple 2.

**`Nequal`** (output_control)  integer `→`  (integer)

Result of the comparison of the input tuples.

## Alternatives

`tuple_equal`,
`tuple_less`,
`tuple_greater`,
`tuple_less_equal`,
`tuple_greater_equal`,
`tuple_equal_elem`,
`tuple_not_equal_elem`,
`tuple_less_elem`,
`tuple_greater_elem`,
`tuple_less_equal_elem`,
`tuple_greater_equal_elem`

## Module

Foundation
