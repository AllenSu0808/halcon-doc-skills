# TupleInsert (Operator)

## Name

`TupleInsert` — Inserts one or more elements into a tuple at index.

## Signature

`static void HOperatorSet.TupleInsert(HTuple tuple, HTuple index, HTuple insertTuple, out HTuple extended)`

`HTuple HTuple.TupleInsert(HTuple index, HTuple insertTuple)`

## Description

`TupleInsert` inserts the elements of the tuple *`insertTuple`*
at index into the tuple *`tuple`* and returns them in the tuple
*`extended`*.
In this context *`index`* determines the start index of the elements
and *`insertTuple`* the values to insert. Successive values of
*`tuple`* will be positioned after the inserted values of
*`insertTuple`*.
The parameter *`index`* must contain a single integer value
(any floating point number must represent an integer value without
fraction). Indices of tuple elements start at 0. Therefore, the first
tuple element has got the index 0. If *`index`* contains the
length of *`tuple`* as index, *`insertTuple`* will be
appended.
The length of the result tuple *`extended`* is always the sum of
the two input tuples *`tuple`* and *`insertTuple`*.
For example, if *`tuple`* contains the values [0,1,0,1,0,1],
the *`index`* contains the value [3] and the
*`insertTuple`* contains the values [2,2,2], then the output
tuple *`extended`* will contain the values [0,1,0,2,2,2,1,0,1].
It is allowed to mix strings and numbers in the input tuples
*`tuple`* and *`insertTuple`*.

### Exception: Empty input tuples

If any of the input tuples is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleInsert`,
which can be used in an expression in the following syntax:

[`Extended := insert(Tuple, Index, InsertTuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple.

**`index`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Start index of elements to be inserted.

**`insertTuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Element(s) to insert at index.

**`extended`** (output_control)  tuple-array `→` [HTuple](HTuple.md) (*int* / long / double / string)

Tuple with inserted elements.

## Alternatives

`TupleConcat`,
`TupleReplace`,
`TupleGenConst`

## See also

`TupleRemove`

## Module

Foundation
