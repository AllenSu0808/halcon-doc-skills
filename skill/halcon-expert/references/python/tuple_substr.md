# tuple_substr (Operator)

## Name

`tuple_substr` — Cut characters from position “n1” through “n2” out of a string tuple.

## Signature

`def tuple_substr(string: MaybeSequence[str], position_1: MaybeSequence[Union[float, int]], position_2: MaybeSequence[Union[float, int]]) -> Sequence[str]`

`def tuple_substr_s(string: MaybeSequence[str], position_1: MaybeSequence[Union[float, int]], position_2: MaybeSequence[Union[float, int]]) -> str`

## Description

`tuple_substr` cuts all characters from position “n1” through “n2”
out of each string of the input tuple *`string`* and
returns them as new strings in the output tuple *`substring`*. The
positions “n1” and “n2” are determined by the second and third input
tuples *`position_1`* and *`position_2`*. Their
length has to be equal. If *`position_1`* and *`position_2`* only
contain one element, this element defines for all strings of
*`string`* “n1” and “n2”, respectively . If
*`string`*, *`position_1`* and *`position_2`* have got the
same number of elements, the first elements of *`position_1`* and
*`position_2`* determine the start and end position for the
first string of *`string`*. The second elements of *`position_1`*
and *`position_2`* do so for the second string of *`string`*
and so on. If *`position_1`* and *`position_2`*
contain more than one element and *`string`* contains only one string,
`tuple_substr` cuts more than one substring out of this string.
The elements of *`position_1`* and *`position_2`* then determine
the start and end positions for
these substrings. If all input tuples contain more than one element but
differ in the number of elements, `tuple_substr` returns an error.

If *`string`* is an empty tuple, the operator returns an empty tuple.
If *`string`* is not empty and *`position_1`* and/or
*`position_2`* are empty tuples, an exception is raised.

### Unicode code points versus bytes

The positions reference Unicode code points. One Unicode code point may be
composed of multiple bytes in the UTF-8 string. If the positions should
reference the raw bytes of the string, this operator can be switched to byte
mode with `set_system('tsp_tuple_string_operator_mode','byte')`. If
*"filename_encoding"* is set to *"locale"* (legacy), this
operator always uses the byte mode.

For general information about string operations see
[Tuple / String Operations](toc_tuple_stringoperations.md).

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_substr`,
which can be used in an expression in the following syntax:

[`Substring := String{Position1:Position2`}](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`string`** (input_control)  string(-array) `→` MaybeSequence[str]

Input tuple with string(s) to examine.

**`position_1`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple with start position(s) “n1”.

**`position_2`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input tuple with end position(s) “n2”.

**`substring`** (output_control)  string(-array) `→` Sequence[str]

Characters of the string(s) from position “n1” to “n2”.

## Alternatives

`tuple_str_first_n`,
`tuple_str_last_n`,
`tuple_strstr`,
`tuple_strrstr`,
`tuple_strlen`,
`tuple_strchr`,
`tuple_strrchr`,
`tuple_split`,
`tuple_environment`

## Module

Foundation
