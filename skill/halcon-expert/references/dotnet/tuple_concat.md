# TupleConcat (Operator)

## Name

`TupleConcat` — Concatenate two tuples to a new one.

## Signature

`static void HOperatorSet.TupleConcat(HTuple t1, HTuple t2, out HTuple concat)`

`HTuple HTuple.TupleConcat(HTuple t2)`

## Description

`TupleConcat` concatenates the input tuples *`t1`* and
*`t2`* to a new tuple *`concat`*. The first elements of
*`concat`* conform to the elements of *`t1`* and the
remaining elements of *`concat`* conform to those of *`t2`*.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleConcat`,
which can be used in an expression in the following syntax:

[`Concat := [T1, T2]`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t1`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple 1.

**`t2`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple 2.

**`concat`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Concatenation of input tuples.

## Alternatives

`TupleGenConst`,
`TupleStrBitSelect`,
`TupleSelect`,
`TupleStrFirstN`,
`TupleStrLastN`,
`TupleSubstr`

## See also

`TupleRemove`

## Module

Foundation
