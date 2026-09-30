# tuple_difference (Operator)

## Name

`tuple_difference` — Compute the difference set of two input tuples.

## Signature

`tuple_difference( : : Set1, Set2 : Difference)`

## Description

`tuple_difference` returns the difference set from
*`Set1`* and *`Set2`* in *`Difference`*. For example,
if *`Set1`* contains the values [0,1,3,3,5] and *`Set2`*
contains the values [2,3,5,10], the output *`Difference`* is [0,1].
The operator also allows mixed types of elements in the input tuples.
However, the elements with different types will be considered as
different elements, i.e. 1.0 and 1 are different. Also, this means, if
*`Set1`* and *`Set2`* have different types of elements, their
difference set could be *`Set1`* itself. For example, if *`Set1`*
contains the values [2,5,3] and *`Set2`* contains the values
[2.0,5.0,3.0], the output *`Difference`* is [2,3,5]. Please note that
the order of tuple elements resulting from `tuple_difference` does
not necessarily conform to the order in the input tuple.

### Exception: Empty input tuples

If both input tuples are empty, the operator returns an empty tuple. If
*`Set1`* is empty and *`Set2`* is not, the operator returns
an empty tuple as well. If *`Set2`* is empty and *`Set1`* is
not, the output corresponds to *`Set1`*.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_difference`,
which can be used in an expression in the following syntax:

[`Difference := difference(Set1, Set2)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_set_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Set1`** (input_control)  tuple(-array) `→`  (integer / real / string / handle)

Input tuple.

**`Set2`** (input_control)  tuple(-array) `→`  (integer / real / string / handle)

Input tuple.

**`Difference`** (output_control)  tuple(-array) `→`  (integer / real / string / handle)

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
