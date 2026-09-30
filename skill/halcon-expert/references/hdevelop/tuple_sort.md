# tuple_sort (Operator)

## Name

`tuple_sort` — Sort the elements of a tuple in ascending order.

## Signature

`tuple_sort( : : Tuple : Sorted)`

## Description

`tuple_sort` sorts all elements of *`Tuple`* in ascending order
and returns the result with *`Sorted`*. As a precondition the
single elements of *`Tuple`* must be comparable. Thus, *`Tuple`*
must either exclusively consist of strings or it must only contain
(integer or floating point) numbers. In the latter case integers and
floating point numbers may be mixed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_sort`,
which can be used in an expression in the following syntax:

[`Sorted := sort(Tuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_misc_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Tuple`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple.

**`Sorted`** (output_control)  tuple(-array) `→`  (integer / real / string)

Sorted tuple.

## Alternatives

`tuple_sort_index`,
`tuple_inverse`

## Module

Foundation
