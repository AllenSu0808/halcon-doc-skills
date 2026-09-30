# tuple_remove (Operator)

## Name

`tuple_remove` — Remove elements from a tuple.

## Signature

`tuple_remove( : : Tuple, Index : Reduced)`

## Description

`tuple_remove` removes one or more elements from the tuple
*`Tuple`* and returns the rest in the tuple *`Reduced`*.
*`Index`* determines the indices of the elements to remove. Thus,
*`Index`* may only contain integer values (any floating point
number within *`Index`* must represent an integer value without
fraction). Note that indices of tuple elements start at 0, i.e. the first
tuple element has got the index 0. Duplicates and indices out of
range are ignored.

### Exception: Empty input tuple

If *`Tuple`* is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_remove`,
which can be used in an expression in the following syntax:

[`Reduced := remove(Tuple, Index)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Tuple`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple.

**`Index`** (input_control)  integer(-array) `→`  (integer)

Indices of the elements to remove.

**`Reduced`** (output_control)  tuple(-array) `→`  (integer / real / string)

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
