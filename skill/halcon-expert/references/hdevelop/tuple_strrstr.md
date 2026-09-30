# tuple_strrstr (Operator)

## Name

`tuple_strrstr` — Backward search for strings within a string tuple.

## Signature

`tuple_strrstr( : : String, ToFind : Position)`

## Description

`tuple_strrstr` searches within the strings of the input tuple
*`String`* for the strings of the input tuple *`ToFind`*. Both
input tuples may only consist of strings. Otherwise `tuple_strrstr`
returns an error. In any case backward search is used, i.e., every string is
examined from its last to its first character. If *`String`* contains
only one string, all strings of *`ToFind`* are searched in it. Thus, the
output tuple consists of as many elements as *`ToFind`*. Whenever a
searched string has been found, the position of its first occurrence gets
stored in the output tuple *`Position`* (positions in strings are
counted starting with 0). If a string can not be found, -1 will be returned
instead of its position. If both input tuples show the same number of
elements, the strings are searched elementwise. I.e., the first string of
*`ToFind`* is searched within the first string of *`String`*, the
second string of *`ToFind`* is searched within the second string of
*`String`* and so on. The results of the elementwise searches are
returned with *`Position`* that contains as many elements as
*`String`* and *`ToFind`*. If *`ToFind`* only contains one
string, this is searched within all strings of *`String`*. Thus, in this
case *`Position`* consists of as many elements as *`String`*. If
both input tuples contain more than one element and the number of elements
differs for the input tuples, `tuple_strrstr` returns an error.

If either or both of the input tuples are empty, the operator returns an
empty tuple.

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

HDevelop provides an in-line operation for `tuple_strrstr`,
which can be used in an expression in the following syntax:

[`Position := strrstr(String, ToFind)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`String`** (input_control)  string(-array) `→`  (string)

Input tuple with string(s) to examine.

**`ToFind`** (input_control)  string(-array) `→`  (string)

Input tuple with string(s) to search.

**`Position`** (output_control)  integer(-array) `→`  (integer)

Position of searched string(s) within the examined string(s).

## Alternatives

`tuple_strstr`,
`tuple_strlen`,
`tuple_strchr`,
`tuple_strrchr`,
`tuple_substr`,
`tuple_str_first_n`,
`tuple_str_last_n`,
`tuple_split`,
`tuple_environment`

## Module

Foundation
