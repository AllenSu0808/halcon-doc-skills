# TupleInt (Operator)

## Name

`TupleInt` — Convert a tuple into a tuple of integer numbers.

## Signature

`static void HOperatorSet.TupleInt(HTuple t, out HTuple intVal)`

`HTuple HTuple.TupleInt()`

## Description

`TupleInt` converts the input tuple *`t`* into a tuple
of integer numbers by truncating *`t`*. The conversion of a
string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleInt`,
which can be used in an expression in the following syntax:

[`Int := int(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`intVal`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long)

Result of the conversion into integer numbers.

## Alternatives

`TupleRound`

## Module

Foundation
