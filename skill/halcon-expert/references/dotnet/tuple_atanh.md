# TupleAtanh (Operator)

## Name

`TupleAtanh` — Compute the inverse hyperbolic tangent of a tuple.

## Signature

`static void HOperatorSet.TupleAtanh(HTuple t, out HTuple atanh)`

`HTuple HTuple.TupleAtanh()`

## Description

`TupleAtanh` computes the inverse hyperbolic tangent of the
input tuple *`t`*. The inverse hyperbolic tangent is always
returned as a floating point number in *`atanh`*. The inverse
hyperbolic tangent of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleAtanh`,
which can be used in an expression in the following syntax:

[`Atanh := atanh(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`atanh`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Inverse hyperbolic tangent of the input tuple.

## Alternatives

`TupleAsinh`,
`TupleAcosh`

## See also

`TupleTanh`,
`TupleTan`,
`TupleAtan`,
`TupleAtan2`

## Module

Foundation
