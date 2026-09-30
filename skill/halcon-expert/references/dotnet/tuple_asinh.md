# TupleAsinh (Operator)

## Name

`TupleAsinh` — Compute the inverse hyperbolic sine of a tuple.

## Signature

`static void HOperatorSet.TupleAsinh(HTuple t, out HTuple asinh)`

`HTuple HTuple.TupleAsinh()`

## Description

`TupleAsinh` computes the inverse hyperbolic sine of the
input tuple *`t`*. The inverse hyperbolic sine is always
returned as a floating point number in *`asinh`*. The inverse
hyperbolic sine of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleAsinh`,
which can be used in an expression in the following syntax:

[`Asinh := asinh(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`asinh`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Inverse hyperbolic sine of the input tuple.

## Alternatives

`TupleAcosh`,
`TupleAtanh`

## See also

`TupleAsin`,
`TupleSin`,
`TupleAsin`

## Module

Foundation
