# TupleNeg (Operator)

## Name

`TupleNeg` — Negate a tuple.

## Signature

`static void HOperatorSet.TupleNeg(HTuple t, out HTuple neg)`

`HTuple HTuple.TupleNeg()`

## Description

`TupleNeg` computes the negation of the input tuple
*`t`*, i.e., *`neg`* = -*`t`*. The negation of an
integer number is again an integer number. The negation of a
floating point number is a floating point number. The negation of a
string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleNeg`,
which can be used in an expression in the following syntax:

[`Neg := -T`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_arithmetic_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`neg`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Negation of the input tuple.

## Module

Foundation
