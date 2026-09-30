# TupleSelect (Operator)

## Name

`TupleSelect` — Select single elements of a tuple.

## Signature

`static void HOperatorSet.TupleSelect(HTuple tuple, HTuple index, out HTuple selected)`

`HTuple HTuple.TupleSelect(HTuple index)`

## Description

`TupleSelect` selects one or more single elements of the tuple
*`tuple`* and returns them with *`selected`*. At this,
*`index`* determines the indices of the elements to select. Thus,
*`index`* may only contain integer values (any floating point
number within *`index`* must represent an integer value without
fraction). Indices of tuple elements start at 0, that means, the first
tuple element has got the index 0.

### Exception: Empty input tuples

If *`tuple`* is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleSelect`,
which can be used in an expression in the following syntax:

[`Selected := Tuple[Index]`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

[`Selected := subset(Tuple, Index)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple.

**`index`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Indices of the elements to select.

**`selected`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Selected tuple element.

## Alternatives

`TupleFirstN`,
`TupleLastN`,
`TupleStrBitSelect`,
`TupleConcat`,
`TupleSelectRange`,
`TupleSelectRank`

## See also

`TupleRemove`

## Module

Foundation
