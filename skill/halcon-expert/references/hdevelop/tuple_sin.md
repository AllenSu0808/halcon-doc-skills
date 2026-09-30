# tuple_sin (Operator)

## Name

`tuple_sin` — Compute the sine of a tuple.

## Signature

`tuple_sin( : : T : Sin)`

## Description

`tuple_sin` computes the sine of the input tuple *`T`*.
The sine is always returned as a floating point number in *`Sin`*.
The angles in *`T`* are represented in radians. The sine of
a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_sin`,
which can be used in an expression in the following syntax:

[`Sin := sin(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  angle.rad(-array) `→`  (real / integer)

Input tuple.

**`Sin`** (output_control)  number(-array) `→`  (real)

Sine of the input tuple.

## Alternatives

`tuple_cos`,
`tuple_tan`

## See also

`tuple_asin`,
`tuple_sinh`,
`tuple_asinh`

## Module

Foundation
