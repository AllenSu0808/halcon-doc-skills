# tuple_sum (Operator)

## Name

`tuple_sum` — Return the sum of all elements of a tuple.

## Signature

`def tuple_sum(tuple: MaybeSequence[Union[float, int, str]]) -> Sequence[Union[float, int, str]]`

`def tuple_sum_s(tuple: MaybeSequence[Union[float, int, str]]) -> Union[float, int, str]`

## Description

`tuple_sum` returns the sum of all elements
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

HDevelop provides an in-line operation for `tuple_sum`,
which can be used in an expression in the following syntax:

[`Sum := sum(Tuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` MaybeSequence[Union[float, int, str]]

Input tuple.

**`sum`** (output_control)  tuple(-array) `→` Sequence[Union[float, int, str]]

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
