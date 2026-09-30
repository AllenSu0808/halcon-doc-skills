# TupleReal (Operator)

## Name

`TupleReal` — Convert a tuple into a tuple of floating point numbers.

## Signature

`static void HOperatorSet.TupleReal(HTuple t, out HTuple real)`

`HTuple HTuple.TupleReal()`

## Description

`TupleReal` converts the input tuple *`t`* into a tuple
of floating point numbers. The conversion of a string is not
allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleReal`,
which can be used in an expression in the following syntax:

[`Real := real(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`real`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Input tuple as floating point numbers.

## Module

Foundation
