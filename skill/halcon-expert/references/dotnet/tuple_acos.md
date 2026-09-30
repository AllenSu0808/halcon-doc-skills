# TupleAcos (Operator)

## Name

`TupleAcos` — Compute the arccosine of a tuple.

## Signature

`static void HOperatorSet.TupleAcos(HTuple t, out HTuple ACos)`

`HTuple HTuple.TupleAcos()`

## Description

`TupleAcos` computes the arccosine of the input tuple
*`t`*. The arccosine is always returned as a floating point
number in *`ACos`*. The angles in *`ACos`* are represented in
radians. The arccosine of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleAcos`,
which can be used in an expression in the following syntax:

[`ACos := acos(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

Restriction:
`-1 <= T <= 1`

**`ACos`** (output_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Arccosine of the input tuple.

## Alternatives

`TupleAsin`,
`TupleAtan`,
`TupleAtan2`

## See also

`TupleCos`,
`TupleCosh`,
`TupleAcosh`

## Module

Foundation
