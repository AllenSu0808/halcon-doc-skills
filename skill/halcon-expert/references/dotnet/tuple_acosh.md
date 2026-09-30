# TupleAcosh (Operator)

## Name

`TupleAcosh` — Compute the inverse hyperbolic cosine of a tuple.

## Signature

`static void HOperatorSet.TupleAcosh(HTuple t, out HTuple acosh)`

`HTuple HTuple.TupleAcosh()`

## Description

`TupleAcosh` computes the inverse hyperbolic cosine of the
input tuple *`t`*. The inverse hyperbolic cosine is always
returned as a floating point number in *`acosh`*. The inverse
hyperbolic cosine of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleAcosh`,
which can be used in an expression in the following syntax:

[`Acosh := acosh(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`acosh`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Inverse hyperbolic cosine of the input tuple.

## Alternatives

`TupleAsinh`,
`TupleAtanh`

## See also

`TupleCosh`,
`TupleCos`,
`TupleAcos`

## Module

Foundation
