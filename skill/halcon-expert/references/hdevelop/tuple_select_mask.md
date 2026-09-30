# tuple_select_mask (Operator)

## Name

`tuple_select_mask` — Select in mask specified elements of a tuple.

## Signature

`tuple_select_mask( : : Tuple, Mask : Selected)`

## Description

`tuple_select_mask` selects one or more single elements of the tuple
*`Tuple`* and returns them with *`Selected`*. For every element
*`Mask`* determines the corresponding element to select.
If the value is greater than 0, the appropriate element is selected.
Thus the length of the two input tuples has to be equal and
*`Mask`* may only contain integer or float values.

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

**`Tuple`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple.

**`Mask`** (input_control)  integer(-array) `→`  (integer)

> 0 specifies the elements to select.

**`Selected`** (output_control)  tuple(-array) `→`  (integer / real / string)

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
