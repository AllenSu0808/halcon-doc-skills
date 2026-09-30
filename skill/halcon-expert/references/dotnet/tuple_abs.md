# TupleAbs (Operator)

## Name

`TupleAbs` — Compute the absolute value of a tuple.

## Signature

`static void HOperatorSet.TupleAbs(HTuple t, out HTuple abs)`

`HTuple HTuple.TupleAbs()`

## Description

`TupleAbs` computes the absolute value of the input tuple
*`t`*. The absolute value of an integer number is again an
integer number. The absolute value of a floating point number is a
floating point number. The absolute value of a string is not
allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleAbs`,
which can be used in an expression in the following syntax:

[`Abs := abs(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`abs`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Absolute value of the input tuple.

## Alternatives

`TupleFabs`

## Module

Foundation
