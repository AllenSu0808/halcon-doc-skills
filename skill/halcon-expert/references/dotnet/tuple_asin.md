# TupleAsin (Operator)

## Name

`TupleAsin` — Compute the arcsine of a tuple.

## Signature

`static void HOperatorSet.TupleAsin(HTuple t, out HTuple ASin)`

`HTuple HTuple.TupleAsin()`

## Description

`TupleAsin` computes the arcsine of the input tuple
*`t`*. The arcsine is always returned as a floating point
number in *`ASin`*. The angles in *`ASin`* are represented
in radians. The arcsine of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleAsin`,
which can be used in an expression in the following syntax:

[`ASin := asin(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

Restriction:
`-1 <= T <= 1`

**`ASin`** (output_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Arcsine of the input tuple.

## Alternatives

`TupleAcos`,
`TupleAtan`,
`TupleAtan2`

## See also

`TupleSin`,
`TupleSinh`,
`TupleAsinh`

## Module

Foundation
