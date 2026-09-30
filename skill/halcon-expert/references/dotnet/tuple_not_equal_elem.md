# TupleNotEqualElem (Operator)

## Name

`TupleNotEqualElem` — Test, whether two tuples are elementwise not equal.

## Signature

`static void HOperatorSet.TupleNotEqualElem(HTuple t1, HTuple t2, out HTuple nequal)`

`HTuple HTuple.TupleNotEqualElem(HTuple t2)`

## Description

`TupleNotEqualElem` tests whether the two input tuples
*`t1`* and *`t2`* are elementwise not equal.
If both tuples have the same length, the corresponding
elements of both tuples are compared. Otherwise, either *`t1`*
or *`t2`* must have length 1. In this case, the comparison is
performed for each element of the longer tuple with the single element
of the other tuple. Two tuple elements differ if they are of types
that may not be compared (e.g., one string and one integer) or if they
differ in their values.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleNotEqualElem`,
which can be used in an expression in the following syntax:

[`Nequal := T1 [!=] T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_comparison_elem_0000.html)
or
[`Nequal := T1 [#] T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_comparison_elem_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t1`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple 1.

**`t2`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple 2.

**`nequal`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Result of the comparison of the input tuples.

## Alternatives

`TupleEqualElem`,
`TupleLessElem`,
`TupleGreaterElem`,
`TupleLessEqualElem`,
`TupleGreaterEqualElem`,
`TupleEqual`,
`TupleNotEqual`,
`TupleLess`,
`TupleGreater`,
`TupleLessEqual`,
`TupleGreaterEqual`

## Module

Foundation
