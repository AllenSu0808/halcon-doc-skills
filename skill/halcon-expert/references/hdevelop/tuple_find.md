# tuple_find (Operator)

## Name

`tuple_find` — Return the indices of all occurrences of a tuple within another tuple.

## Signature

`tuple_find( : : Tuple, ToFind : Indices)`

## Description

`tuple_find` searches *`Tuple`* sequentially for all
occurrences of the values of the second tuple *`ToFind`* and
returns the indices in *`Indices`* (in relation to the first
input tuple *`Tuple`*). For example, if *`Tuple`*
contains the values [3,4,5,6,1,2,3,4,0] and *`ToFind`* contains
the values [3,4], the output tuple *`Indices`* will contain the
values [0,6]. If the first tuple does not contain the second tuple
as a subtuple, `tuple_find` returns -1 in *`Indices`*. It
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

**`Tuple`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple to examine.

**`ToFind`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple with values to find.

**`Indices`** (output_control)  integer(-array) `→`  (integer)

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
