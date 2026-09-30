# tuple_cos (Operator)

## Name

`tuple_cos` — Compute the cosine of a tuple.

## Signature

`tuple_cos( : : T : Cos)`

## Description

`tuple_cos` computes the cosine of the input tuple *`T`*.
The cosine is always returned as a floating point number in *`Cos`*.
The angles in *`T`* are represented in radians. The
cosine of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_cos`,
which can be used in an expression in the following syntax:

[`Cos := cos(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  angle.rad(-array) `→`  (real / integer)

Input tuple.

**`Cos`** (output_control)  number(-array) `→`  (real)

Cosine of the input tuple.

## Alternatives

`tuple_sin`,
`tuple_tan`

## See also

`tuple_acos`,
`tuple_cosh`,
`tuple_acosh`

## Module

Foundation
