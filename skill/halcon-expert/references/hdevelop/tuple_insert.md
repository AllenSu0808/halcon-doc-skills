# tuple_insert (Operator)

## Name

`tuple_insert` — Inserts one or more elements into a tuple at index.

## Signature

`tuple_insert( : : Tuple, Index, InsertTuple : Extended)`

## Description

`tuple_insert` inserts the elements of the tuple *`InsertTuple`*
at index into the tuple *`Tuple`* and returns them in the tuple
*`Extended`*.
In this context *`Index`* determines the start index of the elements
and *`InsertTuple`* the values to insert. Successive values of
*`Tuple`* will be positioned after the inserted values of
*`InsertTuple`*.
The parameter *`Index`* must contain a single integer value
(any floating point number must represent an integer value without
fraction). Indices of tuple elements start at 0. Therefore, the first
tuple element has got the index 0. If *`Index`* contains the
length of *`Tuple`* as index, *`InsertTuple`* will be
appended.
The length of the result tuple *`Extended`* is always the sum of
the two input tuples *`Tuple`* and *`InsertTuple`*.
For example, if *`Tuple`* contains the values [0,1,0,1,0,1],
the *`Index`* contains the value [3] and the
*`InsertTuple`* contains the values [2,2,2], then the output
tuple *`Extended`* will contain the values [0,1,0,2,2,2,1,0,1].
It is allowed to mix strings and numbers in the input tuples
*`Tuple`* and *`InsertTuple`*.

### Exception: Empty input tuples

If any of the input tuples is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_insert`,
which can be used in an expression in the following syntax:

[`Extended := insert(Tuple, Index, InsertTuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Tuple`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple.

**`Index`** (input_control)  integer `→`  (integer)

Start index of elements to be inserted.

**`InsertTuple`** (input_control)  tuple(-array) `→`  (integer / real / string)

Element(s) to insert at index.

**`Extended`** (output_control)  tuple-array `→`  (integer / real / string)

Tuple with inserted elements.

## Alternatives

`tuple_concat`,
`tuple_replace`,
`tuple_gen_const`

## See also

`tuple_remove`

## Module

Foundation
