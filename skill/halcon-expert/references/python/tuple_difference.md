# tuple_difference (Operator)

## Name

`tuple_difference` — Compute the difference set of two input tuples.

## Signature

`def tuple_difference(set_1: HTupleType, set_2: HTupleType) -> Sequence[HTupleElementType]`

`def tuple_difference_s(set_1: HTupleType, set_2: HTupleType) -> HTupleElementType`

## Description

`tuple_difference` returns the difference set from
*`set_1`* and *`set_2`* in *`difference`*. For example,
if *`set_1`* contains the values [0,1,3,3,5] and *`set_2`*
contains the values [2,3,5,10], the output *`difference`* is [0,1].
The operator also allows mixed types of elements in the input tuples.
However, the elements with different types will be considered as
different elements, i.e. 1.0 and 1 are different. Also, this means, if
*`set_1`* and *`set_2`* have different types of elements, their
difference set could be *`set_1`* itself. For example, if *`set_1`*
contains the values [2,5,3] and *`set_2`* contains the values
[2.0,5.0,3.0], the output *`difference`* is [2,3,5]. Please note that
the order of tuple elements resulting from `tuple_difference` does
not necessarily conform to the order in the input tuple.

### Exception: Empty input tuples

If both input tuples are empty, the operator returns an empty tuple. If
*`set_1`* is empty and *`set_2`* is not, the operator returns
an empty tuple as well. If *`set_2`* is empty and *`set_1`* is
not, the output corresponds to *`set_1`*.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_difference`,
which can be used in an expression in the following syntax:

[`Difference := difference(Set1, Set2)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_set_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`set_1`** (input_control)  tuple(-array) `→` HTupleType

Input tuple.

**`set_2`** (input_control)  tuple(-array) `→` HTupleType

Input tuple.

**`difference`** (output_control)  tuple(-array) `→` Sequence[HTupleElementType]

The difference set of two input tuples.

## Result

If the parameters are valid, the operator
`tuple_difference` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`tuple_symmdiff`

## See also

`tuple_intersection`,
`tuple_symmdiff`,
`tuple_union`

## Module

Foundation
