# tuple_rad (Operator)

## Name

`tuple_rad` — Convert a tuple from degrees to radians.

## Signature

`tuple_rad( : : Deg : Rad)`

## Description

`tuple_rad` converts the input tuple *`Deg`* from degrees
to radians. The result is always returned as a floating point
number. The conversion of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_rad`,
which can be used in an expression in the following syntax:

[`Rad := rad(Deg)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Deg`** (input_control)  number(-array) `→`  (real / integer)

Input tuple.

**`Rad`** (output_control)  number(-array) `→`  (real)

Input tuple in radians.

## See also

`tuple_deg`

## Module

Foundation
