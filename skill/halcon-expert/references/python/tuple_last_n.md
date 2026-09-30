# tuple_last_n (Operator)

## Name

`tuple_last_n` — Select all elements from index “n” to the end of a tuple.

## Signature

`def tuple_last_n(tuple: MaybeSequence[Union[float, int, str]], index: int) -> Sequence[Union[float, int, str]]`

`def tuple_last_n_s(tuple: MaybeSequence[Union[float, int, str]], index: int) -> Union[float, int, str]`

## Description

Starting with the “n-th” element of the tuple *`tuple`*,
`tuple_last_n` selects every element of *`tuple`* and returns
it with *`selected`*. Thus, *`selected`* contains all
elements of *`tuple`* from index “n” up to the last element
of *`tuple`* (including the element at position “n”). The index
“n” is determined by the input parameter *`index`*. Thus,
*`index`* must contain a single integer value (if *`index`*
consists of a floating point number, this must represent
an integer value without fraction). Indices of tuple elements start at 0,
that means, the first tuple element has got the index 0.

### Exception: Empty input tuple

If *`tuple`* is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_last_n`,
which can be used in an expression in the following syntax:

[`Selected := lastn(Tuple, Index)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` MaybeSequence[Union[float, int, str]]

Input tuple.

**`index`** (input_control)  integer `→` int

Index of the first element to select.

**`selected`** (output_control)  tuple(-array) `→` Sequence[Union[float, int, str]]

Selected tuple elements.

## Alternatives

`tuple_first_n`,
`tuple_select`,
`tuple_str_bit_select`,
`tuple_concat`,
`tuple_select_mask`

## See also

`tuple_remove`

## Module

Foundation
