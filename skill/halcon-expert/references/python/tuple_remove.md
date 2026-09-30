# tuple_remove (Operator)

## Name

`tuple_remove` — Remove elements from a tuple.

## Signature

`def tuple_remove(tuple: MaybeSequence[Union[float, int, str]], index: MaybeSequence[int]) -> Sequence[Union[float, int, str]]`

`def tuple_remove_s(tuple: MaybeSequence[Union[float, int, str]], index: MaybeSequence[int]) -> Union[float, int, str]`

## Description

`tuple_remove` removes one or more elements from the tuple
*`tuple`* and returns the rest in the tuple *`reduced`*.
*`index`* determines the indices of the elements to remove. Thus,
*`index`* may only contain integer values (any floating point
number within *`index`* must represent an integer value without
fraction). Note that indices of tuple elements start at 0, i.e. the first
tuple element has got the index 0. Duplicates and indices out of
range are ignored.

### Exception: Empty input tuple

If *`tuple`* is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_remove`,
which can be used in an expression in the following syntax:

[`Reduced := remove(Tuple, Index)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` MaybeSequence[Union[float, int, str]]

Input tuple.

**`index`** (input_control)  integer(-array) `→` MaybeSequence[int]

Indices of the elements to remove.

**`reduced`** (output_control)  tuple(-array) `→` Sequence[Union[float, int, str]]

Reduced tuple.

## Alternatives

`tuple_first_n`,
`tuple_last_n`,
`tuple_str_bit_select`,
`tuple_concat`,
`tuple_insert`,
`tuple_replace`

## See also

`tuple_select`,
`tuple_select_mask`

## Module

Foundation
