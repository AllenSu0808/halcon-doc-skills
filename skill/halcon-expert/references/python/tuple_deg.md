# tuple_deg (Operator)

## Name

`tuple_deg` — Convert a tuple from radians to degrees.

## Signature

`def tuple_deg(rad: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def tuple_deg_s(rad: MaybeSequence[Union[float, int]]) -> float`

## Description

`tuple_deg` converts the input tuple *`rad`* from radians
to degrees. The result is always returned as a floating point
number. The conversion of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_deg`,
which can be used in an expression in the following syntax:

[`Deg := deg(Rad)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`rad`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`deg`** (output_control)  number(-array) `→` Sequence[float]

Input tuple in degrees.

## See also

`tuple_rad`

## Module

Foundation
