# tuple_sort_index (Operator)

## Name

`tuple_sort_index` — Sort the elements of a tuple and return the indices of the sorted tuple.

## Signature

`tuple_sort_index( : : Tuple : Indices)`

## Description

`tuple_sort_index` sorts all elements of *`Tuple`* in
ascending order and returns the indices of the elements of the
sorted tuple (in relation to the input tuple *`Tuple`*) with
*`Indices`*. As a precondition the single elements of
*`Tuple`* must be comparable. Thus, *`Tuple`* must
either exclusively consist of strings or it must only contain
(integer or floating point) numbers. In the latter case integers
and floating point numbers may be mixed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_sort_index`,
which can be used in an expression in the following syntax:

[`Indices := sort_index(Tuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_misc_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Tuple`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple.

**`Indices`** (output_control)  integer(-array) `→`  (integer)

Sorted tuple.

## Alternatives

`tuple_sort`,
`tuple_inverse`

## Module

Foundation
