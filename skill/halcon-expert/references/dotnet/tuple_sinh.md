# TupleSinh (Operator)

## Name

`TupleSinh` — Compute the hyperbolic sine of a tuple.

## Signature

`static void HOperatorSet.TupleSinh(HTuple t, out HTuple sinh)`

`HTuple HTuple.TupleSinh()`

## Description

`TupleSinh` computes the hyperbolic sine of the input tuple
*`t`*. The hyperbolic sine is always returned as a floating
point number in *`sinh`*. The hyperbolic sine of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleSinh`,
which can be used in an expression in the following syntax:

[`Sinh := sinh(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`sinh`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Hyperbolic sine of the input tuple.

## Alternatives

`TupleCosh`,
`TupleTanh`

## See also

`TupleAsinh`,
`TupleSin`,
`TupleAsin`

## Module

Foundation
