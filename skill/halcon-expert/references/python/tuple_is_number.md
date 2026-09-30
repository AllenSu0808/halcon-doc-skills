# tuple_is_number (Operator)

## Name

`tuple_is_number` — Check a tuple (of strings) whether it represents numbers.

## Signature

`def tuple_is_number(t: MaybeSequence[Union[float, int, str]]) -> Sequence[int]`

`def tuple_is_number_s(t: MaybeSequence[Union[float, int, str]]) -> int`

## Description

`tuple_is_number` checks each element of the input tuple
*`t`* whether it represents a number. If the element is a
number (`real` or `integer`), 1 is returned for that element.
If the element is a string, it is checked whether the string represents a
number. If so, 1 is returned, otherwise 0.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_is_number`,
which can be used in an expression in the following syntax:

[`IsNumber := is_number(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  tuple(-array) `→` MaybeSequence[Union[float, int, str]]

Input tuple.

**`is_number`** (output_control)  integer(-array) `→` Sequence[int]

Tuple with Boolean numbers.

## Alternatives

`tuple_is_int`,
`tuple_is_real`,
`tuple_type`,
`tuple_is_nan_elem`

## See also

`tuple_number`

## Module

Foundation
