# tuple_chr (Operator)

## Name

`tuple_chr` — Convert a tuple of integer numbers into strings.

## Signature

`tuple_chr( : : T : Chr)`

## Description

`tuple_chr` converts the input tuple *`T`*, consisting of integer
numbers, into a tuple of strings, each of length 1.
When the encoding used in the HALCON library is UTF-8 (see
`set_system('filename_encoding', 'utf8')`) and the string operators
are set to work by code points (see
`set_system('tuple_string_operator_mode', 'codepoint')`), which is the
default for both, the operator accepts Unicode character codes and
returns strings with the appropriate UTF-8 representations of the characters.
When the HALCON library encoding is set to *'locale'* or the string
operator mode is *'byte'*, the operator accepts only numbers between
0 and 256.
In that case the operator `tuple_chr` returns strings with one byte
length each, where the input number is set as ANSI code.
See also [Tuple / String Operations](toc_tuple_stringoperations.md) for a more detailed description
of the different modes and further encoding issues.

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_chr`,
which can be used in an expression in the following syntax:

[`Chr := chr(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_misc_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  integer(-array) `→`  (integer)

Input tuple with Unicode character codes or ANSI codes.

Restriction:
`0 <= T`

**`Chr`** (output_control)  string(-array) `→`  (string)

Output tuple with strings built from the character codes in the
input tuple.

## Alternatives

`tuple_chrt`

## See also

`tuple_ord`,
`tuple_ords`

## Module

Foundation
