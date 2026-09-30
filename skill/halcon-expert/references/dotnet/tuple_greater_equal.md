# TupleGreaterEqual (Operator)

## Name

`TupleGreaterEqual` — Test whether a tuple is greater or equal to another tuple.

## Signature

`static void HOperatorSet.TupleGreaterEqual(HTuple t1, HTuple t2, out HTuple greatereq)`

`HTuple HTuple.TupleGreaterEqual(HTuple t2)`

## Description

`TupleGreaterEqual` tests whether the input tuple
*`t1`* is greater or equal to *`t2`*. A tuple *`t1`*
is said to be greater or equal to a tuple *`t2`*, if
*`t1`* is not less than *`t2`*. A tuple *`t1`* is
said to be less than a tuple *`t2`*, if *`t1`* has been
found to be less when comparing it elementwise to *`t2`* or if
the first min(|T1|,|T2|) elements are equal and *`t1`* has
got less elements than *`t2`*.

With the elementwise comparison, the elements of *`t1`* and
*`t2`* are compared one by one. If the two elements are equal,
the next pair of elements will be examined. If the element of
*`t1`* is greater than that from *`t2`*, the result is 1 and
the comparison will be aborted. If the element of *`t1`* is less
than that from *`t2`*, the result is 0 and the comparison will be
aborted. If all elements have been tested and if all were equal, the
result is 1.

As a precondition for comparing the tuples elementwise two
corresponding elements must either both be (integer or floating point)
numbers or both be strings. Otherwise `TupleGreaterEqual`
returns an error.

### Exception: Empty input tuples

If one input tuple is empty and the other is not, the tuple that is not
empty is considered greater than the empty one.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleGreaterEqual`,
which can be used in an expression in the following syntax:

[`Greatereq := T1 >= T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_comparison_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t1`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple 1.

**`t2`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple 2.

**`greatereq`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Result of the comparison of the input tuples.

## Alternatives

`TupleGreater`,
`TupleLess`,
`TupleLessEqual`,
`TupleEqual`,
`TupleNotEqual`,
`TupleEqualElem`,
`TupleNotEqualElem`,
`TupleLessElem`,
`TupleGreaterElem`,
`TupleLessEqualElem`,
`TupleGreaterEqualElem`

## Module

Foundation
