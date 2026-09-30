# TupleTanh (Operator)

## Name

`TupleTanh` — Compute the hyperbolic tangent of a tuple.

## Signature

`static void HOperatorSet.TupleTanh(HTuple t, out HTuple tanh)`

`HTuple HTuple.TupleTanh()`

## Description

`TupleTanh` computes the hyperbolic tangent of the input
tuple *`t`*. The hyperbolic tangent is always returned as a
floating point number in *`tanh`*. The hyperbolic tangent of a string
is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleTanh`,
which can be used in an expression in the following syntax:

[`Tanh := tanh(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`tanh`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Hyperbolic tangent of the input tuple.

## Alternatives

`TupleSinh`,
`TupleCosh`

## See also

`TupleAtanh`,
`TupleTan`,
`TupleAtan`,
`TupleAtan2`

## Module

Foundation
