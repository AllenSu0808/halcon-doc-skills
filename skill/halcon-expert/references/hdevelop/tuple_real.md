# tuple_real (Operator)

## Name

`tuple_real` — Convert a tuple into a tuple of floating point numbers.

## Signature

`tuple_real( : : T : Real)`

## Description

`tuple_real` converts the input tuple *`T`* into a tuple
of floating point numbers. The conversion of a string is not
allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_real`,
which can be used in an expression in the following syntax:

[`Real := real(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  number(-array) `→`  (real / integer)

Input tuple.

**`Real`** (output_control)  number(-array) `→`  (real)

Input tuple as floating point numbers.

## Module

Foundation
