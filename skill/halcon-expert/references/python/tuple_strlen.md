# tuple_strlen (Operator)

## Name

`tuple_strlen` — Determine the length of every string within a tuple of strings.

## Signature

`def tuple_strlen(t1: MaybeSequence[str]) -> Sequence[int]`

`def tuple_strlen_s(t1: MaybeSequence[str]) -> int`

## Description

`tuple_strlen` checks the length of every string within the
input tuple *`t1`* and returns the length of each string with
the output tuple *`length`*. All elements of *`t1`*
may only consist of strings. Otherwise `tuple_strlen` returns an
error.

If the input tuple is empty, the operator returns an empty tuple.

### Unicode code points versus bytes

The string length references Unicode code points. One Unicode code point may
be composed of multiple bytes in the UTF-8 string. If the length should
reference the raw bytes of the string, this operator can be switched to byte
mode with `set_system('tsp_tuple_string_operator_mode','byte')`. If
*"filename_encoding"* is set to *"locale"* (legacy), this
operator always uses the byte mode.

For general information about string operations see
[Tuple / String Operations](toc_tuple_stringoperations.md).

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_strlen`,
which can be used in an expression in the following syntax:

[`Length := strlen(T1)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t1`** (input_control)  string(-array) `→` MaybeSequence[str]

Input tuple.

**`length`** (output_control)  integer(-array) `→` Sequence[int]

Lengths of the single strings of the input tuple.

## Alternatives

`tuple_strstr`,
`tuple_strrstr`,
`tuple_strchr`,
`tuple_strrchr`,
`tuple_substr`,
`tuple_str_first_n`,
`tuple_str_last_n`,
`tuple_split`,
`tuple_environment`

## See also

`tuple_is_string`

## Module

Foundation
