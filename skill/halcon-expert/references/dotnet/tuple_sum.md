# TupleSum (Operator)

## Name

`TupleSum` — Return the sum of all elements of a tuple.

## Signature

`static void HOperatorSet.TupleSum(HTuple tuple, out HTuple sum)`

`HTuple HTuple.TupleSum()`

## Description

`TupleSum` returns the sum of all elements
of the input tuple *`tuple`*. All elements of *`tuple`*
either have to be strings or numbers (integer or floating point numbers).
It is not allowed to mix strings with numerical values. The result
parameter *`sum`* will contain a floating point number, if
at least one element of *`tuple`* is a floating point number.
If all elements of *`tuple`* are integer numbers the resulting
sum will also be an integer number. If *`tuple`* contains strings,
the concatenation will be used for building the sum.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleSum`,
which can be used in an expression in the following syntax:

[`Sum := sum(Tuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple.

**`sum`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Sum of tuple elements.

## Alternatives

`TupleMean`,
`TupleDeviation`,
`TupleMin`,
`TupleMax`,
`TupleLength`,
`TupleMedian`

## See also

`TupleCumul`

## Module

Foundation
