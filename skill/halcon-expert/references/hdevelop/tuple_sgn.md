# tuple_sgn (Operator)

## Name

`tuple_sgn` — Calculate the sign of a tuple.

## Signature

`tuple_sgn( : : T : Sgn)`

## Description

`tuple_sgn` calculates the sign of the elements of the
input tuple *`T`* and returns them as integer numbers
(-1,0,1) in the output tuple *`Sgn`*.
The calculation of the sign of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_sgn`,
which can be used in an expression in the following syntax:

[`Sgn := sgn(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  number(-array) `→`  (real / integer)

Input tuple.

**`Sgn`** (output_control)  number(-array) `→`  (integer)

Signs of the input tuple as integer numbers.

## Module

Foundation
