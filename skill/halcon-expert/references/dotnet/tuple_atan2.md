# TupleAtan2 (Operator)

## Name

`TupleAtan2` — Compute the arctangent of a tuple for all four quadrants.

## Signature

`static void HOperatorSet.TupleAtan2(HTuple y, HTuple x, out HTuple ATan)`

`HTuple HTuple.TupleAtan2(HTuple x)`

## Description

`TupleAtan2` computes the arctangent of the input tuples
*`y`*/*`x`* while treating all four quadrants
correctly. The arctangent is always returned as a floating point
number in *`ATan`*. The angles in *`ATan`* are represented in
radians. The arctangent of a string is not allowed.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleAtan2`,
which can be used in an expression in the following syntax:

[`ATan := atan2(Y, X)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_trigonometric_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`y`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple of the y-values.

**`x`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple of the x-values.

**`ATan`** (output_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Arctangent of the input tuple.

## Alternatives

`TupleAtan`,
`TupleAsin`,
`TupleAcos`

## See also

`TupleTan`,
`TupleTanh`

## Module

Foundation
