# tuple_mean (Operator)

## Name

`tuple_mean` — Return the mean value of a tuple of numbers.

## Signature

`def tuple_mean(tuple: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_mean` returns the mean value of all elements
of the input tuple *`tuple`* as a floating point
number in the output parameter *`mean`*. The input tuple
may only consist of numbers (integer or floating point numbers).

### Exception: Empty input tuple

If the input tuple is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_mean`,
which can be used in an expression in the following syntax:

[`Mean := mean(Tuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`mean`** (output_control)  number `→` float

Mean value of tuple elements.

## Alternatives

`tuple_deviation`,
`tuple_sum`,
`tuple_min`,
`tuple_max`,
`tuple_length`,
`tuple_median`

## Module

Foundation
