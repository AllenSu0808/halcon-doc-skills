# TupleRemove (Operator)

## Name

`TupleRemove` — Remove elements from a tuple.

## Signature

`static void HOperatorSet.TupleRemove(HTuple tuple, HTuple index, out HTuple reduced)`

`HTuple HTuple.TupleRemove(HTuple index)`

## Description

`TupleRemove` removes one or more elements from the tuple
*`tuple`* and returns the rest in the tuple *`reduced`*.
*`index`* determines the indices of the elements to remove. Thus,
*`index`* may only contain integer values (any floating point
number within *`index`* must represent an integer value without
fraction). Note that indices of tuple elements start at 0, i.e. the first
tuple element has got the index 0. Duplicates and indices out of
range are ignored.

### Exception: Empty input tuple

If *`tuple`* is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleRemove`,
which can be used in an expression in the following syntax:

[`Reduced := remove(Tuple, Index)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple.

**`index`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Indices of the elements to remove.

**`reduced`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Reduced tuple.

## Alternatives

`TupleFirstN`,
`TupleLastN`,
`TupleStrBitSelect`,
`TupleConcat`,
`TupleInsert`,
`TupleReplace`

## See also

`TupleSelect`,
`TupleSelectMask`

## Module

Foundation
