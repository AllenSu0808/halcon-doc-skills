# TupleMean (Operator)

## Name

`TupleMean` — Return the mean value of a tuple of numbers.

## Signature

`static void HOperatorSet.TupleMean(HTuple tuple, out HTuple mean)`

`HTuple HTuple.TupleMean()`

## Description

`TupleMean` returns the mean value of all elements
of the input tuple *`tuple`* as a floating point
number in the output parameter *`mean`*. The input tuple
may only consist of numbers (integer or floating point numbers).

### Exception: Empty input tuple

If the input tuple is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleMean`,
which can be used in an expression in the following syntax:

[`Mean := mean(Tuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

Input tuple.

**`mean`** (output_control)  number `→` [HTuple](HTuple.md) (*double*)

Mean value of tuple elements.

## Alternatives

`TupleDeviation`,
`TupleSum`,
`TupleMin`,
`TupleMax`,
`TupleLength`,
`TupleMedian`

## Module

Foundation
