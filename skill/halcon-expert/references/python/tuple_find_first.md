# tuple_find_first (Operator)

## Name

`tuple_find_first` — Return the index of the first occurrence of a tuple within another tuple.

## Signature

`def tuple_find_first(tuple: MaybeSequence[Union[int, float, str]], to_find: MaybeSequence[Union[int, float, str]]) -> int`

## Description

`tuple_find_first` searches forward through *`tuple`*
for the first occurrence of the values of the second tuple
*`to_find`* and returns the *`index`* (in relation to the
first input tuple *`tuple`*). For example, if *`tuple`*
contains the values [3,4,5,6,1,2,3,4,0] and *`to_find`* contains
the values [3,4], the output *`index`* is 0. If the first tuple
does not contain the second tuple as a subtuple,
`tuple_find_first` returns -1 in *`index`*. It is allowed
to mix strings and numbers in the input tuples.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_find_first`,
which can be used in an expression in the following syntax:

[`Index := find_first(Tuple, ToFind)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` MaybeSequence[Union[int, float, str]]

Input tuple to examine.

**`to_find`** (input_control)  tuple(-array) `→` MaybeSequence[Union[int, float, str]]

Input tuple with values to find.

**`index`** (output_control)  integer `→` int

Index of the first occurrence of the values to find.

## Alternatives

`tuple_find`,
`tuple_find_last`,
`tuple_sort`,
`tuple_equal_elem`

## Module

Foundation
