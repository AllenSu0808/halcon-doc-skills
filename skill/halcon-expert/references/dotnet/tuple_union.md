# TupleUnion (Operator)

## Name

`TupleUnion` — Compute the union set of two input tuples.

## Signature

`static void HOperatorSet.TupleUnion(HTuple set1, HTuple set2, out HTuple union)`

`HTuple HTuple.TupleUnion(HTuple set2)`

## Description

`TupleUnion` returns the union set from
*`set1`* and *`set2`* in *`union`*. For example,
if *`set1`* contains the values [0,1,3,3,5] and *`set2`*
contains the values [3,4], the output *`union`* is [0,1,3,4,5].
The operator also allows mixed types of elements in the input tuples.
However, the elements with different types will be considered as
different elements, i.e. 1.0 and 1 are different. For example,
the union of [2,5,3] and [4.0,5.0] is [2,3,5,4.0,5.0]. Please note
that the order of tuple elements resulting from `TupleUnion`
does not necessarily conform to the order in the input tuple.

### Exception: Empty input tuples

If both of the input tuples are empty, the operator returns an
empty tuple. If one of the input tuples is empty and the other is not,
the output corresponds to the input tuple that is not empty.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleUnion`,
which can be used in an expression in the following syntax:

[`Union := union(Set1, Set2)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_set_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`set1`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string / HHandle)

Input tuple.

**`set2`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string / HHandle)

Input tuple.

**`union`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string / HHandle)

The union set of two input tuples.

## Result

If the parameters are valid, the operator
`TupleUnion` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`TupleIntersection`

## See also

`TupleDifference`,
`TupleIntersection`,
`TupleSymmdiff`

## Module

Foundation
