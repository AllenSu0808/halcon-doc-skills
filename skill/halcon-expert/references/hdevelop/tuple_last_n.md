# tuple_last_n (Operator)

## Name

`tuple_last_n` — Select all elements from index “n” to the end of a tuple.

## Signature

`tuple_last_n( : : Tuple, Index : Selected)`

## Description

Starting with the “n-th” element of the tuple *`Tuple`*,
`tuple_last_n` selects every element of *`Tuple`* and returns
it with *`Selected`*. Thus, *`Selected`* contains all
elements of *`Tuple`* from index “n” up to the last element
of *`Tuple`* (including the element at position “n”). The index
“n” is determined by the input parameter *`Index`*. Thus,
*`Index`* must contain a single integer value (if *`Index`*
consists of a floating point number, this must represent
an integer value without fraction). Indices of tuple elements start at 0,
that means, the first tuple element has got the index 0.

### Exception: Empty input tuple

If *`Tuple`* is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_last_n`,
which can be used in an expression in the following syntax:

[`Selected := lastn(Tuple, Index)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Tuple`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple.

**`Index`** (input_control)  integer `→`  (integer)

Index of the first element to select.

**`Selected`** (output_control)  tuple(-array) `→`  (integer / real / string)

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
