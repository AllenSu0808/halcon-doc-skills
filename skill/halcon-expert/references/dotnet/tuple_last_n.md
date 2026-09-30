# TupleLastN (Operator)

## Name

`TupleLastN` — Select all elements from index “n” to the end of a tuple.

## Signature

`static void HOperatorSet.TupleLastN(HTuple tuple, HTuple index, out HTuple selected)`

`HTuple HTuple.TupleLastN(HTuple index)`

## Description

Starting with the “n-th” element of the tuple *`tuple`*,
`TupleLastN` selects every element of *`tuple`* and returns
it with *`selected`*. Thus, *`selected`* contains all
elements of *`tuple`* from index “n” up to the last element
of *`tuple`* (including the element at position “n”). The index
“n” is determined by the input parameter *`index`*. Thus,
*`index`* must contain a single integer value (if *`index`*
consists of a floating point number, this must represent
an integer value without fraction). Indices of tuple elements start at 0,
that means, the first tuple element has got the index 0.

### Exception: Empty input tuple

If *`tuple`* is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleLastN`,
which can be used in an expression in the following syntax:

[`Selected := lastn(Tuple, Index)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple.

**`index`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Index of the first element to select.

**`selected`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Selected tuple elements.

## Alternatives

`TupleFirstN`,
`TupleSelect`,
`TupleStrBitSelect`,
`TupleConcat`,
`TupleSelectMask`

## See also

`TupleRemove`

## Module

Foundation
