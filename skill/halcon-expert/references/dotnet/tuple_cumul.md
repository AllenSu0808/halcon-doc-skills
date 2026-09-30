# TupleCumul (Operator)

## Name

`TupleCumul` — Calculate the cumulative sums of a tuple.

## Signature

`static void HOperatorSet.TupleCumul(HTuple tuple, out HTuple cumul)`

`HTuple HTuple.TupleCumul()`

## Description

`TupleCumul` returns the different cumulative sums of the
corresponding elements of the input tuple *`tuple`*, i.e. the i-th
element of the result tuple *`cumul`* is the sum of the first i
elements of the input tuple *`tuple`*. For example, if
*`tuple`* contains the values [1,2,3,4], the output tuple
*`cumul`* will contain the values [1,3,6,10].
All elements of *`tuple`*
must be numbers (integer or floating point numbers). Each element
of the result tuple *`cumul`* will contain a floating point number if
at least one element of the calculation is a floating point number.
If all elements of the calculation are integer numbers the resulting
sum in *`cumul`* will also be an integer number.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleCumul`,
which can be used in an expression in the following syntax:

[`Cumul := cumul(Tuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

Input tuple.

**`cumul`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Cumulative sum of the corresponding tuple elements.

## Alternatives

`TupleSum`

## See also

`TupleMin2`,
`TupleMax2`,
`TupleAdd`

## Module

Foundation
