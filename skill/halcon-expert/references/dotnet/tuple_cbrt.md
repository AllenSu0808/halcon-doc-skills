# TupleCbrt (Operator)

## Name

`TupleCbrt` — Compute the cube root of a tuple.

## Signature

`static void HOperatorSet.TupleCbrt(HTuple t, out HTuple cbrt)`

`HTuple HTuple.TupleCbrt()`

## Description

`TupleCbrt` computes the cube root of the input tuple
*`t`*. The cube root is always returned as a floating point
number. The cube root of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleCbrt`,
which can be used in an expression in the following syntax:

[`Cbrt := cbrt(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`cbrt`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Cube root of the input tuple.

## Alternatives

`TuplePow`

## See also

`TupleSqrt`

## Module

Foundation
