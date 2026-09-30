# TupleFirstN (Operator)

## Name

`TupleFirstN` — Select the first elements of a tuple up to the index “n”.

## Signature

`static void HOperatorSet.TupleFirstN(HTuple tuple, HTuple index, out HTuple selected)`

`HTuple HTuple.TupleFirstN(HTuple index)`

## Description

`TupleFirstN` selects the first elements of *`tuple`*
up to the index *`index`* and returns them in *`selected`*.
Indices of tuple elements start at 0,
that means, the first tuple element has got the index 0. In total,
*`index`*+1 elements are returned.

*`index`* must contain a single integer value (or a floating point
number that represents an integer value without fraction).

### Exception: Empty input tuple

If *`tuple`* is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleFirstN`,
which can be used in an expression in the following syntax:

[`Selected := firstn(Tuple, Index)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple.

**`index`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Index of the last element to select.

**`selected`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Selected tuple elements.

## Alternatives

`TupleLastN`,
`TupleSelect`,
`TupleStrBitSelect`,
`TupleConcat`,
`TupleSelectMask`

## See also

`TupleRemove`

## Module

Foundation
