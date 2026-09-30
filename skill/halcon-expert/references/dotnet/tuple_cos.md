# TupleCos (Operator)

## Name

`TupleCos` — Compute the cosine of a tuple.

## Signature

`static void HOperatorSet.TupleCos(HTuple t, out HTuple cos)`

`HTuple HTuple.TupleCos()`

## Description

`TupleCos` computes the cosine of the input tuple *`t`*.
The cosine is always returned as a floating point number in *`cos`*.
The angles in *`t`* are represented in radians. The
cosine of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleCos`,
which can be used in an expression in the following syntax:

[`Cos := cos(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`cos`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Cosine of the input tuple.

## Alternatives

`TupleSin`,
`TupleTan`

## See also

`TupleAcos`,
`TupleCosh`,
`TupleAcosh`

## Module

Foundation
