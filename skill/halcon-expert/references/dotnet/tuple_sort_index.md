# TupleSortIndex (Operator)

## Name

`TupleSortIndex` — Sort the elements of a tuple and return the indices of the sorted tuple.

## Signature

`static void HOperatorSet.TupleSortIndex(HTuple tuple, out HTuple indices)`

`HTuple HTuple.TupleSortIndex()`

## Description

`TupleSortIndex` sorts all elements of *`tuple`* in
ascending order and returns the indices of the elements of the
sorted tuple (in relation to the input tuple *`tuple`*) with
*`indices`*. As a precondition the single elements of
*`tuple`* must be comparable. Thus, *`tuple`* must
either exclusively consist of strings or it must only contain
(integer or floating point) numbers. In the latter case integers
and floating point numbers may be mixed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleSortIndex`,
which can be used in an expression in the following syntax:

[`Indices := sort_index(Tuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_misc_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple.

**`indices`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Sorted tuple.

## Alternatives

`TupleSort`,
`TupleInverse`

## Module

Foundation
