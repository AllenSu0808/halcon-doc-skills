# TupleSymmdiff (Operator)

## Name

`TupleSymmdiff` — Compute the symmetric difference set of two input tuples.

## Signature

`static void HOperatorSet.TupleSymmdiff(HTuple set1, HTuple set2, out HTuple symmDiff)`

`HTuple HTuple.TupleSymmdiff(HTuple set2)`

## Description

`TupleSymmdiff` returns the symmetric difference set from
*`set1`* and *`set2`* in *`symmDiff`*. For example,
if *`set1`* contains the values [0,1,3,3,5] and *`set2`*
contains the values [2,3,5,10], the output *`symmDiff`* is [0,1,2,10].
The operator also allows mixed types of elements in the input tuples.
However, the elements with different types will be considered as
different elements, i.e. 1.0 and 1 are different. Also, this means, if
*`set1`* and *`set2`* have different types of elements, their
symmetric difference set could be the union. For example, if *`set1`*
contains the values [2,5,3] and *`set2`* contains the values [2.0,5.0],
the output *`symmDiff`* is [2,3,5,2.0,5.0]. Please note that the order
of tuple elements resulting from `TupleSymmdiff` does not necessarily
conform to the order in the input tuple.

### Exception: Empty input tuples

If both of the input tuples are empty, the operator returns an
empty tuple. If one of the input tuples is empty and the other is not,
the output corresponds to the input tuple that is not empty.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleSymmdiff`,
which can be used in an expression in the following syntax:

[`SymmDiff := symmdiff(Set1, Set2)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_set_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`set1`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string / HHandle)

Input tuple.

**`set2`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string / HHandle)

Input tuple.

**`symmDiff`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string / HHandle)

The symmetric difference set of two input tuples.

## Result

If the parameters are valid, the operator
`TupleSymmdiff` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`TupleDifference`

## See also

`TupleDifference`,
`TupleIntersection`,
`TupleUnion`

## Module

Foundation
