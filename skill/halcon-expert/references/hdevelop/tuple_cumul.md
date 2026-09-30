# tuple_cumul (Operator)

## Name

`tuple_cumul` — Calculate the cumulative sums of a tuple.

## Signature

`tuple_cumul( : : Tuple : Cumul)`

## Description

`tuple_cumul` returns the different cumulative sums of the
corresponding elements of the input tuple *`Tuple`*, i.e. the i-th
element of the result tuple *`Cumul`* is the sum of the first i
elements of the input tuple *`Tuple`*. For example, if
*`Tuple`* contains the values [1,2,3,4], the output tuple
*`Cumul`* will contain the values [1,3,6,10].
All elements of *`Tuple`*
must be numbers (integer or floating point numbers). Each element
of the result tuple *`Cumul`* will contain a floating point number if
at least one element of the calculation is a floating point number.
If all elements of the calculation are integer numbers the resulting
sum in *`Cumul`* will also be an integer number.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_cumul`,
which can be used in an expression in the following syntax:

[`Cumul := cumul(Tuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Tuple`** (input_control)  number(-array) `→`  (integer / real)

Input tuple.

**`Cumul`** (output_control)  number(-array) `→`  (real / integer)

Cumulative sum of the corresponding tuple elements.

## Alternatives

`tuple_sum`

## See also

`tuple_min2`,
`tuple_max2`,
`tuple_add`

## Module

Foundation
