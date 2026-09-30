# tuple_min2 (Operator)

## Name

`tuple_min2` — Calculate the elementwise minimum of two tuples.

## Signature

`def tuple_min2(t1: MaybeSequence[Union[float, int, str]], t2: MaybeSequence[Union[float, int, str]]) -> Sequence[Union[float, int, str]]`

`def tuple_min2_s(t1: MaybeSequence[Union[float, int, str]], t2: MaybeSequence[Union[float, int, str]]) -> Union[float, int, str]`

## Description

`tuple_min2` returns the elementwise minimum of the input
tuples *`t1`* and *`t2`* in the output tuple *`min_2`*.
If both tuples have the same length the corresponding elements of both
tuples are compared. Otherwise, either *`t1`* or *`t2`*
must have length 1. In this case, the comparison is performed for each
element of the longer tuple with the single element of the other
tuple. If the corresponding elements of the two tuples have the same
type, it is allowed to mix strings with numerical values.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_min2`,
which can be used in an expression in the following syntax:

[`Min2 := min2(T1, T2)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t1`** (input_control)  tuple(-array) `→` MaybeSequence[Union[float, int, str]]

Input tuple 1.

**`t2`** (input_control)  tuple(-array) `→` MaybeSequence[Union[float, int, str]]

Input tuple 2.

**`min_2`** (output_control)  tuple(-array) `→` Sequence[Union[float, int, str]]

Elementwise minimum of the input tuples.

## See also

`tuple_max2`,
`tuple_min`,
`tuple_max`

## Module

Foundation
