# tuple_atan (Operator)

## Name

`tuple_atan` — Compute the arctangent of a tuple.

## Signature

`tuple_atan( : : T : ATan)`

## Description

`tuple_atan` computes the arctangent of the input tuple
*`T`*. The arctangent is always returned as a floating point
number in *`ATan`*. The angles in *`ATan`* are represented in
radians. The arctangent of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_atan`,
which can be used in an expression in the following syntax:

[`ATan := atan(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  number(-array) `→`  (real / integer)

Input tuple.

**`ATan`** (output_control)  angle.rad(-array) `→`  (real)

Arctangent of the input tuple.

## Alternatives

`tuple_atan2`,
`tuple_asin`,
`tuple_acos`

## See also

`tuple_tan`,
`tuple_tanh`,
`tuple_atanh`

## Module

Foundation
