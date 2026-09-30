# TupleLog2 (Operator)

## Name

`TupleLog2` — Compute the base 2 logarithm of a tuple.

## Signature

`static void HOperatorSet.TupleLog2(HTuple t, out HTuple log)`

`HTuple HTuple.TupleLog2()`

## Description

`TupleLog2` computes the base 2 logarithm of the input
tuple *`t`*. The logarithm is always returned as a floating
point number. The logarithm of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleLog2`,
which can be used in an expression in the following syntax:

[`Log := log2(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_exponential_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

Restriction:
`T > 0`

**`log`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Base 2 logarithm of the input tuple.

## Alternatives

`TupleLog`,
`TupleLog10`

## See also

`TupleExp`,
`TupleExp2`,
`TupleExp10`,
`TuplePow`

## Module

Foundation
