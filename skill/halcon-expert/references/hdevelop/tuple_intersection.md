# tuple_intersection (Operator)

## Name

`tuple_intersection` — Compute the intersection set of two input tuples.

## Signature

`tuple_intersection( : : Set1, Set2 : Intersection)`

## Description

`tuple_intersection` returns the intersection set from
*`Set1`* and *`Set2`* in *`Intersection`*. For example,
if *`Set1`* contains the values [0,1,3,3,5] and *`Set2`*
contains the values [2,3,5,10], the output *`Intersection`* is [3,5].
The operator also allows mixed types of elements in the input tuples.
However, the elements with different types will be considered as
different elements, i.e. 1.0 and 1 are different. Also, this means, if
*`Set1`* and *`Set2`* have different types of elements, their
intersection set could be empty. For example, if *`Set1`* contains
the values [2,5,3] and *`Set2`* contains the values [2.0,5.0,0,10], the
output *`Intersection`* is empty. Please note that the order of tuple
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

**`Set1`** (input_control)  tuple(-array) `→`  (integer / real / string / handle)

Input tuple.

**`Set2`** (input_control)  tuple(-array) `→`  (integer / real / string / handle)

Input tuple.

**`Intersection`** (output_control)  tuple(-array) `→`  (integer / real / string / handle)

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
