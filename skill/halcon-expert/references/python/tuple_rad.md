# tuple_rad (Operator)

## Name

`tuple_rad` — Convert a tuple from degrees to radians.

## Signature

`def tuple_rad(deg: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_rad_s(deg: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_rad` converts the input tuple *`deg`* from degrees
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

**`deg`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`rad`** (output_control)  number(-array) `→` Sequence[float]

Input tuple in radians.

## See also

`tuple_deg`

## Module

Foundation
