# TupleSelectRank (Operator)

## Name

`TupleSelectRank` — Select the element of rank n of a tuple.

## Signature

`static void HOperatorSet.TupleSelectRank(HTuple tuple, HTuple rankIndex, out HTuple selected)`

`HTuple HTuple.TupleSelectRank(HTuple rankIndex)`

## Description

`TupleSelectRank` sorts the elements of the tuple
*`tuple`* and returns the element of rank n in *`selected`*.
*`rankIndex`* determines the index of the element to select.
Thus, *`rankIndex`* may only contain integer values (any floating point
number in *`rankIndex`* must represent an integer value without
fraction). Indices of tuple elements start at 0, i.e. the lowest
tuple element has the index 0.

### Exception: Empty input tuples

If *`rankIndex`* is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleSelectRank`,
which can be used in an expression in the following syntax:

[`Selected := select_rank(Tuple, RankIndex)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

Input tuple.

**`rankIndex`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long / double)

Rank of the element to select.

**`selected`** (output_control)  number `→` [HTuple](HTuple.md) (*int* / long / double)

Selected tuple element.

## Alternatives

`TupleSortIndex`,
`TupleSort`

## See also

`TupleMedian`,
`TupleSelect`

## Module

Foundation
