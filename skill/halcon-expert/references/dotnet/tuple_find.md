# TupleFind (Operator)

## Name

`TupleFind` — Return the indices of all occurrences of a tuple within another tuple.

## Signature

`static void HOperatorSet.TupleFind(HTuple tuple, HTuple toFind, out HTuple indices)`

`HTuple HTuple.TupleFind(HTuple toFind)`

## Description

`TupleFind` searches *`tuple`* sequentially for all
occurrences of the values of the second tuple *`toFind`* and
returns the indices in *`indices`* (in relation to the first
input tuple *`tuple`*). For example, if *`tuple`*
contains the values [3,4,5,6,1,2,3,4,0] and *`toFind`* contains
the values [3,4], the output tuple *`indices`* will contain the
values [0,6]. If the first tuple does not contain the second tuple
as a subtuple, `TupleFind` returns -1 in *`indices`*. It
is allowed to mix strings and numbers in the input tuples.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleFind`,
which can be used in an expression in the following syntax:

[`Indices := find(Tuple, ToFind)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple to examine.

**`toFind`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple with values to find.

**`indices`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Indices of the occurrences of the values to find in the
tuple to examine.

## Alternatives

`TupleFindFirst`,
`TupleFindLast`,
`TupleSort`,
`TupleInverse`,
`TupleEqualElem`

## Module

Foundation
