# TupleEqualElem (Operator)

## Name

`TupleEqualElem` — Test, whether two tuples are elementwise equal.

## Signature

`static void HOperatorSet.TupleEqualElem(HTuple t1, HTuple t2, out HTuple equal)`

`HTuple HTuple.TupleEqualElem(HTuple t2)`

## Description

`TupleEqualElem` tests whether the two input tuples
*`t1`* and *`t2`* are elementwise equal.
If both tuples have the same length, the corresponding elements of both
tuples are compared. Otherwise, either *`t1`* or *`t2`* must
have length 1. In this case, the comparison is performed for each element
of the longer tuple with the single element of the other tuple. Two tuple
elements are equal if they are both (integer or floating point)
numbers or both are strings and contain the same value.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleEqualElem`,
which can be used in an expression in the following syntax:

[`Equal := T1 [==] T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_comparison_elem_0000.html)
or
[`Equal := T1 [=] T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_comparison_elem_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t1`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple 1.

**`t2`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple 2.

**`equal`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Result of the comparison of the input tuples.

## Alternatives

`TupleNotEqualElem`,
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
