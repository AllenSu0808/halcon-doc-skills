# tuple_greater_equal_elem (Operator)

## Name

`tuple_greater_equal_elem` — Test, whether a tuple is elementwise greater or equal to another tuple.

## Signature

`def tuple_greater_equal_elem(t1: MaybeSequence[Union[int, float, str]], t2: MaybeSequence[Union[int, float, str]]) -> Sequence[int]`

`def tuple_greater_equal_elem_s(t1: MaybeSequence[Union[int, float, str]], t2: MaybeSequence[Union[int, float, str]]) -> int`

## Description

`tuple_greater_equal_elem` tests elementwise whether the input tuple
*`t1`* is greater than or equal to *`t2`*.
If both tuples have the same length, the corresponding
elements of both tuples are compared. Otherwise, either *`t1`*
or *`t2`* must have length 1. In this case, the comparison is
performed for each element of the longer tuple with the single element
of the other tuple. As a precondition for comparing the tuples elementwise
two corresponding elements must either both be (integer or floating point)
numbers or both be strings. Otherwise `tuple_greater_equal_elem`
returns an error.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_greater_equal_elem`,
which can be used in an expression in the following syntax:

[`Greatereq := T1 [>=] T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_comparison_elem_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t1`** (input_control)  tuple(-array) `→` MaybeSequence[Union[int, float, str]]

Input tuple 1.

**`t2`** (input_control)  tuple(-array) `→` MaybeSequence[Union[int, float, str]]

Input tuple 2.

**`greatereq`** (output_control)  integer(-array) `→` Sequence[int]

Result of the comparison of the input tuples.

## Alternatives

`tuple_equal_elem`,
`tuple_not_equal_elem`,
`tuple_less_elem`,
`tuple_greater_elem`,
`tuple_less_equal_elem`,
`tuple_equal`,
`tuple_not_equal`,
`tuple_less`,
`tuple_greater`,
`tuple_less_equal`,
`tuple_greater_equal`

## Module

Foundation
