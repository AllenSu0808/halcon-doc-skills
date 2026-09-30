# tuple_intersection (Operator)

## Name

`tuple_intersection` — Compute the intersection set of two input tuples.

## Signature

`def tuple_intersection(set_1: HTupleType, set_2: HTupleType) -> Sequence[HTupleElementType]`

`def tuple_intersection_s(set_1: HTupleType, set_2: HTupleType) -> HTupleElementType`

## Description

`tuple_intersection` returns the intersection set from
*`set_1`* and *`set_2`* in *`intersection`*. For example,
if *`set_1`* contains the values [0,1,3,3,5] and *`set_2`*
contains the values [2,3,5,10], the output *`intersection`* is [3,5].
The operator also allows mixed types of elements in the input tuples.
However, the elements with different types will be considered as
different elements, i.e. 1.0 and 1 are different. Also, this means, if
*`set_1`* and *`set_2`* have different types of elements, their
intersection set could be empty. For example, if *`set_1`* contains
the values [2,5,3] and *`set_2`* contains the values [2.0,5.0,0,10], the
output *`intersection`* is empty. Please note that the order of tuple
elements resulting from `tuple_intersection` does not necessarily
conform to the order in the input tuple.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_intersection`,
which can be used in an expression in the following syntax:

[`Intersection := intersection(Set1, Set2)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_set_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`set_1`** (input_control)  tuple(-array) `→` HTupleType

Input tuple.

**`set_2`** (input_control)  tuple(-array) `→` HTupleType

Input tuple.

**`intersection`** (output_control)  tuple(-array) `→` Sequence[HTupleElementType]

The intersection set of two input tuples.

## Result

If the parameters are valid, the operator
`tuple_intersection` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`tuple_union`

## See also

`tuple_difference`,
`tuple_symmdiff`,
`tuple_union`

## Module

Foundation
