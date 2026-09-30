# tuple_sort (Operator)

## Name

`tuple_sort` — Sort the elements of a tuple in ascending order.

## Signature

`def tuple_sort(tuple: MaybeSequence[Union[float, int, str]]) -> Sequence[Union[float, int, str]]`

`def tuple_sort_s(tuple: MaybeSequence[Union[float, int, str]]) -> Union[float, int, str]`

## Description

`tuple_sort` sorts all elements of *`tuple`* in ascending order
and returns the result with *`sorted`*. As a precondition the
single elements of *`tuple`* must be comparable. Thus, *`tuple`*
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

**`tuple`** (input_control)  tuple(-array) `→` MaybeSequence[Union[float, int, str]]

Input tuple.

**`sorted`** (output_control)  tuple(-array) `→` Sequence[Union[float, int, str]]

Sorted tuple.

## Alternatives

`tuple_sort_index`,
`tuple_inverse`

## Module

Foundation
