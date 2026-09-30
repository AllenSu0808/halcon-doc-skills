# tuple_equal (Operator)

## Name

`tuple_equal` — Test whether two tuples are equal.

## Signature

`def tuple_equal(t1: MaybeSequence[Union[int, float, str]], t2: MaybeSequence[Union[int, float, str]]) -> int`

## Description

`tuple_equal` tests whether the two input tuples *`t1`*
and *`t2`* are equal by comparing the tuples elementwise.
Two tuples are equal, if they have got the same number of elements and
if their elements are equal.
Two tuple elements are equal, if they are both (integer or floating point)
numbers or both are strings and contain the same value.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_equal`,
which can be used in an expression in the following syntax:

[`Equal := T1 == T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_comparison_0000.html)
or
[`Equal := T1 = T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_comparison_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t1`** (input_control)  tuple(-array) `→` MaybeSequence[Union[int, float, str]]

Input tuple 1.

**`t2`** (input_control)  tuple(-array) `→` MaybeSequence[Union[int, float, str]]

Input tuple 2.

**`equal`** (output_control)  integer `→` int

Result of the comparison of the input tuples.

## Alternatives

`tuple_not_equal`,
`tuple_less`,
`tuple_greater`,
`tuple_less_equal`,
`tuple_greater_equal`,
`tuple_equal_elem`,
`tuple_not_equal_elem`,
`tuple_less_elem`,
`tuple_greater_elem`,
`tuple_less_equal_elem`,
`tuple_greater_equal_elem`

## Module

Foundation
