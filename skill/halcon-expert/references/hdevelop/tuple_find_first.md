# tuple_find_first (Operator)

## Name

`tuple_find_first` — Return the index of the first occurrence of a tuple within another tuple.

## Signature

`tuple_find_first( : : Tuple, ToFind : Index)`

## Description

`tuple_find_first` searches forward through *`Tuple`*
for the first occurrence of the values of the second tuple
*`ToFind`* and returns the *`Index`* (in relation to the
first input tuple *`Tuple`*). For example, if *`Tuple`*
contains the values [3,4,5,6,1,2,3,4,0] and *`ToFind`* contains
the values [3,4], the output *`Index`* is 0. If the first tuple
does not contain the second tuple as a subtuple,
`tuple_find_first` returns -1 in *`Index`*. It is allowed
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

**`Tuple`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple to examine.

**`ToFind`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple with values to find.

**`Index`** (output_control)  integer `→`  (integer)

Index of the first occurrence of the values to find.

## Alternatives

`tuple_find`,
`tuple_find_last`,
`tuple_sort`,
`tuple_equal_elem`

## Module

Foundation
