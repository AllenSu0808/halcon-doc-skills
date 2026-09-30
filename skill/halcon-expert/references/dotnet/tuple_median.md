# TupleMedian (Operator)

## Name

`TupleMedian` — Return the median of the elements of a tuple.

## Signature

`static void HOperatorSet.TupleMedian(HTuple tuple, out HTuple median)`

`HTuple HTuple.TupleMedian()`

## Description

`TupleMedian` calculates the median of all elements of the
input tuple *`tuple`* and returns it in the output parameter
*`median`*. The input tuple may only consist of numbers
(integer or floating point numbers). The median is defined as the
element with rank n/2 (see [`TupleSelectRank`](tuple_select_rank.md)).

Note that for an even number of input elements, this will return the upper
median, not the arithmetic median. To calculate the arithmetic median, you
can use [`TupleSelectRank`](tuple_select_rank.md) to select the upper and lower median values
and then calculate the arithmetic mean of both values.

### Exception: Empty input tuple

If the input tuple is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleMedian`,
which can be used in an expression in the following syntax:

[`Median := median(Tuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

Input tuple.

**`median`** (output_control)  number `→` [HTuple](HTuple.md) (*int* / long / double)

Median of the tuple elements.

## Alternatives

`TupleSelectRank`

## See also

`TupleMean`,
`TupleMin`,
`TupleMax`

## Module

Foundation
