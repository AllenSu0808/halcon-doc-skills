# tuple_split (Operator)

## Name

`tuple_split` — Split strings into substrings using predefined separator symbol(s).

## Signature

`tuple_split( : : String, Separator : Substrings)`

## Description

`tuple_split` searches within the strings of the input tuple
*`String`* for the separators defined in the input tuple
*`Separator`*.
`tuple_split` then splits the examined strings into
the substrings divided by the separators and returns them in the
tuple *`Substrings`*.
The behavior depends on the length of the input tuples:

- *`Separator`* contains only one string:
  Every string in *`String`* is split up according to the
  separator symbols in *`Separator`*.
  E.g., *`String`* = *['alpha:1', 'beta:2', 'gamma:3']*
  and *`Separator`* = *['a:']*.
  In this case, the operator returns the tuple *`Substrings`* =
  *['lph', '1', 'bet', '2', 'g', 'mm', '3']*.
- *`String`* contains only one string:
  The single string is split up for every element in *`Separator`*.
  E.g., *`String`* = *['alpha:1 beta:2 gamma:3']* and
  *`Separator`* = *[':', '123']*. In this case, the output
  tuple *`Substrings`* will comprise the substrings
  *'alpha'*, *'1'*, *'beta'*, *'2'*,
  *'gamma'*, and *'3'*, as the result of splitting the string
  of *`String`* according to the first element of *`Separator`*
  (*':'*) as well as *'alpha:'*, *'beta:'*, and
  *'gamma:'* as the result of splitting according to the second
  element of *`Separator`* (*'123'*).
- Both tuples consist of the same amount of strings:
  The search is done elementwise.
  I.e., `tuple_split` will split the first string of *`String`*
  according to the separator symbols in the first element of
  *`Separator`*, the second string of *`String`* according to the
  separator symbols in the second element of *`Separator`* and so on.
- Either or both of the input tuples are empty:
  An empty tuple is returned.

Notes to *`Separator`*:
If an element of *`Separator`* contains more than one character,
each character defines a separator (see the example given above).
Subsequent occurrences of *`Separator`* in *`String`* are
treated as one separator.
Separators at the beginning and the end of *`String`* will not
result in an empty string.

Please consider, both input tuples (*`String`* and *`Separator`*)
may only consist of strings. Otherwise `tuple_split` returns an error.
If both input tuples contain more than one element and the number of
elements differs for the input tuples, `tuple_split` returns an error.

### Unicode code points versus bytes

The split characters are interpreted as Unicode code points. One Unicode
code point may be composed of multiple bytes in the UTF-8 string.
If the split characters should be handled as raw bytes of the string, this
operator can be switched to byte mode with
`set_system('tsp_tuple_string_operator_mode','byte')`.
If *'filename_encoding'* is set to *'locale'* (legacy), this
operator always uses the byte mode.

For general information about string operations see
[Tuple / String Operations](toc_tuple_stringoperations.md).

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_split`,
which can be used in an expression in the following syntax:

[`Substrings := split(String, Separator)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`String`** (input_control)  string(-array) `→`  (string)

Input tuple with string(s) to split.

**`Separator`** (input_control)  string(-array) `→`  (string)

Input tuple with separator symbol(s).

**`Substrings`** (output_control)  string(-array) `→`  (string)

Substrings after splitting the input strings.

## Alternatives

`tuple_strstr`,
`tuple_strrstr`,
`tuple_strchr`,
`tuple_strrchr`,
`tuple_strlen`,
`tuple_str_first_n`,
`tuple_str_last_n`,
`tuple_environment`

## Module

Foundation
