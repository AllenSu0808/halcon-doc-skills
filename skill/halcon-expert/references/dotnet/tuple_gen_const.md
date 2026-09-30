# TupleGenConst (Operator)

## Name

`TupleGenConst` — Generate a tuple of a specific length and initialize its elements.

## Signature

`static void HOperatorSet.TupleGenConst(HTuple length, HTuple constVal, out HTuple newtuple)`

`static HTuple HTuple.TupleGenConst(HTuple length, HTuple constVal)`

## Description

`TupleGenConst` generates a new tuple in *`newtuple`*.
The input parameter *`length`* determines the number of elements
for the new tuple. Thus, *`length`* may only consist of a single number.
If *`length`* contains a floating point number, this may only
represent an integer value (without fraction).
The data type and value of each element of the new generated tuple is
determined by the input parameter *`constVal`* that may only
consist of a single element. All elements in *`newtuple`*
have got the same data type and value as the single element in
*`constVal`*.

### Exception: Empty input tuples

If any of the input tuples is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleGenConst`,
which can be used in an expression in the following syntax:

[`Newtuple := gen_tuple_const(Length, Const)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`length`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long / double)

Length of tuple to generate.

**`constVal`** (input_control)  tuple `→` [HTuple](HTuple.md) (*int* / long / double / string / HHandle)

Constant for initializing the tuple elements.

**`newtuple`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

New Tuple.

## Alternatives

`TupleStrBitSelect`,
`TupleSelect`,
`TupleStrFirstN`,
`TupleStrLastN`,
`TupleConcat`,
`TupleInsert`,
`TupleReplace`,
`TupleGenSequence`

## See also

`TupleRand`

## Module

Foundation
