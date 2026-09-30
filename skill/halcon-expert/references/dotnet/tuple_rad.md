# TupleRad (Operator)

## Name

`TupleRad` — Convert a tuple from degrees to radians.

## Signature

`static void HOperatorSet.TupleRad(HTuple deg, out HTuple rad)`

`HTuple HTuple.TupleRad()`

## Description

`TupleRad` converts the input tuple *`deg`* from degrees
to radians. The result is always returned as a floating point
number. The conversion of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleRad`,
which can be used in an expression in the following syntax:

[`Rad := rad(Deg)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`deg`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`rad`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Input tuple in radians.

## See also

`TupleDeg`

## Module

Foundation
