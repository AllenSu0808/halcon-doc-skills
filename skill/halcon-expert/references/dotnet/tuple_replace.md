# TupleReplace (Operator)

## Name

`TupleReplace` — Replaces one or more elements of a tuple.

## Signature

`static void HOperatorSet.TupleReplace(HTuple tuple, HTuple index, HTuple replaceTuple, out HTuple replaced)`

`HTuple HTuple.TupleReplace(HTuple index, HTuple replaceTuple)`

## Description

`TupleReplace` replaces one or more elements of the
input tuple *`tuple`* and returns them with *`replaced`*.
At this, *`index`* determines the indices of the elements
and *`replaceTuple`* the corresponding values to replace.
The parameter *`index`* must contain one or more integer values
(any floating point number must represent an integer value without
fraction). Indices of tuple elements start at 0. Therefore, the first
tuple element has got the index 0. If *`replaceTuple`* contains only
one value, this value will be replaced at all indices of *`index`*.
If a value of *`index`* is greater than the length of the input
tuple *`tuple`*, *`replaced`* will be extended accordingly and
initialized with zeros. For example, if *`tuple`* contains [1],
*`index`* contains the values [2,4], and *`replaceTuple`*
contains the values [3,5], *`replaced`* will be [1,0,3,0,5].

It is allowed to mix strings and numbers in the input tuples
*`tuple`* and *`replaceTuple`*.

### Exception: Empty input tuples

If either *`index`* or *`replaceTuple`* is empty and the other is
not, an exception is raised. If both are empty, the output tuple
*`replaced`* corresponds to the input *`tuple`*. If both are
empty, but the input *`tuple`* is not, the empty tuple will be
extended as described above.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleReplace`,
which can be used in an expression in the following syntax:

[`Replaced := replace(Tuple, Index, ReplaceTuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple.

**`index`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Index/Indices of elements to be replaced.

**`replaceTuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Element(s) to replace.

**`replaced`** (output_control)  tuple-array `→` [HTuple](HTuple.md) (*int* / long / double / string)

Tuple with replaced elements.

## Alternatives

`TupleSelect`,
`TupleFirstN`,
`TupleLastN`,
`TupleSelectMask`,
`TupleStrBitSelect`,
`TupleConcat`,
`TupleSelectRank`

## See also

`TupleRemove`,
`TupleInsert`

## Module

Foundation
