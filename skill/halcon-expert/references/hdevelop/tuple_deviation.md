# tuple_deviation (Operator)

## Name

`tuple_deviation` — Return the standard deviation of the elements of a tuple.

## Signature

`tuple_deviation( : : Tuple : Deviation)`

## Description

`tuple_deviation` calculates the standard deviation of
all elements of the input tuple *`Tuple`*. It returns the
deviation as a floating point number in the output parameter
*`Deviation`*. The input tuple may only consist of numbers
(integer or floating point numbers).

### Exception: Empty input tuple

If the input tuple is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_deviation`,
which can be used in an expression in the following syntax:

[`Deviation := deviation(Tuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Tuple`** (input_control)  number(-array) `→`  (integer / real)

Input tuple.

**`Deviation`** (output_control)  number(-array) `→`  (real)

Standard deviation of tuple elements.

## Alternatives

`tuple_mean`,
`tuple_sum`,
`tuple_min`,
`tuple_max`,
`tuple_length`,
`tuple_median`

## Module

Foundation
