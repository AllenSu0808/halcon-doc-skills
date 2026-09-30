# tuple_abs (Operator)

## Name

`tuple_abs` — Compute the absolute value of a tuple.

## Signature

`def tuple_abs(t: MaybeSequence[Union[float, int]]) -> Sequence[Union[float, int]]`

`def tuple_abs_s(t: MaybeSequence[Union[float, int]]) -> Union[float, int]`

## Description

`tuple_abs` computes the absolute value of the input tuple
*`t`*. The absolute value of an integer number is again an
integer number. The absolute value of a floating point number is a
floating point number. The absolute value of a string is not
allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_abs`,
which can be used in an expression in the following syntax:

[`Abs := abs(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`abs`** (output_control)  number(-array) `→` Sequence[Union[float, int]]

Absolute value of the input tuple.

## Alternatives

`tuple_fabs`

## Module

Foundation
