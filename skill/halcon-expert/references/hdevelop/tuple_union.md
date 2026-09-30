# tuple_union (Operator)

## Name

`tuple_union` — Compute the union set of two input tuples.

## Signature

`tuple_union( : : Set1, Set2 : Union)`

## Description

`tuple_union` returns the union set from
*`Set1`* and *`Set2`* in *`Union`*. For example,
if *`Set1`* contains the values [0,1,3,3,5] and *`Set2`*
contains the values [3,4], the output *`Union`* is [0,1,3,4,5].
The operator also allows mixed types of elements in the input tuples.
However, the elements with different types will be considered as
different elements, i.e. 1.0 and 1 are different. For example,
the union of [2,5,3] and [4.0,5.0] is [2,3,5,4.0,5.0]. Please note
that the order of tuple elements resulting from `tuple_union`
does not necessarily conform to the order in the input tuple.

### Exception: Empty input tuples

If both of the input tuples are empty, the operator returns an
empty tuple. If one of the input tuples is empty and the other is not,
the output corresponds to the input tuple that is not empty.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_union`,
which can be used in an expression in the following syntax:

[`Union := union(Set1, Set2)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_set_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Set1`** (input_control)  tuple(-array) `→`  (integer / real / string / handle)

Input tuple.

**`Set2`** (input_control)  tuple(-array) `→`  (integer / real / string / handle)

Input tuple.

**`Union`** (output_control)  tuple(-array) `→`  (integer / real / string / handle)

The union set of two input tuples.

## Result

If the parameters are valid, the operator
`tuple_union` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`tuple_intersection`

## See also

`tuple_difference`,
`tuple_intersection`,
`tuple_symmdiff`

## Module

Foundation
