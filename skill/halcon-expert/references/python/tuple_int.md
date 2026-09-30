# tuple_int (Operator)

## Name

`tuple_int` — Convert a tuple into a tuple of integer numbers.

## Signature

`def tuple_int(t: MaybeSequence[Union[float, int]]) -> Sequence[int]`

`def tuple_int_s(t: MaybeSequence[Union[float, int]]) -> int`

## Description

`tuple_int` converts the input tuple *`t`* into a tuple
of integer numbers by truncating *`t`*. The conversion of a
string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_int`,
which can be used in an expression in the following syntax:

[`Int := int(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_numerical_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple.

**`int`** (output_control)  number(-array) `→` Sequence[int]

Result of the conversion into integer numbers.

## Alternatives

`tuple_round`

## Module

Foundation
