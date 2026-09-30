# TupleSin (Operator)

## Name

`TupleSin` — Compute the sine of a tuple.

## Signature

`static void HOperatorSet.TupleSin(HTuple t, out HTuple sin)`

`HTuple HTuple.TupleSin()`

## Description

`TupleSin` computes the sine of the input tuple *`t`*.
The sine is always returned as a floating point number in *`sin`*.
The angles in *`t`* are represented in radians. The sine of
a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleSin`,
which can be used in an expression in the following syntax:

[`Sin := sin(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`sin`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Sine of the input tuple.

## Alternatives

`TupleCos`,
`TupleTan`

## See also

`TupleAsin`,
`TupleSinh`,
`TupleAsinh`

## Module

Foundation
