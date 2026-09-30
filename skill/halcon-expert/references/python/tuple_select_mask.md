# tuple_select_mask (Operator)

## Name

`tuple_select_mask` — Select in mask specified elements of a tuple.

## Signature

`def tuple_select_mask(tuple: MaybeSequence[Union[float, int, str]], mask: MaybeSequence[int]) -> Sequence[Union[float, int, str]]`

`def tuple_select_mask_s(tuple: MaybeSequence[Union[float, int, str]], mask: MaybeSequence[int]) -> Union[float, int, str]`

## Description

`tuple_select_mask` selects one or more single elements of the tuple
*`tuple`* and returns them with *`selected`*. For every element
*`mask`* determines the corresponding element to select.
If the value is greater than 0, the appropriate element is selected.
Thus the length of the two input tuples has to be equal and
*`mask`* may only contain integer or float values.

### Exception: Empty input tuples

If both input tuples are empty, the operator returns an
empty tuple. If only one of the input tuples is empty and the other is not,
an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_select_mask`,
which can be used in an expression in the following syntax:

[`Selected := select_mask(Tuple, Mask)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` MaybeSequence[Union[float, int, str]]

Input tuple.

**`mask`** (input_control)  integer(-array) `→` MaybeSequence[int]

> 0 specifies the elements to select.

**`selected`** (output_control)  tuple(-array) `→` Sequence[Union[float, int, str]]

Selected tuple elements.

## Alternatives

`tuple_first_n`,
`tuple_last_n`,
`tuple_str_bit_select`,
`tuple_concat`,
`tuple_select`,
`tuple_select_range`,
`tuple_select_rank`

## See also

`tuple_remove`

## Module

Foundation
