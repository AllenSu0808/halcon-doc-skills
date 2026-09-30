# tuple_select_rank (Operator)

## Name

`tuple_select_rank` — Select the element of rank n of a tuple.

## Signature

`def tuple_select_rank(tuple: MaybeSequence[Union[float, int]], rank_index: Union[float, int]) -> Union[float, int]`

## Description

`tuple_select_rank` sorts the elements of the tuple
*`tuple`* and returns the element of rank n in *`selected`*.
*`rank_index`* determines the index of the element to select.
Thus, *`rank_index`* may only contain integer values (any floating point
number in *`rank_index`* must represent an integer value without
fraction). Indices of tuple elements start at 0, i.e. the lowest
tuple element has the index 0.

### Exception: Empty input tuples

If *`rank_index`* is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_select_rank`,
which can be used in an expression in the following syntax:

[`Selected := select_rank(Tuple, RankIndex)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`rank_index`** (input_control)  number `→` Union[float, int]

Rank of the element to select.

**`selected`** (output_control)  number `→` Union[float, int]

Selected tuple element.

## Alternatives

`tuple_sort_index`,
`tuple_sort`

## See also

`tuple_median`,
`tuple_select`

## Module

Foundation
