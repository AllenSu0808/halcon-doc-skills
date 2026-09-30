# tuple_sum (Operator)

## Name

`tuple_sum` — Return the sum of all elements of a tuple.

## Signature

`tuple_sum( : : Tuple : Sum)`

## Description

`tuple_sum` returns the sum of all elements
of the input tuple *`Tuple`*. All elements of *`Tuple`*
either have to be strings or numbers (integer or floating point numbers).
It is not allowed to mix strings with numerical values. The result
parameter *`Sum`* will contain a floating point number, if
at least one element of *`Tuple`* is a floating point number.
If all elements of *`Tuple`* are integer numbers the resulting
sum will also be an integer number. If *`Tuple`* contains strings,
the concatenation will be used for building the sum.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_sum`,
which can be used in an expression in the following syntax:

[`Sum := sum(Tuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Tuple`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple.

**`Sum`** (output_control)  tuple(-array) `→`  (real / integer / string)

Sum of tuple elements.

## Alternatives

`tuple_mean`,
`tuple_deviation`,
`tuple_min`,
`tuple_max`,
`tuple_length`,
`tuple_median`

## See also

`tuple_cumul`

## Module

Foundation
