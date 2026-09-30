# tuple_concat (Operator)

## Name

`tuple_concat` — Concatenate two tuples to a new one.

## Signature

`tuple_concat( : : T1, T2 : Concat)`

## Description

`tuple_concat` concatenates the input tuples *`T1`* and
*`T2`* to a new tuple *`Concat`*. The first elements of
*`Concat`* conform to the elements of *`T1`* and the
remaining elements of *`Concat`* conform to those of *`T2`*.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_concat`,
which can be used in an expression in the following syntax:

[`Concat := [T1, T2]`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T1`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple 1.

**`T2`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple 2.

**`Concat`** (output_control)  tuple(-array) `→`  (integer / real / string)

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
