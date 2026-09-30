# tuple_ceil (Operator)

## Name

`tuple_ceil` — Compute the ceiling function of a tuple.

## Signature

`tuple_ceil( : : T : Ceil)`

## Description

`tuple_ceil` computes the ceiling function of the input tuple
*`T`*, i.e., the smallest integer greater than or equal to
*`T`*. The ceiling function is always returned as a floating
point number. The ceiling function of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_ceil`,
which can be used in an expression in the following syntax:

[`Ceil := ceil(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  number(-array) `→`  (real / integer)

Input tuple.

**`Ceil`** (output_control)  number(-array) `→`  (real)

Ceiling function of the input tuple.

## Module

Foundation
