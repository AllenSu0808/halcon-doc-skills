# TupleSelectMask (Operator)

## Name

`TupleSelectMask` — Select in mask specified elements of a tuple.

## Signature

`static void HOperatorSet.TupleSelectMask(HTuple tuple, HTuple mask, out HTuple selected)`

`HTuple HTuple.TupleSelectMask(HTuple mask)`

## Description

`TupleSelectMask` selects one or more single elements of the tuple
*`tuple`* and returns them with *`selected`*. For every element
*`mask`* determines the corresponding element to select.
If the value is greater than 0, the appropriate element is selected.
Thus the length of the two input tuples has to be equal and
*`mask`* may only contain integer or float values.

### Exception: Empty input tuples

If both input tuples are empty, the operator returns an
empty tuple. If only one of the input tuples is empty and the other is not,
an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleSelectMask`,
which can be used in an expression in the following syntax:

[`Selected := select_mask(Tuple, Mask)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple.

**`mask`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

> 0 specifies the elements to select.

**`selected`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Selected tuple elements.

## Alternatives

`TupleFirstN`,
`TupleLastN`,
`TupleStrBitSelect`,
`TupleConcat`,
`TupleSelect`,
`TupleSelectRange`,
`TupleSelectRank`

## See also

`TupleRemove`

## Module

Foundation
