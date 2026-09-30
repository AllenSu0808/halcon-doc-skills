# tuple_symmdiff (Operator)

## Name

`tuple_symmdiff` — Compute the symmetric difference set of two input tuples.

## Signature

`tuple_symmdiff( : : Set1, Set2 : SymmDiff)`

## Description

`tuple_symmdiff` returns the symmetric difference set from
*`Set1`* and *`Set2`* in *`SymmDiff`*. For example,
if *`Set1`* contains the values [0,1,3,3,5] and *`Set2`*
contains the values [2,3,5,10], the output *`SymmDiff`* is [0,1,2,10].
The operator also allows mixed types of elements in the input tuples.
However, the elements with different types will be considered as
different elements, i.e. 1.0 and 1 are different. Also, this means, if
*`Set1`* and *`Set2`* have different types of elements, their
symmetric difference set could be the union. For example, if *`Set1`*
contains the values [2,5,3] and *`Set2`* contains the values [2.0,5.0],
the output *`SymmDiff`* is [2,3,5,2.0,5.0]. Please note that the order
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

**`Set1`** (input_control)  tuple(-array) `→`  (integer / real / string / handle)

Input tuple.

**`Set2`** (input_control)  tuple(-array) `→`  (integer / real / string / handle)

Input tuple.

**`SymmDiff`** (output_control)  tuple(-array) `→`  (integer / real / string / handle)

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
