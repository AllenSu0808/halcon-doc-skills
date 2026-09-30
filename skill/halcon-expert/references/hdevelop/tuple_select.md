# tuple_select (Operator)

## Name

`tuple_select` — Select single elements of a tuple.

## Signature

`tuple_select( : : Tuple, Index : Selected)`

## Description

`tuple_select` selects one or more single elements of the tuple
*`Tuple`* and returns them with *`Selected`*. At this,
*`Index`* determines the indices of the elements to select. Thus,
*`Index`* may only contain integer values (any floating point
number within *`Index`* must represent an integer value without
fraction). Indices of tuple elements start at 0, that means, the first
tuple element has got the index 0.

### Exception: Empty input tuples

If *`Tuple`* is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_select`,
which can be used in an expression in the following syntax:

[`Selected := Tuple[Index]`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

[`Selected := subset(Tuple, Index)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Tuple`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple.

**`Index`** (input_control)  integer(-array) `→`  (integer)

Indices of the elements to select.

**`Selected`** (output_control)  tuple(-array) `→`  (integer / real / string)

Selected tuple element.

## Alternatives

`tuple_first_n`,
`tuple_last_n`,
`tuple_str_bit_select`,
`tuple_concat`,
`tuple_select_range`,
`tuple_select_rank`

## See also

`tuple_remove`

## Module

Foundation
