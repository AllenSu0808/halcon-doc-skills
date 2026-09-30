# tuple_atan2 (Operator)

## Name

`tuple_atan2` — Compute the arctangent of a tuple for all four quadrants.

## Signature

`tuple_atan2( : : Y, X : ATan)`

## Description

`tuple_atan2` computes the arctangent of the input tuples
*`Y`*/*`X`* while treating all four quadrants
correctly. The arctangent is always returned as a floating point
number in *`ATan`*. The angles in *`ATan`* are represented in
radians. The arctangent of a string is not allowed.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_atan2`,
which can be used in an expression in the following syntax:

[`ATan := atan2(Y, X)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Y`** (input_control)  number(-array) `→`  (real / integer)

Input tuple of the y-values.

**`X`** (input_control)  number(-array) `→`  (real / integer)

Input tuple of the x-values.

**`ATan`** (output_control)  angle.rad(-array) `→`  (real)

Arctangent of the input tuple.

## Alternatives

`tuple_atan`,
`tuple_asin`,
`tuple_acos`

## See also

`tuple_tan`,
`tuple_tanh`

## Module

Foundation
