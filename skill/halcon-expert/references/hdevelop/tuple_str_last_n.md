# tuple_str_last_n (Operator)

## Name

`tuple_str_last_n` — Cut all characters starting at position “n” out of a string tuple.

## Signature

`tuple_str_last_n( : : String, Position : Substring)`

## Description

`tuple_str_last_n` cuts all characters from position “n” to the end
of the string out of each string of the input tuple *`String`* and
returns them as new strings in the output tuple *`Substring`*. The
position “n” is determined by the second input tuple *`Position`*. If
*`Position`* only contains one element, this element contains “n”. If
*`String`* and *`Position`* have got the same number of elements,
the first element of *`Position`* determines the start position for the
first string of *`String`*, the second element of *`Position`* does
so for the second string of *`String`* and so on. If *`Position`*
contains more than one element and *`String`* contains only one string,
`tuple_str_last_n` cuts more than one substrings out of this string.
The elements of *`Position`* then determine the start positions for
these substrings. If both input tuples contain more than one element but
differ in the number of elements, `tuple_str_last_n` returns an error.

If both input tuples are empty, the operator returns an empty tuple.
Similarly, if *`String`* is empty and *`Position`* is
not, the operator returns an empty tuple. In contrast, if *`Position`*
is empty and *`String`* is not, an exception is raised.

### Unicode code points versus bytes

The position references Unicode code points. One Unicode code point may be
composed of multiple bytes in the UTF-8 string. If the position should
reference the raw bytes of the string, this operator can be switched to byte
mode with `set_system('tsp_tuple_string_operator_mode','byte')`. If
*'filename_encoding'* is set to *'locale'* (legacy), this
operator always uses the byte mode.

For general information about string operations see
[Tuple / String Operations](toc_tuple_stringoperations.md).

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_str_last_n`,
which can be used in an expression in the following syntax:

[`Substring := str_lastn(String, Position)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`String`** (input_control)  string(-array) `→`  (string)

Input tuple with string(s) to examine.

**`Position`** (input_control)  number(-array) `→`  (integer / real)

Input tuple with position(s) “n”.

**`Substring`** (output_control)  string(-array) `→`  (string)

The last characters of the string(s) starting at position “n”.

## Alternatives

`tuple_str_first_n`,
`tuple_substr`,
`tuple_strstr`,
`tuple_strrstr`,
`tuple_strlen`,
`tuple_strchr`,
`tuple_strrchr`,
`tuple_split`,
`tuple_environment`

## Module

Foundation
