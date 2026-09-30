# tuple_find (Operator)

## Name

`tuple_find` — Return the indices of all occurrences of a tuple within another tuple.

## Signature

`def tuple_find(tuple: MaybeSequence[Union[float, int, str]], to_find: MaybeSequence[Union[float, int, str]]) -> Sequence[int]`

`def tuple_find_s(tuple: MaybeSequence[Union[float, int, str]], to_find: MaybeSequence[Union[float, int, str]]) -> int`

## Description

`tuple_find` searches *`tuple`* sequentially for all
occurrences of the values of the second tuple *`to_find`* and
returns the indices in *`indices`* (in relation to the first
input tuple *`tuple`*). For example, if *`tuple`*
contains the values [3,4,5,6,1,2,3,4,0] and *`to_find`* contains
the values [3,4], the output tuple *`indices`* will contain the
values [0,6]. If the first tuple does not contain the second tuple
as a subtuple, `tuple_find` returns -1 in *`indices`*. It
is allowed to mix strings and numbers in the input tuples.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_find`,
which can be used in an expression in the following syntax:

[`Indices := find(Tuple, ToFind)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` MaybeSequence[Union[float, int, str]]

Input tuple to examine.

**`to_find`** (input_control)  tuple(-array) `→` MaybeSequence[Union[float, int, str]]

Input tuple with values to find.

**`indices`** (output_control)  integer(-array) `→` Sequence[int]

Indices of the occurrences of the values to find in the
tuple to examine.

## Alternatives

`tuple_find_first`,
`tuple_find_last`,
`tuple_sort`,
`tuple_inverse`,
`tuple_equal_elem`

## Module

Foundation
