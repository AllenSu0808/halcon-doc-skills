# tuple_str_bit_select (Operator)

## Name

`tuple_str_bit_select` — Select single character or bit from a tuple.

## Signature

`tuple_str_bit_select( : : Tuple, Index : Selected)`

## Description

`tuple_str_bit_select` selects a single character or bit from
a tuple *`Tuple`* of integer numbers and/or strings.
The input parameter *`Index`* determines the character or bit
position to select. *`Index`* must contain a single number. If
*`Index`* contains a floating point number, this may only
represent an integer value (without fraction). The result tuple
*`Selected`* contains a new element for each element of
*`Tuple`*. Let *`Index`* contain the number “n” then each
element of *`Selected`* consists of the “n-th” character
(for strings) or “n-th” bit (for integers) of the corresponding
element of *`Tuple`*.

If *`Tuple`* is empty, an exception is raised.

### Unicode code points versus bytes

The index reference Unicode code points. One Unicode code point may be
composed of multiple bytes in the UTF-8 string. If the index should
reference the raw bytes of the string, this operator can be switched to byte
mode with `set_system('tsp_tuple_string_operator_mode','byte')`. If
*'filename_encoding'* is set to *'locale'* (legacy), this
operator always uses the byte mode.

For general information about string operations see
[Tuple / String Operations](toc_tuple_stringoperations.md).

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_str_bit_select`,
which can be used in an expression in the following syntax:

[`Selected := Tuple{Index`}](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Tuple`** (input_control)  tuple(-array) `→`  (string / integer)

Input tuple.

**`Index`** (input_control)  integer `→`  (integer)

Position of character or bit to select.

**`Selected`** (output_control)  tuple(-array) `→`  (string / integer)

Tuple containing the selected characters and bits.

## Alternatives

`tuple_select`,
`tuple_first_n`,
`tuple_last_n`,
`tuple_concat`,
`tuple_strchr`,
`tuple_strrchr`,
`tuple_str_first_n`,
`tuple_str_last_n`,
`tuple_substr`,
`tuple_and`,
`tuple_or`,
`tuple_xor`,
`tuple_not`

## See also

`tuple_remove`

## Module

Foundation
