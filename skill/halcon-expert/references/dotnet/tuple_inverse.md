# TupleInverse (Operator)

## Name

`TupleInverse` — Invert a tuple.

## Signature

`static void HOperatorSet.TupleInverse(HTuple tuple, out HTuple inverted)`

`HTuple HTuple.TupleInverse()`

## Description

`TupleInverse` inverts the input tuple *`tuple`*. Thus,
*`inverted`* contains the same elements as *`tuple`* but with
the reverse order.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleInverse`,
which can be used in an expression in the following syntax:

[`Inverted := inverse(Tuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_misc_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple.

**`inverted`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Inverted input tuple.

## Alternatives

`TupleSort`,
`TupleSortIndex`

## Module

Foundation
