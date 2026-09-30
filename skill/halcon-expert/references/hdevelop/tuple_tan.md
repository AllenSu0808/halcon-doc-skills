# tuple_tan (Operator)

## Name

`tuple_tan` — Compute the tangent of a tuple.

## Signature

`tuple_tan( : : T : Tan)`

## Description

`tuple_tan` computes the tangent of the input tuple *`T`*.
The tangent is always returned as a floating point number in *`Tan`*.
The angles in *`T`* are represented in radians. The
tangent of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_tan`,
which can be used in an expression in the following syntax:

[`Tan := tan(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  angle.rad(-array) `→`  (real / integer)

Input tuple.

**`Tan`** (output_control)  number(-array) `→`  (real)

Tangent of the input tuple.

## Alternatives

`tuple_sin`,
`tuple_cos`

## See also

`tuple_atan`,
`tuple_atan2`,
`tuple_tanh`,
`tuple_atanh`

## Module

Foundation
