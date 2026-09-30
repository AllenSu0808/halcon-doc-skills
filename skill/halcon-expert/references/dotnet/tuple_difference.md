# TupleDifference (Operator)

## Name

`TupleDifference` — Compute the difference set of two input tuples.

## Signature

`static void HOperatorSet.TupleDifference(HTuple set1, HTuple set2, out HTuple difference)`

`HTuple HTuple.TupleDifference(HTuple set2)`

## Description

`TupleDifference` returns the difference set from
*`set1`* and *`set2`* in *`difference`*. For example,
if *`set1`* contains the values [0,1,3,3,5] and *`set2`*
contains the values [2,3,5,10], the output *`difference`* is [0,1].
The operator also allows mixed types of elements in the input tuples.
However, the elements with different types will be considered as
different elements, i.e. 1.0 and 1 are different. Also, this means, if
*`set1`* and *`set2`* have different types of elements, their
difference set could be *`set1`* itself. For example, if *`set1`*
contains the values [2,5,3] and *`set2`* contains the values
[2.0,5.0,3.0], the output *`difference`* is [2,3,5]. Please note that
the order of tuple elements resulting from `TupleDifference` does
not necessarily conform to the order in the input tuple.

### Exception: Empty input tuples

If both input tuples are empty, the operator returns an empty tuple. If
*`set1`* is empty and *`set2`* is not, the operator returns
an empty tuple as well. If *`set2`* is empty and *`set1`* is
not, the output corresponds to *`set1`*.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleDifference`,
which can be used in an expression in the following syntax:

[`Difference := difference(Set1, Set2)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_set_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`set1`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string / HHandle)

Input tuple.

**`set2`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string / HHandle)

Input tuple.

**`difference`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string / HHandle)

The difference set of two input tuples.

## Result

If the parameters are valid, the operator
`TupleDifference` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`TupleSymmdiff`

## See also

`TupleIntersection`,
`TupleSymmdiff`,
`TupleUnion`

## Module

Foundation
