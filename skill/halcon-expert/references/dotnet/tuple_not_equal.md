# TupleNotEqual (Operator)

## Name

`TupleNotEqual` — Test whether two tuples are not equal.

## Signature

`static void HOperatorSet.TupleNotEqual(HTuple t1, HTuple t2, out HTuple nequal)`

`HTuple HTuple.TupleNotEqual(HTuple t2)`

## Description

`TupleNotEqual` tests whether the two input tuples *`t1`*
and *`t2`* are not equal. Two tuples are not equal, if
they consist of a different number of elements or if they differ
when compared elementwise. Two tuple elements differ, if they
are of types that may not be compared (e.g., one string and one integer)
or if they differ in their values.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleNotEqual`,
which can be used in an expression in the following syntax:

[`Nequal := T1 != T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_comparison_0000.html)
or
[`Nequal := T1 # T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_comparison_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t1`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple 1.

**`t2`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple 2.

**`nequal`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Result of the comparison of the input tuples.

## Alternatives

`TupleEqual`,
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
