# tuple_select_rank (Operator)

## Name

`tuple_select_rank` — Select the element of rank n of a tuple.

## Signature

`tuple_select_rank( : : Tuple, RankIndex : Selected)`

## Description

`tuple_select_rank` sorts the elements of the tuple
*`Tuple`* and returns the element of rank n in *`Selected`*.
*`RankIndex`* determines the index of the element to select.
Thus, *`RankIndex`* may only contain integer values (any floating point
number in *`RankIndex`* must represent an integer value without
fraction). Indices of tuple elements start at 0, i.e. the lowest
tuple element has the index 0.

### Exception: Empty input tuples

If *`RankIndex`* is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_select_rank`,
which can be used in an expression in the following syntax:

[`Selected := select_rank(Tuple, RankIndex)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Tuple`** (input_control)  number(-array) `→`  (integer / real)

Input tuple.

**`RankIndex`** (input_control)  number `→`  (integer / real)

Rank of the element to select.

**`Selected`** (output_control)  number `→`  (integer / real)

Selected tuple element.

## Alternatives

`tuple_sort_index`,
`tuple_sort`

## See also

`tuple_median`,
`tuple_select`

## Module

Foundation
