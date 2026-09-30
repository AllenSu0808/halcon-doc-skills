# tuple_first_n (Operator)

## Name

`tuple_first_n` — Select the first elements of a tuple up to the index “n”.

## Signature

`tuple_first_n( : : Tuple, Index : Selected)`

## Description

`tuple_first_n` selects the first elements of *`Tuple`*
up to the index *`Index`* and returns them in *`Selected`*.
Indices of tuple elements start at 0,
that means, the first tuple element has got the index 0. In total,
*`Index`*+1 elements are returned.

*`Index`* must contain a single integer value (or a floating point
number that represents an integer value without fraction).

### Exception: Empty input tuple

If *`Tuple`* is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_first_n`,
which can be used in an expression in the following syntax:

[`Selected := firstn(Tuple, Index)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Tuple`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple.

**`Index`** (input_control)  integer `→`  (integer)

Index of the last element to select.

**`Selected`** (output_control)  tuple(-array) `→`  (integer / real / string)

Selected tuple elements.

## Alternatives

`tuple_last_n`,
`tuple_select`,
`tuple_str_bit_select`,
`tuple_concat`,
`tuple_select_mask`

## See also

`tuple_remove`

## Module

Foundation
