# TupleEqual (Operator)

## Name

`TupleEqual` — Test whether two tuples are equal.

## Signature

`static void HOperatorSet.TupleEqual(HTuple t1, HTuple t2, out HTuple equal)`

`HTuple HTuple.TupleEqual(HTuple t2)`

## Description

`TupleEqual` tests whether the two input tuples *`t1`*
and *`t2`* are equal by comparing the tuples elementwise.
Two tuples are equal, if they have got the same number of elements and
if their elements are equal.
Two tuple elements are equal, if they are both (integer or floating point)
numbers or both are strings and contain the same value.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleEqual`,
which can be used in an expression in the following syntax:

[`Equal := T1 == T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_comparison_0000.html)
or
[`Equal := T1 = T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_comparison_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t1`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple 1.

**`t2`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple 2.

**`equal`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Result of the comparison of the input tuples.

## Alternatives

`TupleNotEqual`,
`TupleLess`,
`TupleGreater`,
`TupleLessEqual`,
`TupleGreaterEqual`,
`TupleEqualElem`,
`TupleNotEqualElem`,
`TupleLessElem`,
`TupleGreaterElem`,
`TupleLessEqualElem`,
`TupleGreaterEqualElem`

## Module

Foundation
