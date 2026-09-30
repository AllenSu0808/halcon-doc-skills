# TupleSgn (Operator)

## Name

`TupleSgn` — Calculate the sign of a tuple.

## Signature

`static void HOperatorSet.TupleSgn(HTuple t, out HTuple sgn)`

`HTuple HTuple.TupleSgn()`

## Description

`TupleSgn` calculates the sign of the elements of the
input tuple *`t`* and returns them as integer numbers
(-1,0,1) in the output tuple *`sgn`*.
The calculation of the sign of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleSgn`,
which can be used in an expression in the following syntax:

[`Sgn := sgn(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`sgn`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long)

Signs of the input tuple as integer numbers.

## Module

Foundation
