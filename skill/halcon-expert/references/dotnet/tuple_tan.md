# TupleTan (Operator)

## Name

`TupleTan` — Compute the tangent of a tuple.

## Signature

`static void HOperatorSet.TupleTan(HTuple t, out HTuple tan)`

`HTuple HTuple.TupleTan()`

## Description

`TupleTan` computes the tangent of the input tuple *`t`*.
The tangent is always returned as a floating point number in *`tan`*.
The angles in *`t`* are represented in radians. The
tangent of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleTan`,
which can be used in an expression in the following syntax:

[`Tan := tan(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`tan`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Tangent of the input tuple.

## Alternatives

`TupleSin`,
`TupleCos`

## See also

`TupleAtan`,
`TupleAtan2`,
`TupleTanh`,
`TupleAtanh`

## Module

Foundation
