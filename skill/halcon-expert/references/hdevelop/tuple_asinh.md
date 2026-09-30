# tuple_asinh (Operator)

## Name

`tuple_asinh` — Compute the inverse hyperbolic sine of a tuple.

## Signature

`tuple_asinh( : : T : Asinh)`

## Description

`tuple_asinh` computes the inverse hyperbolic sine of the
input tuple *`T`*. The inverse hyperbolic sine is always
returned as a floating point number in *`Asinh`*. The inverse
hyperbolic sine of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_asinh`,
which can be used in an expression in the following syntax:

[`Asinh := asinh(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  number(-array) `→`  (real / integer)

Input tuple.

**`Asinh`** (output_control)  number(-array) `→`  (real)

Inverse hyperbolic sine of the input tuple.

## Alternatives

`tuple_acosh`,
`tuple_atanh`

## See also

`tuple_asin`,
`tuple_sin`,
`tuple_asin`

## Module

Foundation
