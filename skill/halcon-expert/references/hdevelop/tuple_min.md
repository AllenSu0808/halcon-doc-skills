# tuple_min (Operator)

## Name

`tuple_min` — Return the minimal element of a tuple.

## Signature

`tuple_min( : : Tuple : Min)`

## Description

`tuple_min` returns the minimal element of all elements
of the input tuple *`Tuple`*. All elements of *`Tuple`*
either have to be strings or numbers (integer or floating point numbers).
It is not allowed to mix strings with numerical values. The result
parameter *`Min`* will contain a floating point number, if
at least one element of *`Tuple`* is a floating point number.
If all elements of *`Tuple`* are integer numbers the resulting
minimum in *`Min`* will also be an integer number.

### Exception: Empty input tuple

If the input tuple is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_min`,
which can be used in an expression in the following syntax:

[`Min := min(Tuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Tuple`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple.

**`Min`** (output_control)  tuple(-array) `→`  (real / integer / string)

Minimal element of the input tuple elements.

## Alternatives

`tuple_max`,
`tuple_mean`,
`tuple_deviation`,
`tuple_sum`,
`tuple_length`,
`tuple_median`

## See also

`tuple_max2`,
`tuple_min2`

## Module

Foundation
