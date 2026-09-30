# TupleDeviation (Operator)

## Name

`TupleDeviation` — Return the standard deviation of the elements of a tuple.

## Signature

`static void HOperatorSet.TupleDeviation(HTuple tuple, out HTuple deviation)`

`HTuple HTuple.TupleDeviation()`

## Description

`TupleDeviation` calculates the standard deviation of
all elements of the input tuple *`tuple`*. It returns the
deviation as a floating point number in the output parameter
*`deviation`*. The input tuple may only consist of numbers
(integer or floating point numbers).

### Exception: Empty input tuple

If the input tuple is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleDeviation`,
which can be used in an expression in the following syntax:

[`Deviation := deviation(Tuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

Input tuple.

**`deviation`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Standard deviation of tuple elements.

## Alternatives

`TupleMean`,
`TupleSum`,
`TupleMin`,
`TupleMax`,
`TupleLength`,
`TupleMedian`

## Module

Foundation
