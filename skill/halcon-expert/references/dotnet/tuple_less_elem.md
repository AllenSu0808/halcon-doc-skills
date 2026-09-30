# TupleLessElem (Operator)

## Name

`TupleLessElem` — Test, whether a tuple is elementwise less than another tuple.

## Signature

`static void HOperatorSet.TupleLessElem(HTuple t1, HTuple t2, out HTuple less)`

`HTuple HTuple.TupleLessElem(HTuple t2)`

## Description

`TupleLessElem` tests elementwise whether the input tuple
*`t1`* is less than *`t2`*.
If both tuples have the same length, the corresponding
elements of both tuples are compared. Otherwise, either *`t1`*
or *`t2`* must have length 1. In this case, the comparison is
performed for each element of the longer tuple with the single element
of the other tuple. As a precondition for comparing the tuples elementwise
two corresponding elements must either both be (integer or floating point)
numbers or both be strings. Otherwise `TupleLessElem`
returns an error.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleLessElem`,
which can be used in an expression in the following syntax:

[`Less := T1 [<] T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_comparison_elem_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t1`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple 1.

**`t2`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple 2.

**`less`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Result of the comparison of the input tuples.

## Alternatives

`TupleEqualElem`,
`TupleNotEqualElem`,
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
