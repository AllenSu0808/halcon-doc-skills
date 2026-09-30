# tuple_concat (Operator)

## Name

`tuple_concat` — Concatenate two tuples to a new one.

## Signature

`def tuple_concat(t1: MaybeSequence[Union[float, int, str]], t2: MaybeSequence[Union[float, int, str]]) -> Sequence[Union[float, int, str]]`

`def tuple_concat_s(t1: MaybeSequence[Union[float, int, str]], t2: MaybeSequence[Union[float, int, str]]) -> Union[float, int, str]`

## Description

`tuple_concat` concatenates the input tuples *`t1`* and
*`t2`* to a new tuple *`concat`*. The first elements of
*`concat`* conform to the elements of *`t1`* and the
remaining elements of *`concat`* conform to those of *`t2`*.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_concat`,
which can be used in an expression in the following syntax:

[`Concat := [T1, T2]`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t1`** (input_control)  tuple(-array) `→` MaybeSequence[Union[float, int, str]]

Input tuple 1.

**`t2`** (input_control)  tuple(-array) `→` MaybeSequence[Union[float, int, str]]

Input tuple 2.

**`concat`** (output_control)  tuple(-array) `→` Sequence[Union[float, int, str]]

Concatenation of input tuples.

## Alternatives

`tuple_gen_const`,
`tuple_str_bit_select`,
`tuple_select`,
`tuple_str_first_n`,
`tuple_str_last_n`,
`tuple_substr`

## See also

`tuple_remove`

## Module

Foundation
