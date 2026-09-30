# TupleMax (Operator)

## Name

`TupleMax` — Return the maximal element of a tuple.

## Signature

`static void HOperatorSet.TupleMax(HTuple tuple, out HTuple max)`

`HTuple HTuple.TupleMax()`

## Description

`TupleMax` returns the maximal element of all elements
of the input tuple *`tuple`*. All elements of *`tuple`*
either have to be strings or numbers (integer or floating point numbers).
It is not allowed to mix strings with numerical values. The result
parameter *`max`* will contain a floating point number, if
at least one element of *`tuple`* is a floating point number.
If all elements of *`tuple`* are integer numbers the resulting
maximum in *`max`* will also be an integer number.

### Exception: Empty input tuple

If the input tuple is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleMax`,
which can be used in an expression in the following syntax:

[`Max := max(Tuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple.

**`max`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Maximal element of the input tuple elements.

## Alternatives

`TupleMin`,
`TupleMean`,
`TupleDeviation`,
`TupleSum`,
`TupleLength`,
`TupleMedian`

## See also

`TupleMax2`,
`TupleMin2`

## Module

Foundation
