# TupleFindFirst (Operator)

## Name

`TupleFindFirst` — Return the index of the first occurrence of a tuple within another tuple.

## Signature

`static void HOperatorSet.TupleFindFirst(HTuple tuple, HTuple toFind, out HTuple index)`

`HTuple HTuple.TupleFindFirst(HTuple toFind)`

## Description

`TupleFindFirst` searches forward through *`tuple`*
for the first occurrence of the values of the second tuple
*`toFind`* and returns the *`index`* (in relation to the
first input tuple *`tuple`*). For example, if *`tuple`*
contains the values [3,4,5,6,1,2,3,4,0] and *`toFind`* contains
the values [3,4], the output *`index`* is 0. If the first tuple
does not contain the second tuple as a subtuple,
`TupleFindFirst` returns -1 in *`index`*. It is allowed
to mix strings and numbers in the input tuples.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleFindFirst`,
which can be used in an expression in the following syntax:

[`Index := find_first(Tuple, ToFind)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple to examine.

**`toFind`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple with values to find.

**`index`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Index of the first occurrence of the values to find.

## Alternatives

`TupleFind`,
`TupleFindLast`,
`TupleSort`,
`TupleEqualElem`

## Module

Foundation
