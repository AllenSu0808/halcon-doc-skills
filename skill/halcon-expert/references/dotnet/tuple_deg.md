# TupleDeg (Operator)

## Name

`TupleDeg` — Convert a tuple from radians to degrees.

## Signature

`static void HOperatorSet.TupleDeg(HTuple rad, out HTuple deg)`

`HTuple HTuple.TupleDeg()`

## Description

`TupleDeg` converts the input tuple *`rad`* from radians
to degrees. The result is always returned as a floating point
number. The conversion of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleDeg`,
which can be used in an expression in the following syntax:

[`Deg := deg(Rad)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`rad`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`deg`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Input tuple in degrees.

## See also

`TupleRad`

## Module

Foundation
