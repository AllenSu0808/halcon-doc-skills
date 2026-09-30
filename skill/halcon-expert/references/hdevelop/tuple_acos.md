# tuple_acos (Operator)

## Name

`tuple_acos` — Compute the arccosine of a tuple.

## Signature

`tuple_acos( : : T : ACos)`

## Description

`tuple_acos` computes the arccosine of the input tuple
*`T`*. The arccosine is always returned as a floating point
number in *`ACos`*. The angles in *`ACos`* are represented in
radians. The arccosine of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_acos`,
which can be used in an expression in the following syntax:

[`ACos := acos(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  number(-array) `→`  (real / integer)

Input tuple.

Restriction:
`-1 <= T <= 1`

**`ACos`** (output_control)  angle.rad(-array) `→`  (real)

Arccosine of the input tuple.

## Alternatives

`tuple_asin`,
`tuple_atan`,
`tuple_atan2`

## See also

`tuple_cos`,
`tuple_cosh`,
`tuple_acosh`

## Module

Foundation
