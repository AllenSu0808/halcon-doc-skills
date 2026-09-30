# tuple_inverse (Operator)

## Name

`tuple_inverse` — Invert a tuple.

## Signature

`def tuple_inverse(tuple: MaybeSequence[Union[float, int, str]]) -> Sequence[Union[float, int, str]]`

`def tuple_inverse_s(tuple: MaybeSequence[Union[float, int, str]]) -> Union[float, int, str]`

## Description

`tuple_inverse` inverts the input tuple *`tuple`*. Thus,
*`inverted`* contains the same elements as *`tuple`* but with
the reverse order.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_inverse`,
which can be used in an expression in the following syntax:

[`Inverted := inverse(Tuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_misc_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` MaybeSequence[Union[float, int, str]]

Input tuple.

**`inverted`** (output_control)  tuple(-array) `→` Sequence[Union[float, int, str]]

Inverted input tuple.

## Alternatives

`tuple_sort`,
`tuple_sort_index`

## Module

Foundation
