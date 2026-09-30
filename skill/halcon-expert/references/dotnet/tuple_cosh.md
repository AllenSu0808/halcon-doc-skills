# TupleCosh (Operator)

## Name

`TupleCosh` — Compute the hyperbolic cosine of a tuple.

## Signature

`static void HOperatorSet.TupleCosh(HTuple t, out HTuple cosh)`

`HTuple HTuple.TupleCosh()`

## Description

`TupleCosh` computes the hyperbolic cosine of the input tuple
*`t`*. The hyperbolic cosine is always returned as a floating
point number in *`cosh`*. The hyperbolic cosine of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleCosh`,
which can be used in an expression in the following syntax:

[`Cosh := cosh(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`cosh`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Hyperbolic cosine of the input tuple.

## Alternatives

`TupleSinh`,
`TupleTanh`

## See also

`TupleAcosh`,
`TupleCos`,
`TupleAcos`

## Module

Foundation
