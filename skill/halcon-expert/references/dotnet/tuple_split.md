# TupleSplit (Operator)

## Name

`TupleSplit` — Split strings into substrings using predefined separator symbol(s).

## Signature

`static void HOperatorSet.TupleSplit(HTuple stringVal, HTuple separator, out HTuple substrings)`

`HTuple HTuple.TupleSplit(HTuple separator)`

## Description

`TupleSplit` searches within the strings of the input tuple
*`stringVal`* for the separators defined in the input tuple
*`separator`*.
`TupleSplit` then splits the examined strings into
the substrings divided by the separators and returns them in the
tuple *`substrings`*.
The behavior depends on the length of the input tuples:

- *`separator`* contains only one string:
  Every string in *`stringVal`* is split up according to the
  separator symbols in *`separator`*.
  E.g., *`stringVal`* = *["alpha:1", "beta:2", "gamma:3"]*
  and *`separator`* = *["a:"]*.
  In this case, the operator returns the tuple *`substrings`* =
  *["lph", "1", "bet", "2", "g", "mm", "3"]*.
- *`stringVal`* contains only one string:
  The single string is split up for every element in *`separator`*.
  E.g., *`stringVal`* = *["alpha:1 beta:2 gamma:3"]* and
  *`separator`* = *[":", "123"]*. In this case, the output
  tuple *`substrings`* will comprise the substrings
  *"alpha"*, *"1"*, *"beta"*, *"2"*,
  *"gamma"*, and *"3"*, as the result of splitting the string
  of *`stringVal`* according to the first element of *`separator`*
  (*":"*) as well as *"alpha:"*, *"beta:"*, and
  *"gamma:"* as the result of splitting according to the second
  element of *`separator`* (*"123"*).
- Both tuples consist of the same amount of strings:
  The search is done elementwise.
  I.e., `TupleSplit` will split the first string of *`stringVal`*
  according to the separator symbols in the first element of
  *`separator`*, the second string of *`stringVal`* according to the
  separator symbols in the second element of *`separator`* and so on.
- Either or both of the input tuples are empty:
  An empty tuple is returned.

Notes to *`separator`*:
If an element of *`separator`* contains more than one character,
each character defines a separator (see the example given above).
Subsequent occurrences of *`separator`* in *`stringVal`* are
treated as one separator.
Separators at the beginning and the end of *`stringVal`* will not
result in an empty string.

Please consider, both input tuples (*`stringVal`* and *`separator`*)
may only consist of strings. Otherwise `TupleSplit` returns an error.
If both input tuples contain more than one element and the number of
elements differs for the input tuples, `TupleSplit` returns an error.

### Unicode code points versus bytes

The split characters are interpreted as Unicode code points. One Unicode
code point may be composed of multiple bytes in the UTF-8 string.
If the split characters should be handled as raw bytes of the string, this
operator can be switched to byte mode with
`set_system('tsp_tuple_string_operator_mode','byte')`.
If *"filename_encoding"* is set to *"locale"* (legacy), this
operator always uses the byte mode.

For general information about string operations see
[Tuple / String Operations](toc_tuple_stringoperations.md).

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleSplit`,
which can be used in an expression in the following syntax:

[`Substrings := split(String, Separator)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`stringVal`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Input tuple with string(s) to split.

**`separator`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Input tuple with separator symbol(s).

**`substrings`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Substrings after splitting the input strings.

## Alternatives

`TupleStrstr`,
`TupleStrrstr`,
`TupleStrchr`,
`TupleStrrchr`,
`TupleStrlen`,
`TupleStrFirstN`,
`TupleStrLastN`,
`TupleEnvironment`

## Module

Foundation
