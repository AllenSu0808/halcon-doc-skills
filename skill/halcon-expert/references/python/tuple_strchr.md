# tuple_strchr (Operator)

## Name

`tuple_strchr` — Forward search for characters within a string tuple.

## Signature

`def tuple_strchr(string: MaybeSequence[str], to_find: MaybeSequence[str]) -> Sequence[int]`

`def tuple_strchr_s(string: MaybeSequence[str], to_find: MaybeSequence[str]) -> int`

## Description

`tuple_strchr` searches within the strings of the input tuple
*`string`* for the characters of the input tuple *`to_find`*. Both
input tuples may only consist of strings. Otherwise `tuple_strchr`
returns an error. If the elements of *`to_find`* contain more than one
character, only the first character of each element is considered for
searching. If *`string`* contains only one string, all the characters
defined in *`to_find`* are searched in this string. Thus, the output tuple
consists of as many elements as *`to_find`*. Whenever a searched
character has been found, the position of its first occurrence gets stored in
the output tuple *`position`* (remark: the position starts at 0 for the
first character of a string). If a character can not be found, -1 will be
returned instead of its position. If both input tuples show the same number
of elements, the search is done elementwise. I.e., the first character of
the first element of *`to_find`* is searched within the first string of
*`string`*, the first character of the second element of *`to_find`*
is searched within the second string of *`string`* and so on. The
results of the elementwise searches are returned with *`position`* that
contains as many elements as *`string`* and *`to_find`*. If
*`to_find`* only contains one string, its first character is searched
within all strings of *`string`*. Thus, in this case *`position`*
consists of as many elements as *`string`*. If both input tuples
contain more than one element and the number of elements differs for the
input tuples, `tuple_strchr` returns an error.

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### Unicode code points versus bytes

The position references Unicode code points. One Unicode code point may be
composed of multiple bytes in the UTF-8 string. If the position should
reference the raw bytes of the string, this operator can be switched to byte
mode with `set_system('tsp_tuple_string_operator_mode','byte')`. If
*"filename_encoding"* is set to *"locale"* (legacy), this
operator always uses the byte mode.

For general information about string operations see
[Tuple / String Operations](toc_tuple_stringoperations.md).

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_strchr`,
which can be used in an expression in the following syntax:

[`Position := strchr(String, ToFind)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`string`** (input_control)  string(-array) `→` MaybeSequence[str]

Input tuple with string(s) to examine.

**`to_find`** (input_control)  string(-array) `→` MaybeSequence[str]

Input tuple with character(s) to search.

**`position`** (output_control)  integer(-array) `→` Sequence[int]

Position of searched character(s) within the string(s).

## Alternatives

`tuple_strrchr`,
`tuple_strstr`,
`tuple_strrstr`,
`tuple_strlen`,
`tuple_substr`,
`tuple_str_first_n`,
`tuple_str_last_n`,
`tuple_split`,
`tuple_environment`

## Module

Foundation
