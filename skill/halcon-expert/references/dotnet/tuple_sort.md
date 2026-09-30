# TupleSort (Operator)

## Name

`TupleSort` — Sort the elements of a tuple in ascending order.

## Signature

`static void HOperatorSet.TupleSort(HTuple tuple, out HTuple sorted)`

`HTuple HTuple.TupleSort()`

## Description

`TupleSort` sorts all elements of *`tuple`* in ascending order
and returns the result with *`sorted`*. As a precondition the
single elements of *`tuple`* must be comparable. Thus, *`tuple`*
must either exclusively consist of strings or it must only contain
(integer or floating point) numbers. In the latter case integers and
floating point numbers may be mixed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleSort`,
which can be used in an expression in the following syntax:

[`Sorted := sort(Tuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_misc_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple.

**`sorted`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Sorted tuple.

## Alternatives

`TupleSortIndex`,
`TupleInverse`

## Module

Foundation
