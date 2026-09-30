# tuple_length (Operator)

## Name

`tuple_length` — Return the number of elements of a tuple.

## Signature

`def tuple_length(tuple: MaybeSequence[Union[float, int, str]]) -> int`

## Description

`tuple_length` returns the number of elements of the input tuple
*`tuple`*.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns 0.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_length`,
which can be used in an expression in the following syntax:

[`Length := |Tuple|`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` MaybeSequence[Union[float, int, str]]

Input tuple.

**`length`** (output_control)  integer `→` int

Number of elements of input tuple.

## Alternatives

`tuple_min`,
`tuple_max`,
`tuple_mean`,
`tuple_deviation`,
`tuple_sum`,
`tuple_median`

## See also

`tuple_type`

## Module

Foundation
