# TupleIntersection (Operator)

## Name

`TupleIntersection` — Compute the intersection set of two input tuples.

## Signature

`static void HOperatorSet.TupleIntersection(HTuple set1, HTuple set2, out HTuple intersection)`

`HTuple HTuple.TupleIntersection(HTuple set2)`

## Description

`TupleIntersection` returns the intersection set from
*`set1`* and *`set2`* in *`intersection`*. For example,
if *`set1`* contains the values [0,1,3,3,5] and *`set2`*
contains the values [2,3,5,10], the output *`intersection`* is [3,5].
The operator also allows mixed types of elements in the input tuples.
However, the elements with different types will be considered as
different elements, i.e. 1.0 and 1 are different. Also, this means, if
*`set1`* and *`set2`* have different types of elements, their
intersection set could be empty. For example, if *`set1`* contains
the values [2,5,3] and *`set2`* contains the values [2.0,5.0,0,10], the
output *`intersection`* is empty. Please note that the order of tuple
elements resulting from `TupleIntersection` does not necessarily
conform to the order in the input tuple.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleIntersection`,
which can be used in an expression in the following syntax:

[`Intersection := intersection(Set1, Set2)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_set_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`set1`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string / HHandle)

Input tuple.

**`set2`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string / HHandle)

Input tuple.

**`intersection`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string / HHandle)

The intersection set of two input tuples.

## Result

If the parameters are valid, the operator
`TupleIntersection` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`TupleUnion`

## See also

`TupleDifference`,
`TupleSymmdiff`,
`TupleUnion`

## Module

Foundation
