# tuple_median (Operator)

## Name

`tuple_median` — Return the median of the elements of a tuple.

## Signature

`def tuple_median(tuple: MaybeSequence[Union[float, int]]) -> Union[int, float]`

## Description

`tuple_median` calculates the median of all elements of the
input tuple *`tuple`* and returns it in the output parameter
*`median`*. The input tuple may only consist of numbers
(integer or floating point numbers). The median is defined as the
element with rank n/2 (see [`tuple_select_rank`](tuple_select_rank.md)).

Note that for an even number of input elements, this will return the upper
median, not the arithmetic median. To calculate the arithmetic median, you
can use [`tuple_select_rank`](tuple_select_rank.md) to select the upper and lower median values
and then calculate the arithmetic mean of both values.

### Exception: Empty input tuple

If the input tuple is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_median`,
which can be used in an expression in the following syntax:

[`Median := median(Tuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`median`** (output_control)  number `→` Union[int, float]

Median of the tuple elements.

## Alternatives

`tuple_select_rank`

## See also

`tuple_mean`,
`tuple_min`,
`tuple_max`

## Module

Foundation
