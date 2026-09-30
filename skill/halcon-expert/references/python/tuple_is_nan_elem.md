# tuple_is_nan_elem (Operator)

## Name

`tuple_is_nan_elem` — Check a tuple whether it represents NaNs (Not-a-number).

## Signature

`def tuple_is_nan_elem(t: MaybeSequence[Union[float, int]]) -> int`

## Description

`tuple_is_nan_elem` checks each element of the input tuple
*`t`* whether it represents a NaN. If it does, 1 is
returned for that element, otherwise 0.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_is_nan_elem`,
which can be used in an expression in the following syntax:

[`IsNaN := is_nan_elem(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  tuple(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`is_na_n`** (output_control)  number `→` int

Tuple with Boolean numbers.

## Alternatives

`tuple_type`,
`tuple_is_number`,
`tuple_sem_type`

## See also

`tuple_is_int`,
`tuple_is_real`,
`tuple_is_string`

## Module

Foundation
