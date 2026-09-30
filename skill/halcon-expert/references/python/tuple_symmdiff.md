# tuple_symmdiff (Operator)

## Name

`tuple_symmdiff` — Compute the symmetric difference set of two input tuples.

## Signature

`def tuple_symmdiff(set_1: HTupleType, set_2: HTupleType) -> Sequence[HTupleElementType]`

`def tuple_symmdiff_s(set_1: HTupleType, set_2: HTupleType) -> HTupleElementType`

## Description

`tuple_symmdiff` returns the symmetric difference set from
*`set_1`* and *`set_2`* in *`symm_diff`*. For example,
if *`set_1`* contains the values [0,1,3,3,5] and *`set_2`*
contains the values [2,3,5,10], the output *`symm_diff`* is [0,1,2,10].
The operator also allows mixed types of elements in the input tuples.
However, the elements with different types will be considered as
different elements, i.e. 1.0 and 1 are different. Also, this means, if
*`set_1`* and *`set_2`* have different types of elements, their
symmetric difference set could be the union. For example, if *`set_1`*
contains the values [2,5,3] and *`set_2`* contains the values [2.0,5.0],
the output *`symm_diff`* is [2,3,5,2.0,5.0]. Please note that the order
of tuple elements resulting from `tuple_symmdiff` does not necessarily
conform to the order in the input tuple.

### Exception: Empty input tuples

If both of the input tuples are empty, the operator returns an
empty tuple. If one of the input tuples is empty and the other is not,
the output corresponds to the input tuple that is not empty.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_symmdiff`,
which can be used in an expression in the following syntax:

[`SymmDiff := symmdiff(Set1, Set2)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_set_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`set_1`** (input_control)  tuple(-array) `→` HTupleType

Input tuple.

**`set_2`** (input_control)  tuple(-array) `→` HTupleType

Input tuple.

**`symm_diff`** (output_control)  tuple(-array) `→` Sequence[HTupleElementType]

The symmetric difference set of two input tuples.

## Result

If the parameters are valid, the operator
`tuple_symmdiff` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`tuple_difference`

## See also

`tuple_difference`,
`tuple_intersection`,
`tuple_union`

## Module

Foundation
